
<div align="center">

<img  src="https://raw.githubusercontent.com/ImperatorLang/eopsin/c485feda7b5e7eb0d835f3ad39eed679b96aa05c/eopsin.png" width="240" />
<h1 style="text-align: center;">hebi</h1></br>


[![Build Status](https://app.travis-ci.com/ImperatorLang/hebi.svg?branch=master)](https://app.travis-ci.com/ImperatorLang/hebi)
[![PyPI version](https://badge.fury.io/py/hebi.svg)](https://pypi.org/project/hebi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hebi.svg)
[![PyPI - Status](https://img.shields.io/pypi/status/hebi.svg)](https://pypi.org/project/hebi/)
[![Coverage Status](https://coveralls.io/repos/github/ImperatorLang/hebi/badge.svg?branch=master)](https://coveralls.io/github/ImperatorLang/hebi?branch=master)

</div>

> DISCLAIMER: This is a rough first draft, based on [eopsin](https://github.com/ImperatorLang/eopsin).
> If you are looking for a working product, first look there.

This is an implementation of smart contracts for Cardano which are written in a very strict subset of valid Python.
The general philosophy of this project is to write a compiler that 
ensure the following:

If the program compiles then:
1. it is a valid Python program
2. the output running it with python is the same as running it on-chain.

### Why hebi?
- 100% valid Python. Leverage the existing tool stack for Python, syntax highlighting, linting, debugging, unit-testing, [property-based testing](https://hypothesis.readthedocs.io/), [verification](https://github.com/marcoeilers/nagini)
- Intuitive. Just like Python.
- Flexible. Imperative, functional, the way you want it.
- Efficient & Secure. Static type inference ensures strict typing and optimized code


### Getting Started

#### Developer Community and Questions

This repository contains a discussions page.
Feel free to open up a new discussion with questions regarding development using hebi and using certain features.
Others may be able to help you and will also benefit from the previously shared questions.

Check out the community [here](https://github.com/ImperatorLang/hebi/discussions)

#### Installation

Install Python 3.8. Then run

```bash
python3.8 -m pip install hebi
```

#### Writing a Smart Contract

A short non-complete introduction in starting to write smart contracts follows.

1. Make sure you understand python. Hebi works like python and uses python. There are tons of tutorials for python, choose what suits you best.
2. Make sure your contract is valid python and the types check out. Write simple contracts first and run them using `hebi eval` to get a feeling for how they work.
3. Make sure your contract is valid hebi code. Run `hebi compile` and look at the compiler erros for guidance along what works and doesn't work and why.
4. Dig into the [`examples`](https://github.com/ImperatorLang/hebi/tree/master/examples) to understand common patterns. Check out the [`prelude`](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py) for understanding how the Script Context is structured and how complex datums are defined.

A simple contract called the "Gift Contract" verifies that only specific wallets can withdraw money.
They are authenticated by a signature.
See the [tutorial by `pycardano`](https://pycardano.readthedocs.io/en/latest/guides/plutus.html) for explanations on what each of the parameters to the validator means
and how to build transactions with the contract.

```python3
from hebi.prelude import *

@dataclass()
class CancelDatum(PlutusData):
    pubkeyhash: bytes


def validator(datum: CancelDatum, redeemer: None, context: ScriptContext) -> None:
    sig_present = False
    for s in context.tx_info.signatories:
        if datum.pubkeyhash == s:
            sig_present = True
    assert sig_present, "Required signature missing"
```

All contracts written in hebi are 100% valid python.
Minting policies follow the same structure, but expect a value of type `None` as first argument.
See the `examples` directory for more.

### Compiling

Write your program in python. You may start with the content of `examples`.
Arguments to scripts are passed in as Plutus Data objects in JSON notation.

You can run any of the following commands
```bash
# Evaluate script in Python - this can be used to make sure there are no obvious errors
hebi eval examples/smart_contracts/assert_sum.py "{\"int\": 4}" "{\"int\": 38}" "{\"constructor\": 0, \"fields\": []}"

# Compile script to 'uplc', the Cardano Smart Contract assembly
hebi compile examples/smart_contracts/assert_sum.py
```

### Deploying

The deploy process generates all artifacts required for usage with common libraries like [pycardano](https://github.com/Python-Cardano/pycardano), [lucid](https://github.com/spacebudz/lucid) and the [cardano-cli](https://github.com/input-output-hk/cardano-node).

```bash
# Automatically generate all artifacts needed for using this contract
hebi build examples/smart_contracts/assert_sum.py
```

See the [tutorial by `pycardano`](https://pycardano.readthedocs.io/en/latest/guides/plutus.html) for explanations how to build transactions with `hebi` contracts.

### The small print

_Not every valid python program is a valid smart contract_.
Not all language features of python will or can be supported.
The reasons are mainly of practical nature (i.e. we can't infer types when functions like `eval` are allowed).
Specifically, only a pure subset of python is allowed.
Further, only immutable objects may be generated.

For your program to be accepted, make sure to only make use of language constructs supported by the compiler.
You will be notified of which constructs are not supported when trying to compile.

### Name

Hebi is japanese for "snake", which is a play on words on python, the underlying language.

## Contributing

### Architecture

This program consists of a few independent components:
1. An aggressive static type inferencer
2. Rewriting tools to simplify complex python expressions
3. A compiler from a subset of python into UPLC

### Debugging artefacts

For debugging purposes, you can also run

```bash
# Compile script to 'uplc', and evaluate the script in UPLC (for debugging purposes)
python3 -m hebi eval_uplc examples/smart_contracts/assert_sum.py "{\"int\": 4}" "{\"int\": 38}" "{\"constructor\": 0, \"fields\": []}"

# Compile script to 'pluto', an intermediate language (for debugging purposes)
python3 -m hebi compile_pluto examples/smart_contracts/assert_sum.py
```

### Sponsoring

You can sponsor the development of hebi. Just drop me a message on social media and let me know what it is for.
Donation in ADA can be submitted to `$imperatorlang` or `addr1qyz3vgd5xxevjy2rvqevz9n7n7dney8n6hqggp23479fm6vwpj9clsvsf85cd4xc59zjztr5zwpummwckmzr2myjwjns74lhmr`.

### Supporters

<a href="https://github.com/MuesliSwapTeam/"><img  src="https://avatars.githubusercontent.com/u/91151317?v=4" width="50" /></a>
<a href="https://github.com/AadaFinance/"><img  src="https://avatars.githubusercontent.com/u/89693711?v=4" width="50" /></a>
