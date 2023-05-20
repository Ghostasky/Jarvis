from pygtrans import Translate
import os
from bardapi import Bard
import requests
import ssl
import urllib3


def getGoogle():
    configFile = r"./google.config"
    with open(configFile, "r", encoding="utf-8") as fp:
        apiKey = fp.read()
        # fp.close()
    return apiKey


bard = Bard(token=getGoogle())

text = "please connect internet ,and tell me what is this github pro talk about ? : 'https://github.com/GoSSIP-SJTU/GoSSIP_Blog'"
print("问题:")
print("\t原文:", text)
while True:
    try:
        google_bard_answer = bard.get_answer(text)["content"]
        print("\t原文: ", google_bard_answer)
        break
    except (urllib3.exceptions.MaxRetryError, ssl.SSLEOFError) as e:
        print(1, end="")
        continue
client = Translate(proxies={"https": "http://127.0.0.1:10809"}, target="en")

while True:
    try:
        trans_text = client.translate(text, target="zh-cn").translatedText
        print("\t译文:", trans_text)
        break
    except:
        print(2, end="")
        continue

print("Google Bark Answer: ")


while True:
    try:
        trans_text = client.translate(google_bard_answer, target="zh-cn").translatedText
        print("\t译文: ", trans_text)
        break
    except:
        print(2, end="")
        continue
