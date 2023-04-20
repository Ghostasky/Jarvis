# -*- coding: UTF-8 -*- 
import argparse
import art
import openai
import datetime
import os
import sys
# from getKey import getKeyFromConfig
from Jarvis.getKey import getKeyFromConfig
from distutils.sysconfig import get_python_lib
import getpass

def sendMessage(messageLog):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model= "gpt-4",
        messages=messageLog,  
        stop=None,            
        temperature=0.7,        
    )
    return response.choices[0].message.content
    pass
def getInput():
    print("")
    line =input("\033[32m>\033[0m ")
    lines = []
    lines.append(line)
    while True:
        a = input()
        if not a:
            break
        # 下面用来写其他命令，之后再说
        if '/' == line[0]:
            return line

        lines.append(a)
    print("[*]Has been sent.\n")
    return '\n'.join(lines)
    pass




openai.api_key = getKeyFromConfig()
messageContent = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: "+str(datetime.datetime.now())[0:10]+" Current date: "+str(datetime.datetime.now())[0:10]
messages = [{"role": "system", "content": messageContent}]

filePath= r"C:/Users/" + getpass.getuser()+"/Jarvis_log/"


def main():
    Art=art.text2art("jarvis","rand")
    print(Art)
    print("Current Date: "+str(datetime.datetime.now())[0:10]+"."+"power by Ghostasky".rjust(100-len("Current Date: "+str(datetime.datetime.now())[0:10]+".")))
    print("="*100)
    try:
        while True:
            user_input = getInput()
            fileName = str(datetime.datetime.now())[0:10]+'.txt'
            pathAndFile = filePath+fileName
            print(pathAndFile)

            with open(pathAndFile,"a+",encoding="utf-8") as file:
                now_time = str(datetime.datetime.now())
                file.write(str(now_time)[:-7]+"| Q: "+user_input+"\n")
                pass
            messages.append({"role": "user", "content": user_input})
            response = sendMessage(messages)
            with open(pathAndFile,"a+",encoding="utf-8") as file:
                now_time = str(datetime.datetime.now())
                file.writelines(str(now_time)[:-7]+"| A: "+response+"\n")
                pass    
            print(f"\033[34mJarvis>\033[0m {response}\n")
            # \033[31mException: {}\033[0m"
    except (KeyboardInterrupt, EOFError) as e:
        print("\nBye Bye~")
        os._exit(0)



if __name__ == '__main__':
    main()