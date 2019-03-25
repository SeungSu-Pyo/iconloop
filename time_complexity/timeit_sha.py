from hashlib import sha3_256
import timeit


# 시간 측정할 메서드
def runtime(f, data):
    start = timeit.default_timer()
    for i in enumerate(range(0, 10000000)):
        f(data)
    end = timeit.default_timer()
    print(end - start)


def sha3_256(data: bytes) -> bytes:
    """
    Computes hash using the input data
    :param data: input datasss
    :return: hashed data in bytes
    """
    # context = ContextContainer._get_context()
    # if context.step_counter:
    #     step_count = 1
    #     if data:
    #         step_count += len(data)
    #     context.step_counter.apply_step(StepType.API_CALL, step_count)
    #
    return sha3_256(data).digest()


runtime(sha3_256, b'123')

# repeat = 10000
#
# for i in range(repeat):
#     recover_key(msg_hash, signature, False)
#
# for i in range(repeat)
#     create_address_with_key(public_key)
#
# for i in range(repeat):
#     sha3_256(data)