# -*- coding: UTF-8 -*- 
import argparse
import art
import openai
import datetime
import os
import sys

from distutils.sysconfig import get_python_lib
import getpass



# 本地
# from log import writeLogInfo
# from command_ import command
# from getKey import getKeyFromConfig
# from allData import alldata

# 发布版
from Jarvis.getKey import getKeyFromConfig
from Jarvis.log import writeLogInfo
from Jarvis.command_ import alldata
from Jarvis.command_ import command
from Jarvis.allData import alldata


def sendMessage(messageLog,stream,modle="gpt-3.5-turbo"):
    if stream== True:
        response = openai.ChatCompletion.create(
            model=modle,
            # model= "gpt-4",
            messages=messageLog,  
            stop=None, 
            temperature=0.7,
            stream=True,     
        )
        return response
    else:
        response = openai.ChatCompletion.create(
        model=modle,
        # model= "gpt-4",
        messages=messageLog,  
        stop=None, 
        temperature=0.7,
        )
        return response.choices[0].message.content

def getInput():
    print("")
    line =input("\033[32m>\033[0m ")
    lines = []
    lines.append(line)
    while True:
        a = input()
        if not a:
            break

        lines.append(a)
    print("[*]Has been sent.\n")
    return '\n'.join(lines)




openai.api_key = getKeyFromConfig()
filePath= r"C:/Users/" + getpass.getuser()+"/Jarvis_log/"


def showInterface():
    Art=art.text2art("jarvis","rand")
    print(Art)
    print("Current Date: "+str(datetime.datetime.now())[0:10]+"."+"power by Ghostasky".rjust(100-len("Current Date: "+str(datetime.datetime.now())[0:10]+".")))
    print("v0.7")
    print("="*100)
    pass


def mainLoop():
    try:
        while True:
            user_input = getInput()
            if user_input[0] =='/':
                command(user_input)
            else:
                fileName = str(datetime.datetime.now())[0:10]+'.txt'
                pathAndFile = filePath+fileName
                writeLogInfo(pathAndFile,user_input,"Q")
                # print(alldata.messag/es)
                # messages = 
                alldata.messages.append({"role": "user", "content": user_input})
                # print(alldata.messages)
                response = sendMessage(alldata.messages,False)

                writeLogInfo(pathAndFile,response,"A")
                print(f"\033[34mJarvis>\033[0m {response}\n")
                print(alldata.messages)

    except (KeyboardInterrupt, EOFError) as e:
        print("\nBye Bye~")
        os._exit(0)


def streammainloop():
    try:
        while True:
            user_input = getInput()
            if user_input[0] =='/':
                command(user_input)
            else:
                fileName = str(datetime.datetime.now())[0:10]+'.txt'
                pathAndFile = filePath+fileName
                writeLogInfo(pathAndFile,user_input,"Q")
                alldata.messages[1] = {"role": "user", "content": user_input}
                response = sendMessage(alldata.messages,True)
                completion = {"role": "assistant", "content": ""}
                print(f"\033[34mJarvis>\033[0m ",end="")
                for event in response:
                    if event["choices"][0]["finish_reason"] == "stop":
                        writeLogInfo(pathAndFile,completion['content'],"A")
                        break
                    for delta_k, delta_v in event["choices"][0]["delta"].items():
                        if delta_v == "assistant":
                            continue
                        print(f"{delta_v}", end="",flush=True)
                        completion[delta_k] += delta_v
                
    except (KeyboardInterrupt, EOFError) as e:
        print("\nBye Bye~")
        os._exit(0)




def showHelpInfo():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l',"--list_all_role",help="list all role",action="store_true")
    args = parser.parse_args()
    if args.list_all_role:
        print("1. You are ChatGPT, a large language model....")
        print("2. bypass openai ")

def main():
    # a = getInput()
    # test(a)
    showInterface()
    showHelpInfo()
    # mainLoop()
    streammainloop()

if __name__ == '__main__':
    main()