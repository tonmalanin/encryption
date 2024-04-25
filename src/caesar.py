import cipher


class Caesar(cipher.Cipher):
    def encrypt(self, text, key):
        shift = ord(key[0]) - 33
        result_text = ""
        for char in text:
            if char.isspace():
                result_text += char
            else:
                result_text += chr(33 + (ord(char) - 33 + shift) % 94)
        return result_text

    def decrypt(self, text, key):
        shift = ord(key[0]) - 33
        result_text = ""
        for char in text:
            if char.isspace():
                result_text += char
            else:
                result_text += chr(33 + (ord(char) - 33 - shift) % 94)
        return result_text
