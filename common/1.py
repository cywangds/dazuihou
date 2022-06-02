'''
Description:
Date: 2022-03-31 10:17:01
'''
import base64
import json
import random
import sys
import time
import requests
from Crypto.Cipher import AES
from binascii import b2a_hex
import xlwt

class AesCrypt():

    def __init__(self):
        self.key = 'cDv2v8$X6vkubmv1'.encode('utf-8')
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.key, self.mode)

    def add_to_16(self, text):
        pad = 16 - len(text.encode('utf-8')) % 16
        text = text + pad * chr(pad)
        return text.encode('utf-8')

    def encrypt(self, text, base=64):
        text = self.add_to_16(text)

        # 加密,输出bytes类型
        cipher_text = self.cryptor.encrypt(text)
        if base == 16:
            # 返回16进制密文
            return b2a_hex(cipher_text).decode('utf-8')
        elif base == 64:
            # 返回base64密文
            return base64.b64encode(cipher_text).decode('utf-8')

    def decrypt(self, str, base=64):
        #res_text = self.cryptor.decrypt(base64.b64decode(str)).decode('unicode-escape')
        res_text = self.cryptor.decrypt(base64.b64decode(str)).decode('utf-8')
        return res_text

    def decrypt1(self, str, base=64):
        res_text = self.cryptor.decrypt(base64.b64decode(str)).decode('utf-8')
        #return json.loads(res_text.replace('\x07', '').strip())
        return res_text.replace('\x07', '').strip()
ans={'1':'1'}


if __name__ == '__main__':
    c=AesCrypt().encrypt(json.dumps(ans))
    print(c)
    c=AesCrypt().decrypt(c)
    print(c)