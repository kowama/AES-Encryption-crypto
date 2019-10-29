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
      It is assumed that you use Python 3.0+
      , so plaintext's type must be str type(== unicode).
      """

    @staticmethod
    def encrypt(message: str, key: str) -> str:
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    @staticmethod
    def decrypt(enc: str, key: str) -> str:
        enc = base64.b64decode(enc)
        cipher = AES.new(key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


if __name__ == '__main__':
    m = input('give a cipher text : ')
    k = ''
    while len(k) != 24:
        k = input('give a key [24] :  ')
        print(len(k))

    # k
    c = AESCipher.encrypt(m, k)
    print(c)
