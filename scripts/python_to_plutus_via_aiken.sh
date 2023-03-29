#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 -m hebi compile /dev/stdin | bash uplc_to_cbor.sh | python3 cbor_to_plutus.py