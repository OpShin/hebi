
<div align="center">

<img  src="https://raw.githubusercontent.com/OpShin/hebi/master/hebi.png" width="240" />
<h1 style="text-align: center;">hebi</h1></br>


[![Build Status](https://app.travis-ci.com/OpShin/hebi.svg?branch=master)](https://app.travis-ci.com/OpShin/hebi)
[![PyPI version](https://badge.fury.io/py/hebi.svg)](https://pypi.org/project/hebi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hebi.svg)
[![PyPI - Status](https://img.shields.io/pypi/status/hebi.svg)](https://pypi.org/project/hebi/)
[![Coverage Status](https://coveralls.io/repos/github/OpShin/hebi/badge.svg?branch=master)](https://coveralls.io/github/OpShin/hebi?branch=master)

</div>

> Note this is the sister project of [eopsin](https://github.com/ImperatorLang/eopsin).
It uses an even more restricted subset of python (for example no while loops).
The benefit is that the resulting code is greatly reduced in size and cpu/memory consumption.


This is an implementation of smart contracts for Cardano which are written in a very strict subset of valid Python.
The general philosophy of this project is to write a compiler that 
ensure the following:

If the program compiles then:
1. it is a valid Python program
2. the output running it with python is the same as running it on-chain.

### Why hebi?
- 100% valid Python. Leverage the existing tool stack for Python, syntax highlighting, linting, debugging, unit-testing, [property-based testing](https://hypothesis.readthedocs.io/), [verification](https://github.com/marcoeilers/nagini)
- Intuitive. Just like Python.
- Functional. Forces you to write elegant, functional code in Python.
- Efficient & Secure. Static type inference ensures strict typing and optimized code

Eopsin is more comfortable to use than hebi.
If you want to start building, write your contract in eopsin first.
Then, after everything works to your pleasing, try to port to hebi and enjoy the performance gains.

### Getting Started

#### Example repository

Check out this example repository for a quick start in setting up a development environment
and compiling some sample contracts yours:

https://github.com/OpShin/eopsin-example

You can replace the contracts in your local copy of the repository with code from the
`examples` section here to start exploring different contracts.

#### Developer Community and Questions

The eopsin repository contains a discussions page.
Feel free to open up a new discussion with questions regarding development using hebi and using certain features.
Others may be able to help you and will also benefit from the previously shared questions.

Check out the community [here](https://github.com/OpShin/eopsin/discussions)

You can also chat with other developers [in the welcoming discord
community](https://discord.gg/2ETSZnQQH9) of OpShin

#### Installation

Install Python 3.8. Then run

```bash
python3.8 -m pip install hebi
```

#### Writing a Smart Contract

A short non-complete introduction in starting to write smart contracts follows.

1. Make sure you understand EUTxOs, Addresses, Validators etc on Cardano. [There is a wonderful crashcourse by @KtorZ](https://aiken-lang.org/fundamentals/eutxo). The contract will work on these concepts
2. Make sure you understand python. Eopsin works like python and uses python. There are tons of tutorials for python, choose what suits you best.
3. Make sure your contract is valid python and the types check out. Write simple contracts first and run them using `hebi eval` to get a feeling for how they work.
4. Make sure your contract is valid hebi code. Run `hebi compile` and look at the compiler erros for guidance along what works and doesn't work and why.
5. Dig into the [`examples`](https://github.com/OpShin/hebi/tree/master/examples) to understand common patterns. Check out the [`prelude`](https://imperatorlang.github.io/hebi/hebi/prelude.html) for understanding how the Script Context is structured and how complex datums are defined.
6. Check out the [sample repository](https://github.com/OpShin/eopsin-example) to find a sample setup for developing your own contract.


In summary, a smart contract in hebi is defined by the function `validator` in your contract file.
The function validates that a specific value can be spent, minted, burned, withdrawn etc, depending
on where it is invoked/used as a credential.
If the function fails (i.e. raises an error of any kind such as a `KeyError` or `AssertionError`)
the validation is denied, and the funds can not be spent, minted, burned etc.

> There is a subtle difference here in comparison to most other Smart Contract languages.
> In hebi a validator may return anything (in particular also `False`) - as long as it does not fail, the execution is considered valid.
> This is more similar to how contracts in Solidity always pass, unless they run out of gas or hit an error.
> So make sure to `assert` what you want to ensure to hold for validation!

A simple contract called the "Gift Contract" verifies that only specific wallets can withdraw money.
They are authenticated by a signature.
If you don't understand what a pubkeyhash is and how this validates anything, check out [this gentle introduction into Cardanos EUTxO](https://aiken-lang.org/fundamentals/eutxo).
Also see the [tutorial by `pycardano`](https://pycardano.readthedocs.io/en/latest/guides/plutus.html) for explanations on what each of the parameters to the validator means
and how to build transactions with the contract.


```python3
from hebi.prelude import *

@dataclass()
class CancelDatum(PlutusData):
    pubkeyhash: bytes


def validator(datum: CancelDatum, redeemer: None, context: ScriptContext) -> None:
    assert datum.pubkeyhash in context.tx_info.signatories, "Required signature missing"
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

See the [tutorial by `pycardano`](https://pycardano.readthedocs.io/en/latest/guides/plutus.html) for explanations how to build transactions with `eopsin` contracts.
Contracts in hebi are invoked the same, so you can just follow the tutorial there.

### The small print

_Not every valid python program is a valid smart contract_.
Not all language features of python will or can be supported.
The reasons are mainly of practical nature (i.e. we can't infer types when functions like `eval` are allowed).
Specifically, only a pure subset of python is allowed.
Further, only immutable objects may be generated.

For your program to be accepted, make sure to only make use of language constructs supported by the compiler.
You will be notified of which constructs are not supported when trying to compile.

### Name

Hebi is japanese for "snake", which is a play on words on `python`, the underlying language.

### Versioning scheme

Since this project builds on top of eopsin, it has a particular versioning scheme.
The first three numbers indicate the version of `hebi` (starting at `0.1.0`).
Then follows the latest version number of `eopsin` which was merged into the project (starting at `0.9.3`).
This is intended to help navigating releases among both packages, where it might be important
that a recent eopsin release is integrated that contains a security patch.

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

You can sponsor the development of hebi through GitHub or [Teiki](https://alpha.teiki.network/projects/opshin) or just by sending ADA. Drop me a message on social media and let me know what it is for.

- **[Teiki](https://alpha.teiki.network/projects/opshin)** Stake your ada to support OpShin at [Teiki](https://alpha.teiki.network/projects/opshin)
- **GitHub** Sponsor the developers of this project through the button "Sponsor" next to them
- **ADA** Donation in ADA can be submitted to `$opshin` or `addr1qyz3vgd5xxevjy2rvqevz9n7n7dney8n6hqggp23479fm6vwpj9clsvsf85cd4xc59zjztr5zwpummwckmzr2myjwjns74lhmr`.

### Supporters

<a href="https://github.com/inversion-dev"><img src="https://avatars.githubusercontent.com/u/127298233?s=200&v=4" width="50"></a>
<a href="https://github.com/MuesliSwapTeam/"><img  src="https://avatars.githubusercontent.com/u/91151317?v=4" width="50" /></a>
<a href="https://github.com/AadaFinance/"><img  src="https://avatars.githubusercontent.com/u/89693711?v=4" width="50" /></a>
