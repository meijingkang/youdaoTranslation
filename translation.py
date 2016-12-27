import urllib.request
import urllib
import json
import re
from typing import re


class Translator(object):
    def translate(self ,word):
        #解决中文请求参数问题
        result = ""
        word = urllib.parse.quote(word)
        path = "http://fanyi.youdao.com/openapi.do?keyfrom=woshimeijunkangaaa&key=801746524&type=data&doctype=json&version=1.1&q="+word
        f = urllib.request.urlopen(path)
        s = f.read().decode('utf-8')
        for shortS in s.split(","):
            if shortS.__contains__("trans"):
                #找到翻译的key-value
                replace = shortS.replace("{", "").replace('"', "").replace("[", "").replace("]", "")
                result = result +replace+"\n"
            if shortS.__contains__("explains"):
                replace = shortS.replace("{", "").replace('"', "").replace("[", "").replace("]", "").replace("}", "")
                result = result + replace
                return result
trans = Translator()
iscontinue = True
while iscontinue :
    word = input("input word:")
    if word =="exit":
        iscontinue = False
        break
    if word =="-help":
        print("input exit to exit\n input -help to help")
    result = trans.translate(word)
    print(result)

