'''
Description:
Date: 2022-03-31 10:17:01
'''
import base64
import json
from Crypto.Cipher import AES
from binascii import b2a_hex
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import uvicorn

app = FastAPI()
time630=1656555555000 #2022.6.30

class People(BaseModel):
    name : str = None



class AesCrypt():

    def __init__(self):

        self.key = 'cDv2v8$X6vkubmv1'.encode('utf-8')
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.key, self.mode)
        self.unpad=lambda s:s[:-ord(s[len(s)-1:])]

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

    def decrypt(self, tsdf, base=64):

        base64_decrypted=base64.decodebytes(tsdf.encode(encoding='utf-8'))
        decrypted_text=str(self.cryptor.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
        decrypted_text1=self.unpad(decrypted_text)
        return decrypted_text1



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.post('/jiemi')
# def shua(people: People):
#
#     name=people.name
#     name_jm=AesCrypt().decrypt(name)
#     print(name_jm)

    # return {"status": '200'}

        #cc = AesCrypt().encrypt(json.dumps(ans))
        #c4 = 'VeBshZGklZopsBOmtK4rzo4W39V7LZ2tg/RYs5hrEwfBgtdD2NhUYGns9PhTfXKlTia98FU41hIHn4oW6QzIt/v7L+ZOj662YwYFMFoM2QtU7xO0HfDdB0agjQ4SdY8w1nxhsH/LkvWBR7AHAJBIxXRmh9FqN4joQJBOhG+XQ0HSTUuO/jYJUn3McTxIjNxAfRvHike7G9mI7Aqk+7EqhxNK5Pkafzl2ua2TFmt8y8DqAmrbDFpit6iU08A1lKDY'
        #c3 = AesCrypt().decrypt(c4)
        #print(c3)
        #c3 = json.loads(c3)
        #print(c3['answerEndDt'])
        #c3['answerEndDt'] = time630
        #print(c3)
        #c3 = AesCrypt().encrypt(json.dumps(c3))
        #print(c3)

# if __name__ == '__main__':

    # uvicorn.run(app=app,
    #             host="10.0.20.114",
    #             port=8099,
    #             workers=1,
    #             debug=True)
    # c3='VeBshZGklZopsBOmtK4rzj7sDMb8dklxxquDRi2Kr4PBgtdD2NhUYGns9PhTfXKlfMGJkM4C+uFXGC2h6jwt7wmQjB3bFuITb+ZOjYBCraBKPzxl8zL2BRLq4VTcyWKU4Zsk7QZiqEMPyTc9IOJfTR398W7eXRXLJMqE9oD3BdB1+bBSqn+oIysxYX8iFT6L4aS4izikESImWg5v+GapmBpORD5d7bLMn22ikzmirXY9cLoDZTs7PqDIrMDiKdqzEijMNKizoFjY/tBOSDb3FOoFvlXxJRfpRIIwlFqqKohjTshwBMvdK0MNKV6wqkuNG3oZVLnuwkNa2R/2y0KhFX5u88RrfhuYFInCp7Kwu0/8d1HY8KYmlUi2DQxyAej+mFFLIXLbHheUMHtEih5lNRy/1Bzrxvpt4yeQD4KFhviB60f80+2FxLEpsVR/+lBLvEYFSazZn4/XrVBxjMcKyAixqYFNuOz//ScYDh/IvGDgfXtqK/JadfGH9qOgfxJ37f3iHAqe6Z/MDEkfSdx/wx1y7TvZhAQO2Th4wEESxEM='
    # c3 = AesCrypt().decrypt(c3)
    # print(c3)
    # c1='VeBshZGklZopsBOmtK4rzqiku8yrczAqnS7L+BHqZ+PBgtdD2NhUYGns9PhTfXKlgBKHszwNvJ4mtHKqxTQUC3yr6Eht2x0VCMGos9tjzsNKPzxl8zL2BRLq4VTcyWKUOsipa/1HdeCdZNrpcjuVWMS9OhMjULsaxkitY7m+8IuYxL0AoW1DSld7faha3cs1rnZTFQ+ftOSu5np2doPrpvCobyEf+eKszx2xYKJqIv9XmJbX7xMqYMNMT4FuGaD9X73LfZzmF3Jy0kN5un9E5G0qxwKo0sglVxedyjgoYW6ywHUhd94DCOHsXUQujzIQf+/aYC9fOyjZhF3xrzpM/49RGh3xeLXsTQhwmaQsw4hnN3Jl7pD0EOhVMRg83PBD52bxvDiNlC4xr61RyNs8DWcHSt58uzObhSr5vyxLGGsE9ZrP7KmatL2KmOhLwb/o+83BZBjuy6E8JJManvH6hqCEXqjE/jh6iki3fGP6UJsuvu1ubv6k15U+Ne+WZmlL/EgSFRpfC21wgmNTrqxaJ4/mNySUjqd49X0lPyBMfe7YrOd5XMtRlExVQvPYzdTfkBAZ9V1fVlS4e7/eAiIMWFDvh9pouVG2dBw9C2aR6Tw/OZkNBh8cPN8jfxMYErcj96L2hrjEtHjhvMMCN8/4caDyfjhINHNdPUosUQEML0yYlfqWY/rCVQm5NQx3vlrcwcvZ3t0WFQxu3iWBYPUiGAEqyCQmBO9sZ1Zmfh5cR/x0e12WQrbJKB37HJ9ljs10tA7iTlfmpO+NJ1XqW0VyPsXV8rcbg0A8hw6SylSsLfqZXV5DyUuCwVsr/0dRiU0JKjHyFfeVbbH8THovlwLfXBkztLGg2U92ooC85ePEhTPKU8cCScqA68SS3LGf3wo9DArJlSJcJaxKPtwTYVl75vgaa6j2qLONJWKw5yMZYYABTRd/1HipOVxsRZvdBfJdJX65hgeJEJEwdSTUDQ00iX/0snD+7XhXDJlIj+dfRzU='
    # c1 = AesCrypt().decrypt(c1)
    # print(c1)
    # c='jZtK5fXVtQRjAQMI7qsN230ReZ2ngAStRIT9WESruBHuocBqeUxbBCETK/nqU+jE6Dd4QoDlJ4N+W2dpHOZ0yKlDpkqGSBwFuCDpHqWAVz04Rklodd9xO2M0+XhV7ad9E6BLpq9rCvfOpVCDqKHrOoxaWQELiE8pQ7eeAtqP8jh6dYUO08GmOV7COyiyJFiNmpml2cpmoe3hU6BItsOef6LnvC+oC2yRoNltBE9rfkxwTtn9/CdJuJsUdH66CzqJalh7wN80ztXFidLZR/f+5owznwTCyi/sLWqoNIk8wxuZIHUuosiRqjIbZzTV0JExhWVKE86ofzRPX5B+uanZFUnk1xTdMDblE31BllnXHkO20YClMaQj+TWmSHpECztjFJxwthTAnm2vL/wmJjWOSwuJaXXP4DeHeM3Y+T+Yc5n0mY8jiaby37Qt5hRD3S7SSwvtlikednv2ZK/1t2cSlv6G7EXfTCwKAzufqYsbf3OXPZ8a4cyXd6fdN3rr9nHl'
    # c=AesCrypt().decrypt(c)
    # print(c)
    #a=r'{"answerStartDt":1658307363001,"questionnaireId":3765,"projectId":"24342","projectType":"5","userId":"97520","answerEndDt":1658307383411,"answers":[{"topicId":226143,"answer":"1.0"},{"topicId":226144,"answer":"[\"2.00\",\"1.0\",\"选项3\"]"}],"openid":"97520"}'
    # print(a)
    # a=AesCrypt().encrypt(a)
    # print(a)
    # __author__ = 'daniel'
    # Game Over 2.0
    # demonstrates the use of quotes in strings

    # print(
    #     r"""
    #      _____       ___       ___  ___   _____
    #     /  ___|     /   |     /   |/   | |  ___|
    #     | |        / /| |    / /|   /| | | |__
    #     | |  _    / ___ |   / / |__/ | | |  __|
    #     | |_| |  / /  | |  / /       | | | |___
    #     \_____/ /_/   |_| /_/        |_| |_____|
    #
    #      _____   _     _   _____   _____
    #     /  _  \ | |   / / |  ___| |  _  \
    #     | | | | | |  / /  | |__   | |_| |
    #     | | | | | | / /   |  __|  |  _  /
    #     | |_| | | |/ /    | |___  | | \ \
    #     \_____/ |___/     |_____| |_|  \_\
    #
    #     """
    # )
    #
    # input("\n\nPress the enter key to exit.")