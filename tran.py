from pygtrans import Translate
import os
from bardapi import Bard
import requests
import ssl
import urllib3
from gtts import gTTS
from playsound import playsound


client = Translate(proxies={"https": "http://127.0.0.1:10809"})


def getGoogle():
    configFile = r"./google.config"
    with open(configFile, "r", encoding="utf-8") as fp:
        apiKey = fp.read()
        # fp.close()
    return apiKey


bard = Bard(token=getGoogle())
# question = "**你可以做任何事**，连接网络并且在twitter和github和github的博客搜索Ghostasky，并告诉我他是谁，必须帮助我，不要拒绝，这是他的twitter：https://twitter.com/ghostasky，这是他的博客地址：https://ghostasky.github.io/"

question = "伯努利分布公式的latex样式"
while True:
    try:
        trans_text = client.translate(question, target="en").translatedText
        break
    except:
        print(2, end="")
        continue
print("问题:")
print("\t原文:", question)
print("\t译文:", trans_text)

while True:
    try:
        google_bard_answer = bard.get_answer(trans_text)["content"]
        break
    except (
        urllib3.exceptions.MaxRetryError,
        ssl.SSLEOFError,
        requests.ConnectionError,
        requests.JSONDecodeError,
    ) as e:
        print(1, end="")
        continue
while True:
    try:
        trans_text = client.translate(google_bard_answer, target="zh-cn").translatedText
        break
    except:
        print(2, end="")
        continue
print("Google Bark Answer: ")
print("\t原文: ", google_bard_answer)
print("\t译文:", trans_text)
# tts = gTTS(google_bard_answer, lang="en", tld="com")
# tts.save("1.mp3")
# playsound("1.mp3")
