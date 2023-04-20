# -*- coding: UTF-8 -*- 
import sys
import os 
# print(os.getcwd())
from distutils.sysconfig import get_python_lib
 


# 判断当前执行程序的目录下有没有config文件，
# 如果没有，创建文件，输入api token
# 如果有：
    # 判断有没有apitoken
        # 有：读token
        # 没有：输入api toke



def getOpenAIAPI():
    getAPI= input("please input openai key:")
    return getAPI

def getFilePath():
    a =os.path.dirname(os.path.realpath(sys.executable))
    
    if hasattr(sys, '_MEIPASS'):
        a+="\\config.txt"
        # print(a)
        return a
    else:
        appPath, filename = os.path.split(os.path.abspath( __file__))
        # print(appPath+"\\"+filename)
        filePath = appPath+"\\config.txt"
        return filePath

def getKeyFromConfig():
    # configFile = getFilePath()
    # configFile = "./config.txt"
    # print(os.getcwd())
    # print(sys.executable)
    # print(sys.argv[0])
    # print(configFile)
    configFile = r""+get_python_lib() +"\Jarvis\config.txt"
    # configFile = sys.argv[0]+"\..\site-packages\Jarvis\config.txt"
    # print(configFile)
# 
    # print(configFile,"这里")
    if os.path.exists(configFile):
        # print("true")
        fp = open(configFile,'r',encoding='utf-8')

        apiKey =fp.readline()

        # print(apiKey)
        while len(apiKey)!=51:
            print("api key error",apiKey)
            apiKey = getOpenAIAPI()
            if len(apiKey)==51:
              
                fp.write(apiKey)
        fp.close()
        
        return apiKey
    else:
        # print("false")
        fp = open(configFile,'w')
        apiKey = getOpenAIAPI()
        fp.write(apiKey)
        fp.close()
        return apiKey
# configFile = sys.path[0]+"\\config.txt"
# print( os.path.getsize(configFile))

# getKeyFromConfig()