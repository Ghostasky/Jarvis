# -*- coding: UTF-8 -*- 
import sys
import os 
from distutils.sysconfig import get_python_lib
import getpass 


# 判断当前执行程序的目录下有没有config文件，
# 如果没有，创建文件，输入api token
# 如果有：
    # 判断有没有apitoken
        # 有：读token
        # 没有：输入api toke



def getOpenAIAPI():
    getAPI= input("please input openai key:")
    return getAPI


def getKeyFromConfig():
    # configFile = getFilePath()
    # configFile = r""+get_python_lib() +"\\Jarvis\\static\\config.txt"
    configFile= r"C:/Users/" + getpass.getuser()+"/Jarvis_log/"+"config.txt"
    if os.path.exists(configFile):
        # print("true")
        # fp = open(configFile,encoding='utf-8')
        with open(configFile,'r',encoding='utf-8') as fp:
            apiKey =fp.read()
            # print(apiKey)
        # print(apiKey)
        while len(apiKey)!=51:
            print("api key error",apiKey)
            apiKey = getOpenAIAPI()
            with open(configFile,'w',encoding='utf-8') as fp:
                fp.write(apiKey)
        # fp.close()
        
        return apiKey
    else:
        # 文件不存在，创建文件然后写入
        fp = open(configFile,'w+')
        apiKey = getOpenAIAPI()
        fp.writelines(apiKey)
        # print(apiKey)
        fp.close()
        return apiKey
getKeyFromConfig()