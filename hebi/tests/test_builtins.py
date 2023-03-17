import unittest

import parameterized
from hypothesis import example, given
from hypothesis import strategies as st
from uplc import ast as uplc, eval as uplc_eval

from .. import compiler


class BuiltinTest(unittest.TestCase):
    @given(xs=st.lists(st.booleans()))
    def test_all(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[bool]) -> bool:
    return all(x)
            """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusList([uplc.PlutusInteger(int(x)) for x in xs])]:
            f = uplc.Apply(f, d)
        ret = bool(uplc_eval(f).value)
        self.assertEqual(ret, all(xs), "all returned wrong value")

    @given(xs=st.lists(st.booleans()))
    def test_any(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[bool]) -> bool:
    return any(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusList([uplc.PlutusInteger(int(x)) for x in xs])]:
            f = uplc.Apply(f, d)
        ret = bool(uplc_eval(f).value)
        self.assertEqual(ret, any(xs), "any returned wrong value")

    @given(i=st.integers())
    def test_abs(self, i):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> int:
    return abs(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        try:
            for d in [uplc.PlutusInteger(i)]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except Exception as e:
            ret = None
        self.assertEqual(ret, abs(i), "abs returned wrong value")

    @given(
        xs=st.one_of(
            st.lists(st.integers()), st.lists(st.integers(min_value=0, max_value=255))
        )
    )
    def test_bytes_int_list(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> bytes:
    return bytes(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        try:
            exp = bytes(xs)
        except ValueError:
            exp = None
        try:
            for d in [uplc.PlutusList([uplc.PlutusInteger(x) for x in xs])]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "bytes (integer list) returned wrong value")

    @given(i=st.integers())
    @example(256)
    @example(0)
    def test_chr(self, i):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> str:
    return chr(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        try:
            i_unicode = chr(i).encode("utf8")
        except (ValueError, OverflowError):
            i_unicode = None
        try:
            for d in [uplc.PlutusInteger(i)]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except Exception as e:
            ret = None
        self.assertEqual(ret, i_unicode, "chr returned wrong value")

    @given(x=st.integers())
    @example(0)
    @example(-1)
    @example(100)
    def test_hex(self, x):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> str:
    return hex(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusInteger(x)]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value.decode("utf8")
        self.assertEqual(ret, hex(x), "hex returned wrong value")

    @unittest.skip("Integer stripping is currently broken")
    @given(xs=st.one_of(st.builds(lambda x: str(x), st.integers()), st.text()))
    @example("")
    @example("10_00")
    @example("_")
    @example("_1")
    @example("0\n")
    def test_int_string(self, xs: str):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: str) -> int:
    return int(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        try:
            exp = int(xs)
        except ValueError:
            exp = None
        try:
            for d in [uplc.PlutusByteString(xs.encode("utf8"))]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "str (integer) returned wrong value")

    @parameterized.parameterized.expand(
        ["10_00", "00", "_", "_1", "-10238", "19293812983721837981", "jakjsdh"]
    )
    def test_int_string(self, xs: str):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: str) -> int:
    return int(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        try:
            exp = int(xs)
        except ValueError:
            exp = None
        try:
            for d in [uplc.PlutusByteString(xs.encode("utf8"))]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "str (integer) returned wrong value")

    @given(i=st.binary())
    def test_len_bytestring(self, i):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: bytes) -> int:
    return len(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusByteString(i)]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value
        self.assertEqual(ret, len(i), "len (bytestring) returned wrong value")

    @given(xs=st.lists(st.integers()))
    def test_len_lists(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> int:
    return len(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusList([uplc.PlutusInteger(x) for x in xs])]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value
        self.assertEqual(ret, len(xs), "len returned wrong value")

    @given(xs=st.lists(st.integers()))
    def test_max(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> int:
    return max(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        try:
            exp = max(xs)
        except ValueError:
            exp = None
        try:
            f = code.term
            # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
            for d in [uplc.PlutusList([uplc.PlutusInteger(int(x)) for x in xs])]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "max returned wrong value")

    @given(xs=st.lists(st.integers()))
    def test_min(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> int:
    return min(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        try:
            exp = min(xs)
        except ValueError:
            exp = None
        try:
            f = code.term
            # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
            for d in [uplc.PlutusList([uplc.PlutusInteger(int(x)) for x in xs])]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "min returned wrong value")

    @given(x=st.integers(), y=st.integers(min_value=0, max_value=20))
    def test_pow(self, x: int, y: int):
        source_code = """
def validator(x: int, y: int) -> int:
    return pow(x, y) % 10000000000
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        try:
            exp = pow(x, y) % 10000000000
        except ValueError:
            exp = None
        try:
            for d in [uplc.PlutusInteger(x), uplc.PlutusInteger(y)]:
                f = uplc.Apply(f, d)
            ret = uplc_eval(f).value
        except:
            ret = None
        self.assertEqual(ret, exp, "pow returned wrong value")

    @given(x=st.integers())
    @example(0)
    @example(-1)
    @example(100)
    def test_oct(self, x):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> str:
    return oct(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusInteger(x)]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value.decode("utf8")
        self.assertEqual(ret, oct(x), "oct returned wrong value")

    @given(i=st.integers(max_value=100))
    def test_range(self, i):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> List[int]:
    return range(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusInteger(i)]:
            f = uplc.Apply(f, d)
        ret = [x.value for x in uplc_eval(f).value]
        self.assertEqual(ret, list(range(i)), "sum returned wrong value")

    @given(x=st.integers())
    @example(0)
    @example(-1)
    @example(100)
    def test_str_int(self, x):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> str:
    return str(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusInteger(x)]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value.decode("utf8")
        self.assertEqual(ret, str(x), "str returned wrong value")

    @given(xs=st.lists(st.integers()))
    def test_sum(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> int:
    return sum(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusList([uplc.PlutusInteger(x) for x in xs])]:
            f = uplc.Apply(f, d)
        ret = uplc_eval(f).value
        self.assertEqual(ret, sum(xs), "sum returned wrong value")

    @given(xs=st.lists(st.integers()))
    def test_reversed(self, xs):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: List[int]) -> List[int]:
    return reversed(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusList([uplc.PlutusInteger(x) for x in xs])]:
            f = uplc.Apply(f, d)
        ret = [x.value for x in uplc_eval(f).value]
        self.assertEqual(ret, list(reversed(xs)), "reversed returned wrong value")

    @given(x=st.integers())
    def test_bool_constr_int(self, x):
        # this tests that errors that are caused by assignments are actually triggered at the time of assigning
        source_code = """
def validator(x: int) -> bool:
    return bool(x)
        """
        ast = compiler.parse(source_code)
        code = compiler.compile(ast)
        code = code.compile()
        f = code.term
        # UPLC lambdas may only take one argument at a time, so we evaluate by repeatedly applying
        for d in [uplc.PlutusInteger(x)]:
            f = uplc.Apply(f, d)
        ret = bool(uplc_eval(f).value)
        self.assertEqual(ret, bool(x), "reversed returned wrong value")
