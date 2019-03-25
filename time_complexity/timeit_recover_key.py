import timeit


# 시간 측정할 메서드
def runtime(f, msg_hash, signature):
    start = timeit.default_timer()
    for i in enumerate(range(0, 10000000)):
        f(msg_hash, signature)
    end = timeit.default_timer()
    print(end - start)


msg_hash = b'1257b9ea76e716b145463f0350f534f973399898a18a50d391e7d2815e72c950'
signature = b'5a245303fb54346541c9cf1fb19efe53d0520d7e01701bafd8ea40b8e2cb6f352209ca2f2cf0ee144f8f05a4fca2f9b3e7083e063afbae62a2bbb465f2fd035101'
# PublicKey =


def recover_key(msg_hash: bytes, signature: bytes, compressed: bool = True):
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


def _recover_key(msg_hash: bytes, signature: bytes, compressed: False):
    """Returns the public key from message hash and recoverable signature
    :param msg_hash: 32 bytes data
    :param signature: signature_data(64) + recovery_id(1)
    :param compressed: the type of public key to return
    :return: public key recovered from msg_hash and signature
        (compressed: 33 bytes key, uncompressed: 65 bytes key)
    """
    # if isinstance(msg_hash, bytes) \
    #         and len(msg_hash) == 32 \
    #         and isinstance(signature, bytes) \
    #         and len(signature) == 65:
    #     internal_recover_sig = _public_key.ecdsa_recoverable_deserialize(
    #         ser_sig=signature[:64], rec_id=signature[64])
    #     internal_pubkey = _public_key.ecdsa_recover(
    #         msg_hash, internal_recover_sig, raw=True, digest=None)

    public_key = PublicKey(internal_pubkey, raw=False, ctx=_public_key.ctx)
    return public_key.serialize(compressed)


runtime(recover_key, msg_hash, signature)

