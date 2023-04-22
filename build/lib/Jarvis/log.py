import datetime


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
