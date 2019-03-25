from iconservice import Address
import timeit
import hashlib


# 시간 측정할 메서드
def runtime(f, data):
    start = timeit.default_timer()
    for i in enumerate(range(0, 1000000)):
        f(data)
    end = timeit.default_timer()
    print(end - start)


hex_string = '041e110fa67887498246b20fe42374880bccee4962ef849508f3d68fe66034d15cfb347af4609eda3b84afc652c108be7650e595e458b1f916eecad7d27a8b35a0'
public_key = bytes.fromhex(hex_string)
print(public_key.hex())

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
    # if isinstance(public_key, bytes):
    #     size = len(public_key)
    #     prefix: bytes = public_key[0]
    #
    #     if size == 33 and prefix in (0x02, 0x03):
    #         uncompressed_public_key: bytes = _convert_key(public_key)
    #     elif size == 65 and prefix == 0x04:
    #         uncompressed_public_key: bytes = public_key
    #     else:
    #         return None

    body: bytes = hashlib.sha3_256(public_key[1:]).digest()[-20:]
    return Address("0x", body)

runtime(create_address_with_key, public_key)

# timeit.timeit('create_address_with_key(public_key)', number= 1)