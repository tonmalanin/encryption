import random
import string


def generate_key(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
