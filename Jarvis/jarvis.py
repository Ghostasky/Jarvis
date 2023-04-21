# -*- coding: UTF-8 -*- 
import argparse
import art
import openai
import datetime
import os
import sys
from Jarvis.getKey import getKeyFromConfig
from distutils.sysconfig import get_python_lib
import getpass
# import Jarvis.role
import role
def sendMessage(messageLog):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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
        # 下面用来写其他命令，之后再说
        if '/' == line[0]:
            aaaa = line[0].split()
            return aaaa

        lines.append(a)
    print("[*]Has been sent.\n")
    return '\n'.join(lines)




openai.api_key = getKeyFromConfig()
# messages = [{"role": "system", "content": Jarvis.role.role_1}]
messages = [{"role": "system", "content": role.role_1}]
filePath= r"C:/Users/" + getpass.getuser()+"/Jarvis_log/"


def showInterface():
    Art=art.text2art("jarvis","rand")
    print(Art)
    print("Current Date: "+str(datetime.datetime.now())[0:10]+"."+"power by Ghostasky".rjust(100-len("Current Date: "+str(datetime.datetime.now())[0:10]+".")))
    print("="*100)
    pass


def mainLoop():
    try:
        while True:
            user_input = getInput()
            
            fileName = str(datetime.datetime.now())[0:10]+'.txt'
            pathAndFile = filePath+fileName
            writeLogInfo(pathAndFile,user_input,"Q")

            messages.append({"role": "user", "content": user_input})
            response = sendMessage(messages)

            writeLogInfo(pathAndFile,response,"A")

            print(f"\033[34mJarvis>\033[0m {response}\n")

    except (KeyboardInterrupt, EOFError) as e:
        print("\nBye Bye~")
        os._exit(0)

def writeLogInfo(filePath,Input, QorA):
    if QorA == "Q":
        with open(filePath,"a+",encoding="utf-8") as file:
            now_time = str(datetime.datetime.now())
            file.write(str(now_time)[:-7]+"| Q: "+Input+"\n")
            file.close()
        pass
    elif QorA  == "A":
        with open(filePath,"a+",encoding="utf-8") as file:
            now_time = str(datetime.datetime.now())
            file.writelines(str(now_time)[:-7]+"| A: "+Input+"\n")
            file.close()
        pass


def showHelpInfo():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l',"--list_all_role",help="list all role",action="store_true")
    args = parser.parse_args()
    if args.list_all_role:
        print("1. You are ChatGPT, a large language model....")
        print("2. bypass openai ")

def changerole():
    pass
def test(a):
    if a[0]=='/':
        print("change role")
    pass
def main():
    a = getInput()
    test(a)
    # showInterface()
    # showHelpInfo()
    # mainLoop()

if __name__ == '__main__':
    main()