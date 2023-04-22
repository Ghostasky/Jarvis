# -*- coding: utf-8 -*-
from distutils.sysconfig import get_python_lib
import prettytable as pt
import json
# 本地
# from allData import alldata
# from role import roleAndPrompt


# 发布
from Jarvis.allData import alldata
from Jarvis.role import roleAndPrompt


def command(user_input):
    user_input_temp = user_input.split(" ")
    match user_input_temp[0]:
        case "/list" | "/?" | "/help":
            showAllCommand()
        case "/change_role"| "/cr":
            # temp = user_input.split(" ")[]
            if len(user_input_temp) != 2:
                print("缺参数")
            else:
                number = user_input_temp[1]
                changeRole(number)
        case "/list_role" | "/lr":
            showAllRole()
        case _:
            print("no this command, please input again.")

def showAllCommand():
    print('''Here are all command: 
    /list : show all command.
    /change_role : change the prompt
    /list_role : show all prompt''')
    pass

def changeRole(number):
    number = int(number)
    print(number,type(number))
    
    # alldata.changeRole(roleAndPrompt[number+1]["prompt"])
    alldata.messages = [{"role": "system", "content": roleAndPrompt[number-1]["prompt"]}]
    print("[*] already change: "+ roleAndPrompt[number-1]["act"])
    # print(alldata.messages)
    pass

def showAllRole():
    path = r"" + get_python_lib() +"\Jarvis\\static\\role.json"
    with open(path,'r',encoding="utf-8") as f:
        jsonstr = json.load(f)
    i = 1
    tb = pt.PrettyTable()
    tb.field_names = ["Number", "Act", "Prompt"]
    for eachRole in jsonstr:
        prompt = eachRole["prompt"].split('\n')[0]
        # print(i," ", eachRole["act"]+":"+prompt[:40]+"...")
        # print('{0:30} ==== {0:10}'.format(eachRole["act"],prompt[:40]) )
        # print(i,eachRole["act"].ljust(20,chr(12288))," === ",prompt[:50].rjust(30,chr(12288)),"...")
        tb.add_row([i,eachRole["act"], prompt[:33]+"..."])
        i+=1
    # tb.set_style(pt.RANDOM)
    tb.align = 'l'
    print(tb)

# showAllRole()


