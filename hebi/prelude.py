from hashlib import sha256, sha3_256, blake2b
from hebi.ledger.api_v2 import *


@dataclass(unsafe_hash=True)
class Token(PlutusData):
    """
    A token, represented by policy id and token name
    """

    policy_id: PolicyId
    token_name: TokenName


# Used to indicate that this contract does not expect a redeemer
NoRedeemer = Nothing

### Optimized methods for handling tokens at addresses


def all_tokens_unlocked_from_address(
    txins: List[TxInInfo], address: Address, token: Token
) -> int:
    """Returns how many tokens of specified type are unlocked from given address"""
    return sum(
        [
            txi.resolved.value.get(token.policy_id, {b"": 0}).get(token.token_name, 0)
            for txi in txins
            if txi.resolved.address == address
        ]
    )


def all_tokens_locked_at_address_with_datum(
    txouts: List[TxOut], address: Address, token: Token, output_datum: OutputDatum
) -> int:
    """Returns how many tokens of specified type are locked at then given address with the specified datum"""
    return sum(
        [
            txo.value.get(token.policy_id, {b"": 0}).get(token.token_name, 0)
            for txo in txouts
            if txo.address == address and txo.datum == output_datum
        ]
    )


def all_tokens_locked_at_address(
    txouts: List[TxOut], address: Address, token: Token
) -> int:
    """Returns how many tokens of specified type are locked at the given address"""
    return sum(
        [
            txo.value.get(token.policy_id, {b"": 0}).get(token.token_name, 0)
            for txo in txouts
            if txo.address == address
        ]
    )


def resolve_spent_utxo(txins: List[TxInInfo], p: Spending) -> TxOut:
    """Returns the UTxO whose spending should be validated"""
    return [txi.resolved for txi in txins if txi.out_ref == p.tx_out_ref][0]


def resolve_datum_unsafe(txout: TxOut, tx_info: TxInfo) -> BuiltinData:
    """
    Returns the datum attached to a given transaction output, independent of whether it was inlined or embedded.
    Raises an exception if no datum was attached.
    """
    attached_datum = txout.datum
    if isinstance(attached_datum, SomeOutputDatumHash):
        return tx_info.data[attached_datum.datum_hash]
    elif isinstance(attached_datum, SomeOutputDatum):
        return attached_datum.datum
    else:
        # no datum attached
        assert False, "No datum was attached to the given transaction output"


def resolve_datum(
    txout: TxOut, tx_info: TxInfo
) -> Union[SomeOutputDatum, NoOutputDatum]:
    """
    Returns SomeOutputDatum with the datum attached to a given transaction output,
    independent of whether it was inlined or embedded, if there was an attached datum.
    Otherwise it returns NoOutputDatum.
    """
    attached_datum = txout.datum
    if isinstance(attached_datum, SomeOutputDatumHash):
        res: Union[SomeOutputDatum, NoOutputDatum] = SomeOutputDatum(
            tx_info.data[attached_datum.datum_hash]
        )
    else:
        res: Union[SomeOutputDatum, NoOutputDatum] = attached_datum
    return res
