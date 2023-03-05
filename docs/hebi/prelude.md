# Prelude

[hebi Index](../README.md#hebi-index) /
[Hebi](./index.md#hebi) /
Prelude

> Auto-generated documentation for [hebi.prelude](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py) module.

#### Attributes

- `BoolData` - A Datum that represents a boolean value in Haskell implementations.
  It is thus used as an encoding for booleans in the ScriptContext.
  
  Example value: TrueData(): `Union[TrueData, FalseData]`

- `PubKeyHash` - A public key hash, used to identify signatures provided by a wallet: `bytes`

- `ValidatorHash` - A validator hash, used to identify signatures provided by a smart contract: `bytes`

- `Credential` - A credential, either smart contract or public key hash: `Union[PubKeyCredential, ScriptCredential]`

- `StakingCredential` - Part of an address that controls who can delegate the stake associated with an address: `Union[StakingHash, StakingPtr]`

- `PolicyId` - The policy Id of a token: `bytes`

- `TokenName` - The name of a token in bytes (not textual representation!): `bytes`

- `Value` - The Plutus representation of amounts of tokens being spent, sent or minted
  It is a two-layered dictionary that stores for each policy id and token name
  the amount of the token that is being sent/minted/burned etc
  
  Lovelace is represented with policy id b"" and token name b"": `Dict[PolicyId, Dict[TokenName, int]]`

- `DatumHash` - A hash of a Datum: `bytes`

- `BuiltinData` - The abstract super type of any object in eopsin.
  Use if you don't know what kind of object is being passed or if it doesn't matter.: `Anything`

- `Redeemer` - An abstract type annotation that something is supposed to be used as a redeemer.: `BuiltinData`

- `Datum` - An abstract type annotation that something is supposed to be used as a datum.: `BuiltinData`

- `OutputDatum` - Possible cases of datum association with an output: `Union[NoOutputDatum, SomeOutputDatumHash, SomeOutputDatum]`

- `ScriptPurpose` - The reason that this script is being invoked: `Union[Minting, Spending, Rewarding, Certifying]`

- `NoRedeemer` - Used to indicate that this contract does not expect a redeemer: `Nothing`


- [Prelude](#prelude)
  - [Address](#address)
  - [Certifying](#certifying)
  - [DCertDelegDeRegKey](#dcertdelegderegkey)
  - [DCertDelegDelegate](#dcertdelegdelegate)
  - [DCertDelegRegKey](#dcertdelegregkey)
  - [DCertGenesis](#dcertgenesis)
  - [DCertMir](#dcertmir)
  - [DCertPoolRegister](#dcertpoolregister)
  - [DCertPoolRetire](#dcertpoolretire)
  - [FalseData](#falsedata)
  - [FinitePOSIXTime](#finiteposixtime)
  - [LowerBoundPOSIXTime](#lowerboundposixtime)
  - [Minting](#minting)
  - [NegInfPOSIXTime](#neginfposixtime)
  - [NoOutputDatum](#nooutputdatum)
  - [NoScriptHash](#noscripthash)
  - [NoStakingCredential](#nostakingcredential)
  - [Nothing](#nothing)
  - [POSIXTimeRange](#posixtimerange)
  - [PosInfPOSIXTime](#posinfposixtime)
  - [PubKeyCredential](#pubkeycredential)
  - [Rewarding](#rewarding)
  - [ScriptContext](#scriptcontext)
  - [ScriptCredential](#scriptcredential)
  - [SomeDatumHash](#somedatumhash)
  - [SomeOutputDatum](#someoutputdatum)
  - [SomeOutputDatumHash](#someoutputdatumhash)
  - [SomeScriptHash](#somescripthash)
  - [SomeStakingCredential](#somestakingcredential)
  - [Spending](#spending)
  - [StakingHash](#stakinghash)
  - [StakingPtr](#stakingptr)
  - [Token](#token)
  - [TrueData](#truedata)
  - [TxId](#txid)
  - [TxInInfo](#txininfo)
  - [TxInfo](#txinfo)
  - [TxOut](#txout)
  - [TxOutRef](#txoutref)
  - [UpperBoundPOSIXTime](#upperboundposixtime)
  - [all_tokens_locked_at_address](#all_tokens_locked_at_address)
  - [all_tokens_locked_at_address_with_datum](#all_tokens_locked_at_address_with_datum)
  - [all_tokens_unlocked_from_address](#all_tokens_unlocked_from_address)
  - [resolve_spent_utxo](#resolve_spent_utxo)

## Address

[Show source in prelude.py:162](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L162)

A Shelley address, consisting of a payment and staking credential

#### Signature

```python
class Address(PlutusData):
    ...
```



## Certifying

[Show source in prelude.py:437](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L437)

#### Signature

```python
class Certifying(PlutusData):
    ...
```



## DCertDelegDeRegKey

[Show source in prelude.py:296](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L296)

#### Signature

```python
class DCertDelegDeRegKey(PlutusData):
    ...
```



## DCertDelegDelegate

[Show source in prelude.py:302](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L302)

#### Signature

```python
class DCertDelegDelegate(PlutusData):
    ...
```



## DCertDelegRegKey

[Show source in prelude.py:290](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L290)

#### Signature

```python
class DCertDelegRegKey(PlutusData):
    ...
```



## DCertGenesis

[Show source in prelude.py:323](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L323)

#### Signature

```python
class DCertGenesis(PlutusData):
    ...
```



## DCertMir

[Show source in prelude.py:328](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L328)

#### Signature

```python
class DCertMir(PlutusData):
    ...
```



## DCertPoolRegister

[Show source in prelude.py:309](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L309)

#### Signature

```python
class DCertPoolRegister(PlutusData):
    ...
```



## DCertPoolRetire

[Show source in prelude.py:316](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L316)

#### Signature

```python
class DCertPoolRetire(PlutusData):
    ...
```



## FalseData

[Show source in prelude.py:44](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L44)

A Datum that represents False in Haskell implementations.
It is thus used as an encoding for False in the ScriptContext.

Example value: FalseData()

#### Signature

```python
class FalseData(PlutusData):
    ...
```



## FinitePOSIXTime

[Show source in prelude.py:356](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L356)

Finite POSIX time, used to indicate that there is a lower or upper bound for the execution of this transaction

#### Signature

```python
class FinitePOSIXTime(PlutusData):
    ...
```



## LowerBoundPOSIXTime

[Show source in prelude.py:389](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L389)

Lower bound for the execution of this transaction

#### Signature

```python
class LowerBoundPOSIXTime(PlutusData):
    ...
```



## Minting

[Show source in prelude.py:410](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L410)

Script purpose indicating that the given policy id is being minted or burned

#### Signature

```python
class Minting(PlutusData):
    ...
```



## NegInfPOSIXTime

[Show source in prelude.py:347](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L347)

Negative infinite POSIX time, used to indicate that there is no lower bound for the execution of this transaction

#### Signature

```python
class NegInfPOSIXTime(PlutusData):
    ...
```



## NoOutputDatum

[Show source in prelude.py:222](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L222)

Indicates that there is no datum associated with an output

#### Signature

```python
class NoOutputDatum(PlutusData):
    ...
```



## NoScriptHash

[Show source in prelude.py:255](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L255)

Indicates that there is no script associated with an output

#### Signature

```python
class NoScriptHash(PlutusData):
    ...
```



## NoStakingCredential

[Show source in prelude.py:141](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L141)

Indicates that this address has no staking credentials.
Its funds can not be delegated.

#### Signature

```python
class NoStakingCredential(PlutusData):
    ...
```



## Nothing

[Show source in prelude.py:20](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L20)

#### Attributes

- `CONSTR_ID` - The maximimum constructor ID for simple cbor types, chosen to minimize probability of collision while keeping the corresponding cbor small: `6`


Nothing, can be used to signify non-importance of a parameter to a function

Example value: Nothing()

#### Signature

```python
class Nothing(PlutusData):
    ...
```



## POSIXTimeRange

[Show source in prelude.py:400](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L400)

Time range in which this transaction can be executed

#### Signature

```python
class POSIXTimeRange(PlutusData):
    ...
```



## PosInfPOSIXTime

[Show source in prelude.py:366](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L366)

Infinite POSIX time, used to indicate that there is no upper bound for the execution of this transaction

#### Signature

```python
class PosInfPOSIXTime(PlutusData):
    ...
```



## PubKeyCredential

[Show source in prelude.py:77](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L77)

Part of an address that is authenticated by a public key hash

Example value: PubKeyCredential(bytes.fromhex("c06ddaad12fc4ded18e56feac72957c1aa75fce6096b40e63ec88274"))

#### Signature

```python
class PubKeyCredential(PlutusData):
    ...
```



## Rewarding

[Show source in prelude.py:431](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L431)

#### Signature

```python
class Rewarding(PlutusData):
    ...
```



## ScriptContext

[Show source in prelude.py:468](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L468)

Auxiliary information about the transaction and reason for invocation of the called script.

#### Signature

```python
class ScriptContext(PlutusData):
    ...
```



## ScriptCredential

[Show source in prelude.py:93](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L93)

Part of an address that is authenticated by a smart cotnract

Example value: ScriptCredential(bytes.fromhex("c06ddaad12fc4ded18e56feac72957c1aa75fce6096b40e63ec88274"))

#### Signature

```python
class ScriptCredential(PlutusData):
    ...
```



## SomeDatumHash

[Show source in prelude.py:189](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L189)

Indicates that there is a datum associated with this output, which has the given hash.

#### Signature

```python
class SomeDatumHash(PlutusData):
    ...
```



## SomeOutputDatum

[Show source in prelude.py:241](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L241)

Indicates that there is an datum associated with an output, which is inlined and equal to the attached datum

#### Signature

```python
class SomeOutputDatum(PlutusData):
    ...
```



## SomeOutputDatumHash

[Show source in prelude.py:231](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L231)

Indicates that there is an datum associated with an output, which has the attached hash

#### Signature

```python
class SomeOutputDatumHash(PlutusData):
    ...
```



## SomeScriptHash

[Show source in prelude.py:199](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L199)

Indicates that there is a script associated with this output, which has the given hash.

#### Signature

```python
class SomeScriptHash(PlutusData):
    ...
```



## SomeStakingCredential

[Show source in prelude.py:151](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L151)

Indicates that this address has staking credentials.
Its funds can be delegated by the credentialed user.

#### Signature

```python
class SomeStakingCredential(PlutusData):
    ...
```



## Spending

[Show source in prelude.py:420](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L420)

Script purpose indicating that the given transaction output is being spent, which is
owned by the invoked contract

#### Signature

```python
class Spending(PlutusData):
    ...
```



## StakingHash

[Show source in prelude.py:109](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L109)

Indicates that the stake of this address is controlled by the associated credential

#### Signature

```python
class StakingHash(PlutusData):
    ...
```



## StakingPtr

[Show source in prelude.py:119](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L119)

Indicates that the stake of this address is controlled by the associated pointer.

In an address, a chain pointer refers to a point of the chain containing a stake key registration certificate.
A point is identified by the 3 coordinates in this object.

#### Signature

```python
class StakingPtr(PlutusData):
    ...
```



## Token

[Show source in prelude.py:478](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L478)

A token, represented by policy id and token name

#### Signature

```python
class Token(PlutusData):
    ...
```



## TrueData

[Show source in prelude.py:32](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L32)

A Datum that represents True in Haskell implementations.
It is thus used as an encoding for True in the ScriptContext.

Example value: TrueData()

#### Signature

```python
class TrueData(PlutusData):
    ...
```



## TxId

[Show source in prelude.py:9](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L9)

A transaction id, a 64 bytes long hash of the transaction body (also called transaction hash).

Example value: TxId(bytes.fromhex("842a4d37b036da6ab3c04331240e67d81746beb44f23ad79703e026705361956"))

#### Signature

```python
class TxId(PlutusData):
    ...
```



## TxInInfo

[Show source in prelude.py:280](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L280)

The plutus representation of an transaction output, that is consumed by the transaction.

#### Signature

```python
class TxInInfo(PlutusData):
    ...
```



## TxInfo

[Show source in prelude.py:447](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L447)

A complex agglomeration of everything that could be of interest to the executed script, regarding the transaction
that invoked the script

#### Signature

```python
class TxInfo(PlutusData):
    ...
```



## TxOut

[Show source in prelude.py:264](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L264)

The plutus representation of an transaction output, consisting of
- address: address owning this output
- value: tokens associated with this output
- datum: datum associated with this output
- reference_script: reference script associated with this output

#### Signature

```python
class TxOut(PlutusData):
    ...
```



## TxOutRef

[Show source in prelude.py:63](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L63)

A reference to a transaction output (hash/id + index)

#### Signature

```python
class TxOutRef(PlutusData):
    ...
```



## UpperBoundPOSIXTime

[Show source in prelude.py:378](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L378)

Upper bound for the execution of this transaction

#### Signature

```python
class UpperBoundPOSIXTime(PlutusData):
    ...
```



## all_tokens_locked_at_address

[Show source in prelude.py:519](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L519)

Returns how many tokens of specified type are locked at the given address

#### Signature

```python
def all_tokens_locked_at_address(
    txouts: List[TxOut], address: Address, token: Token
) -> int:
    ...
```

#### See also

- [Address](#address)
- [Token](#token)



## all_tokens_locked_at_address_with_datum

[Show source in prelude.py:506](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L506)

Returns how many tokens of specified type are locked at then given address with the specified datum

#### Signature

```python
def all_tokens_locked_at_address_with_datum(
    txouts: List[TxOut], address: Address, token: Token, output_datum: OutputDatum
) -> int:
    ...
```

#### See also

- [Address](#address)
- [OutputDatum](#outputdatum)
- [Token](#token)



## all_tokens_unlocked_from_address

[Show source in prelude.py:493](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L493)

Returns how many tokens of specified type are unlocked from given address

#### Signature

```python
def all_tokens_unlocked_from_address(
    txins: List[TxInInfo], address: Address, token: Token
) -> int:
    ...
```

#### See also

- [Address](#address)
- [Token](#token)



## resolve_spent_utxo

[Show source in prelude.py:532](https://github.com/ImperatorLang/hebi/blob/master/hebi/prelude.py#L532)

Returns the UTxO whose spending should be validated

#### Signature

```python
def resolve_spent_utxo(txins: List[TxInInfo], p: Spending) -> TxOut:
    ...
```

#### See also

- [Spending](#spending)
- [TxOut](#txout)