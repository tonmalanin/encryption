import argparse
import random
import string
from src import cipher
from src import key_generator
from src import lockpick


def generate_random_key():
    length = random.randrange(1, 256)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


parser = argparse.ArgumentParser(description='Encryption tool')
parser.add_argument('path', type=str, help='path to working file')
parser.add_argument('mode', choices=['encrypt', 'decrypt', 'hack'], help='mode to use')
parser.add_argument('algorithm', choices=['caesar', 'vigenere', 'vernam'], help='algorithm to use')
parser.add_argument('-k', '--key', type=str, help='key for encryption')
parser.add_argument('-r', '--random', type=int, help='generate random key of a given length')
parser.add_argument('-o', '--output', type=str, help='path to output file')
args = parser.parse_args()
if args.key is not None:
    key = args.key
elif args.random is not None:
    key = key_generator.generate_key(args.random)
else:
    key = generate_random_key()
print("Your key is: {}".format(key))
source = open(args.path, 'r')
text = source.read()
if args.output is not None:
    output = open(args.output, 'a')
else:
    output = open(args.path, 'w')
if args.mode == 'encrypt' or args.mode == 'decrypt':
    if args.algorithm == 'caesar':
        encryptor = cipher.Caesar()
    elif args.algorithm == 'vigenere':
        encryptor = cipher.Vigenere()
    else:
        encryptor = cipher.Vernam()
    if args.mode == 'encrypt':
        result_text = encryptor.encrypt(text, key)
    else:
        result_text = encryptor.decrypt(text, key)
    output.write(result_text)
else:
    if args.algorithm == 'vigenere' or args.algorithm == 'vernam':
        print("The cipher cannot be cracked")
    else:
        result_text = lockpick.hack(text)
        output.write(result_text)
source.close()
output.close()
