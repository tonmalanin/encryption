import argparse
from src import cipher
from src import key_generator
from src import lockpick


def generate_random_key():
    return 'key'


parser = argparse.ArgumentParser(description='Encryption tool')
parser.add_argument('mode', choices=['encrypt', 'decrypt', 'hack'], help='mode to use')
parser.add_argument('path', type=str, help='path to working file')
parser.add_argument('algorithm', choices=['caesar', 'vigenere', 'vernam'], help='algorithm to use')
parser.add_argument('-k', '--key', type=str, default=generate_random_key(), help='key for encryption')
parser.add_argument('-r', '--random', type=int, help='generate random key of a given length')
parser.add_argument('-o', '--output', type=str, help='path to output file')
args = parser.parse_args()
