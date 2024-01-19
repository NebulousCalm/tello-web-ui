import random
import string


def gen_key(val):
    return ''.join(random.choice(string.ascii_letters) for character in range(val))
