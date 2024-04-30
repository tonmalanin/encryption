import argparse
import random
import string

from src import caesar, key_generator, lockpick, vernam, vigenere


def generate_random_key():
    length = random.randrange(1, 256)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class EncryptionTool:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Encryption tool')
        parser.add_argument('path', type=str, help='path to working file')
        parser.add_argument('mode', choices=['encrypt', 'decrypt', 'hack'], help='mode to use')
        parser.add_argument('algorithm', choices=['caesar', 'vigenere', 'vernam'], help='algorithm to use')
        parser.add_argument('-k', '--key', type=str, help='key for encryption')
        parser.add_argument('-r', '--random', type=int, help='generate random key of a given length')
        parser.add_argument('-o', '--output', type=str, help='path to output file')
        self.args = parser.parse_args()
        self.key = generate_random_key()
        self.path = self.args.path
        self.output = self.args.output
        self.encryptor = caesar.Caesar()

    def set_key(self):
        if self.args.key:
            self.key = self.args.key
        elif self.args.random:
            self.key = key_generator.generate_key(self.args.random)

    def set_encryptor(self):
        if self.args.algorithm == 'vigenere':
            self.encryptor = vigenere.Vigenere()
        elif self.args.algorithm == 'vernam':
            self.encryptor = vernam.Vernam()

    def work(self, text, output):
        if self.args.mode == 'encrypt' or self.args.mode == 'decrypt':
            print(f'Your key is: {self.key}')
            self.set_encryptor()
            if self.args.mode == 'encrypt':
                result_text = self.encryptor.encrypt(text, self.key)
            else:
                result_text = self.encryptor.decrypt(text, self.key)
            output.write(result_text)
        else:
            if self.args.algorithm == 'vigenere' or self.args.algorithm == 'vernam':
                print('The cipher cannot be cracked')
            else:
                hacker = lockpick.LockPick()
                result_text = hacker.hack(text)
                output.write(result_text)
