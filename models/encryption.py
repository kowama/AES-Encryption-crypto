# -*- coding: utf-8 -*-

# !/usr/bin/python


import base64

from Crypto.Cipher import AES

BS = 16


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()


def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


def iv():
    """
    The initialization vector to use for encryption or decryption.
    It is ignored for MODE_ECB and MODE_CTR.
    """
    return chr(0) * 16


class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """

    @staticmethod
    def encrypt(message: str, key: str, key_size: int = 255):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    @staticmethod
    def decrypt(enc: str, key: str, key_size: int = 256):
        enc = base64.b64decode(enc)
        cipher = AES.new(key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


# c =lDRwTGua0oY4kTJ8SSyYIg==
# k = asdrfgtyuiolpkjg
if __name__ == '__main__':
    #   k = '`?.F(fHbN6XK|j!t'
    m = input('give a cipher text : ')
    k = '1'
    while len(k) % 16 != 0:
        k = input('give a key [16] :  ')

    # k
    print(len(k))

    c = AESCipher.encrypt(m, k)
    print(c)
