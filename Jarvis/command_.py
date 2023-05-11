# -*- coding: utf-8 -*-
from distutils.sysconfig import get_python_lib
import prettytable as pt
import json
import requests
import getpass 
import datetime
# 本地
# from allData import alldata
# from role import roleAndPrompt


# 发布
from Jarvis.allData import alldata
from Jarvis.role import roleAndPrompt


LIMIT_URL = "https://api.openai.com/dashboard/billing/subscription"
USAGE_URL = "https://api.openai.com/dashboard/billing/usage"

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
        case "/hisuse" | "/hu":
            showHistoryUseage();
            pass
        case _:
            print("no this command, please input again.")

def showAllCommand():
    print('''Here are all command: 
    /list : show all command.
    /change_role : change the prompt
    /list_role : show all prompt
    /hisuse : show history usage
    ''')
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

def showHistoryUseage():
    apiFile =r"C:/Users/" + getpass.getuser()+"/Jarvis_log/"+"config.txt"
    # print(apiFile)
    with open(apiFile,'r',encoding="utf-8") as f:
        key =f.read()
        # print(key)
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=90)
    data = make_request(
        key, USAGE_URL, params=[start_date.isoformat(), end_date.isoformat()]
    )
    limit = make_request(key, LIMIT_URL)
    hard_limit = float(limit["hard_limit_usd"])

    timestamps = [item["timestamp"] for item in data["daily_costs"]]
    line_items = [item["line_items"] for item in data["daily_costs"]]
    now = datetime.datetime.now()
    month = now.strftime("%m")
    total = 0
    result = []
    for cost in data['daily_costs']:
        timestamp = cost['timestamp']
        date = datetime.datetime.fromtimestamp(timestamp)
        if date.month == int(month):
            result.append(cost)
    
    for i in result:
        usage = 0
        lineitem_ = i['line_items']
        for j in lineitem_:
            usage += j['cost']
        total+=usage
        print("日期：", str(datetime.datetime.fromtimestamp(i['timestamp']))[:10], " 使用量(美分)：", usage)

    # for i in range(len(line_items)):
    #     usage = 0
    #     dt_object = datetime.datetime.fromtimestamp(timestamps[i])
    #     for j in range(len(line_items[i])):
    #         usage += line_items[i][j]["cost"]
    #     total += usage
    #     print("日期：", str(dt_object)[:10], " 使用量(美分)：", usage,dt_object.month)
    dollar = total / 100
    print(f"本月总使用量：${dollar:.4f}")
    pass


def make_request(api_key, url, params=None):
    """发出API请求并返回结果"""
    headers = {"Authorization": f"Bearer {api_key}"}

    if url == USAGE_URL:
        # 如果请求的是USAGE_URL，则需要包含起始时间和结束时间
        start_date, end_date = params
        params = {"start_date": start_date, "end_date": end_date}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"请求出错: {response.content.decode('utf-8')}")
        exit(1)

    return json.loads(response.content.decode("utf-8"))

# showHistoryUseage()