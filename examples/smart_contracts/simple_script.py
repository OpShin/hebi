from hebi.prelude import *


@dataclass()
class RequireSignature(PlutusData):
    CONSTR_ID = 0
    vkeyhash: bytes  # this is either a PubKeyHash or a VerificationKeyHash


@dataclass()
class RequireAllOf(PlutusData):
    CONSTR_ID = 1
    scripts: List[Datum]  # "Script"


@dataclass()
class RequireAnyOf(PlutusData):
    CONSTR_ID = 2
    scripts: List[Datum]  # "Script"


@dataclass()
class RequireMOf(PlutusData):
    CONSTR_ID = 3
    num: int
    scripts: List[Datum]  # "Script"


@dataclass()
class RequireBefore(PlutusData):
    CONSTR_ID = 4
    unixtimestamp: int


@dataclass()
class RequireAfter(PlutusData):
    CONSTR_ID = 5
    unixtimestamp: int


Script = Union[
    RequireSignature,
    RequireMOf,
    RequireAnyOf,
    RequireAllOf,
    RequireAfter,
    RequireBefore,
]


def validate_script(
    script_raw: Datum, signatories: List[bytes], valid_range: POSIXTimeRange
) -> bool:
    script: Script = script_raw  # cast to Script in the type system to avoid recursive type definition
    if isinstance(script, RequireSignature):
        return script.vkeyhash in signatories
    elif isinstance(script, RequireAllOf):
        return all(
            [validate_script(s, signatories, valid_range) for s in script.scripts]
        )
    elif isinstance(script, RequireAnyOf):
        return any(
            [validate_script(s, signatories, valid_range) for s in script.scripts]
        )
    elif isinstance(script, RequireMOf):
        return (
            sum(
                [
                    1 if validate_script(s, signatories, valid_range) else 0
                    for s in script.scripts
                ]
            )
            >= script.num
        )
    elif isinstance(script, RequireBefore):
        upper_bound = valid_range.upper_bound
        upper_limit = upper_bound.limit
        if isinstance(upper_limit, FinitePOSIXTime):
            upper_closed = upper_bound.closed
            if isinstance(upper_closed, TrueData):
                return upper_limit.time <= script.unixtimestamp
            else:
                return upper_limit.time < script.unixtimestamp
        elif isinstance(upper_limit, PosInfPOSIXTime):
            return False
        elif isinstance(upper_limit, NegInfPOSIXTime):
            return True
    elif isinstance(script, RequireAfter):
        lower_bound = valid_range.lower_bound
        lower_limit = lower_bound.limit
        if isinstance(lower_limit, FinitePOSIXTime):
            lower_closed = lower_bound.closed
            if isinstance(lower_closed, TrueData):
                return lower_limit.time >= script.unixtimestamp
            else:
                return lower_limit.time > script.unixtimestamp
        elif isinstance(lower_limit, PosInfPOSIXTime):
            return True
        elif isinstance(lower_limit, NegInfPOSIXTime):
            return False
    assert False, "Invalid simple script passed"


# to fully emulate simple script behaviour, compile with --force-three-params
# the script is a contract parameter, pass it into the build command
def validator(
    script: Script, datum: None, redeemer: None, context: ScriptContext
) -> None:
    assert validate_script(
        script, context.tx_info.signatories, context.tx_info.valid_range
    ), "Simple Script validation failed!"
