import random
import string


def gen_key(val):
    return ''.join(random.choice(string.ascii_characters) for character in range(val))
