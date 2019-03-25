# -*- coding: utf-8 -*-

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import json
import time
import xlsxwriter
from typing import Optional, Any

from secp256k1 import PublicKey, ALL_FLAGS, FLAG_VERIFY, NO_FLAGS

_public_key = PublicKey(flags=ALL_FLAGS)


def sha3_256(data: bytes) -> bytes:
    """
    Computes hash using the input data

    :param data: input data
    :return: hashed data in bytes
    """
    return hashlib.sha3_256(data).digest()


def json_dumps(obj: Any, **kwargs) -> str:
    """
    Converts a python object `obj` to a JSON string

    :param obj: a python object to be converted
    :param kwargs: json options (see https://docs.python.org/3/library/json.html#json.dumps)
    :return: json string
    """
    return json.dumps(obj, **kwargs)


def json_loads(src: str, **kwargs) -> Any:
    """
    Parses a JSON string `src` and converts it to a python object

    :param src: a JSON string to be converted
    :param kwargs: kwargs: json options (see https://docs.python.org/3/library/json.html#json.loads)
    :return: a python object
    """
    return json.loads(src, **kwargs)


def create_address_with_key(public_key: bytes):
    """Create an address with a given public key, charging a fee

    :param public_key: Public key based on secp256k1
    :return: Address created from a given public key or None if failed
    """
    # FIXME: Add step calculation code
    try:
        return _create_address_with_key(public_key)
    except:
        return None


def _create_address_with_key(public_key: bytes):
    """Create an address with a given public key

    :param public_key: Public key based on secp256k1
    :return: Address created from a given public key or None if failed
    """
    if isinstance(public_key, bytes):
        size = len(public_key)
        prefix: bytes = public_key[0]

        if size == 33 and prefix in (0x02, 0x03):
            uncompressed_public_key: bytes = _convert_key(public_key)
        elif size == 65 and prefix == 0x04:
            uncompressed_public_key: bytes = public_key
        else:
            return None

        body: bytes = hashlib.sha3_256(uncompressed_public_key[1:]).digest()[-20:]
        return body

    return None


def _convert_key(public_key: bytes) -> Optional[bytes]:
    """Convert key between compressed and uncompressed keys

    :param public_key: compressed or uncompressed key
    :return: the counterpart key of a given public_key
    """
    size = len(public_key)
    if size == 33:
        compressed = True
    elif size == 65:
        compressed = False
    else:
        return None

    public_key = PublicKey(public_key, raw=True, flags=NO_FLAGS, ctx=_public_key.ctx)
    return public_key.serialize(compressed=not compressed)


def recover_key(msg_hash: bytes, signature: bytes, compressed: bool = True) -> Optional[bytes]:
    """Returns the public key from message hash and recoverable signature, charging a fee

    :param msg_hash: 32 bytes data
    :param signature: signature_data(64) + recovery_id(1)
    :param compressed: the type of public key to return
    :return: public key recovered from msg_hash and signature
        (compressed: 33 bytes key, uncompressed: 65 bytes key)
    """
    # FIXME: Add step calculation code
    try:
        return _recover_key(msg_hash, signature, compressed)
    except:
        return None


def _recover_key(msg_hash: bytes, signature: bytes, compressed: bool) -> Optional[bytes]:
    """Returns the public key from message hash and recoverable signature

    :param msg_hash: 32 bytes data
    :param signature: signature_data(64) + recovery_id(1)
    :param compressed: the type of public key to return
    :return: public key recovered from msg_hash and signature
        (compressed: 33 bytes key, uncompressed: 65 bytes key)
    """
    if isinstance(msg_hash, bytes) \
            and len(msg_hash) == 32 \
            and isinstance(signature, bytes) \
            and len(signature) == 65:
        internal_recover_sig = _public_key.ecdsa_recoverable_deserialize(
            ser_sig=signature[:64], rec_id=signature[64])
        internal_pubkey = _public_key.ecdsa_recover(
            msg_hash, internal_recover_sig, raw=True, digest=None)

        public_key = PublicKey(internal_pubkey, raw=False, ctx=_public_key.ctx)
        return public_key.serialize(compressed)

    # change logic to check the time
    return None


def evaluate_sha3_256(repeat: int, count: int, increase: int = 10, byte_size: int = 32):
    timer = Timer()
    worksheet = workbook.add_worksheet("sha3_256")
    worksheet.write(0, 0, f"repeat:{repeat}")
    worksheet.write(0, 1, f"count:{count}")
    row = 1
    col = 1

    public_key: bytes = bytes.fromhex("041e110fa67887498246b20fe42374880bccee4962ef849508f3d68fe66034d15cfb347af4609eda3b84afc652c108be7650e595e458b1f916eecad7d27a8b35a0")
    unit_data: bytes = public_key[:byte_size]

    for i in range(0, increase):
        data = unit_data * i
        worksheet.write(row, col, len(data))

        for _ in range(count):
            row += 1
            timer.start()
            for _ in range(repeat):
                sha3_256(data)
            timer.stop()
            worksheet.write(row, col, timer.duration)
        col += 1
        row = 1


def evaluate_recover_key(repeat: int, count: int):
    timer = Timer()
    msg_hash: bytes = bytes.fromhex('1257b9ea76e716b145463f0350f534f973399898a18a50d391e7d2815e72c950')
    signature: bytes = bytes.fromhex('5a245303fb54346541c9cf1fb19efe53d0520d7e01701bafd8ea40b8e2cb6f352209ca2f2cf0ee144f8f05a4fca2f9b3e7083e063afbae62a2bbb465f2fd035101')

    worksheet = workbook.add_worksheet("recover_key")
    worksheet.write(0, 0, f"repeat:{repeat}")
    worksheet.write(0, 1, f"count:{count}")
    row = 1
    col = 1
    worksheet.write(0, 2, f"msg_hash size:{len(msg_hash)}")
    worksheet.write(0, 3, f"sig size:{len(signature)}")
    worksheet.write(row, col, "uncompressed")
    worksheet.write(row, col + 1, "compressed")
    for _ in range(count):
        row += 1
        timer.start()
        for _ in range(repeat):
            recover_key(msg_hash, signature, False)
        timer.stop()
        worksheet.write(row, col, timer.duration)
        timer.start()
        for _ in range(repeat):
            recover_key(msg_hash, signature, True)
        timer.stop()
        worksheet.write(row, col+1, timer.duration)


def evaluate_create_address_with_key(repeat: int, count: int):
    timer = Timer()
    uncompressed_public_key: bytes = bytes.fromhex(
        "041e110fa67887498246b20fe42374880bccee4962ef849508f3d68fe66034d15cfb347af4609eda3b84afc652c108be7650e595e458b1f916eecad7d27a8b35a0")
    compressed_public_key: bytes = bytes.fromhex("02") + uncompressed_public_key[1:33]
    print(f"public key size(uncompressed):{len(uncompressed_public_key)}")
    print(f"public key size(compressed):{len(compressed_public_key)}")
    print(f"public key(uncompressed):{uncompressed_public_key}")
    print(f"public key(compressed):{compressed_public_key}")

    worksheet = workbook.add_worksheet("create_address")
    worksheet.write(0, 0, f"repeat:{repeat}")
    worksheet.write(0, 1, f"count:{count}")

    row = 1
    col = 1
    worksheet.write(row, col, "uncompressed")
    worksheet.write(row, col + 1, "compressed")
    for _ in range(count):
        row += 1
        timer.start()
        for _ in range(repeat):
            create_address_with_key(uncompressed_public_key)
        timer.stop()
        worksheet.write(row, col, timer.duration)
        timer.start()
        for _ in range(repeat):
            create_address_with_key(compressed_public_key)
        timer.stop()

        worksheet.write(row, col+1, timer.duration)


class Timer(object):
    def __init__(self):
        super().__init__()
        self.start_time: float = 0.0
        self.stop_time: float = 0.0
        self.duration: float = 0.0

    def start(self) -> float:
        self.start_time = time.monotonic()
        return self.start_time

    def stop(self) -> float:
        self.stop_time = time.monotonic()
        self.duration: float = self.stop_time - self.start_time

        return self.stop_time

    def __str__(self) -> str:
        return f'{self.duration: 0.6f}'


def main():

    repeat: int = 1_000
    count: int = 50
    global workbook

    workbook = xlsxwriter.Workbook('test.xlsx')

    print("sha3 256 evaluate start")
    evaluate_sha3_256(repeat, count, increase=50)
    print("sha3 256 evaluate end")

    print("recover key evaluate start")
    evaluate_recover_key(repeat, count)
    print("recover key evaluate end")

    print("create address with key evaluate start")
    evaluate_create_address_with_key(repeat, count)
    print("create address with key evaluate end")

    workbook.close()


if __name__ == '__main__':
    # msg_hash: bytes = bytes.fromhex('1257b9ea76e716b145463f0350f534f973399898a18a50d391e7d2815e72c950')
    # signature: bytes = bytes.fromhex(
    #     '5a245303fb54346541c9cf1fb19efe53d0520d7e01701bafd8ea40b8e2cb6f352209ca2f2cf0ee144f8f05a4fca2f9b3e7083e063afbae62a2bbb465f2fd035101')
    # recovered_uncompressed_public_key = recover_key(msg_hash, signature, False)
    # print(recovered_uncompressed_public_key)
    # recovered_compressed_public_key = recover_key(msg_hash, signature, True)
    # print(recovered_compressed_public_key)
    # print(create_address_with_key(recovered_uncompressed_public_key) == create_address_with_key(recovered_compressed_public_key))
    # print(create_address_with_key(recovered_compressed_public_key))

    main()