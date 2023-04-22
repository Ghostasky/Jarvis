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
# from allData import alldata


# 发布版
from Jarvis.getKey import getKeyFromConfig
from Jarvis.log import writeLogInfo
from Jarvis.command_ import alldata
from Jarvis.command_ import command
# from Jarvis.allData import alldata


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
        # if '/' == line[0]:
        #     aaaa = line[0].split()
        #     return aaaa

        lines.append(a)
    print("[*]Has been sent.\n")
    return '\n'.join(lines)




openai.api_key = getKeyFromConfig()
# # messages = [{"role": "system", "content": Jarvis.role.role_1}]
# messages = [{"role": "system", "content": global_role}]
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
            # user_input = input("\033[32m>\033[0m ")
            # user_input = 
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
                response = sendMessage(alldata.messages)

                writeLogInfo(pathAndFile,response,"A")
                print(f"\033[34mJarvis>\033[0m {response}\n")

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





    # match user_input[]
    pass
# def test(a):
#     if a[0]=='/':
#         match a[1:]:
#             case "changerole":
#                 global_role = role.role[2]
#             case "list":
#                 global_role = role.role[1]
#             case _:
#                 global_role = "normal" # normal
        # while global_role == "no this role":
        #     print(global_role+", re inpuut")
        #     match a[1:]:
        #         case "aaab":
        #             global_role = role.role_2
        #         case "bbbc":
        #             global_role = role.role_1
        #         case _:
        #             global_role = "no this role"
        #         # pass
        # print(global_role)
    pass
def main():
    # a = getInput()
    # test(a)
    showInterface()
    showHelpInfo()
    mainLoop()
    # print(alldata.global_role)
    # alldata.changeRole("hello")
    # print(alldata.global_role)
    

if __name__ == '__main__':
    main()