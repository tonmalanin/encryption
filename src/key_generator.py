import string
import random


def generate_key(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
