from src import cipher


class Vernam(cipher.Cipher):
    def encrypt(self, text, key):
        it = 0
        result_text = ''
        for char in text:
            if char.isspace():
                result_text += char
            else:
                shift = ord(key[it]) - 33
                result_text += chr(33 + ((ord(char) - 33) ^ shift) % 94)
                it = (it + 1) % len(key)
        return result_text

    def decrypt(self, text, key):
        return Vernam.encrypt(self, text, key)
