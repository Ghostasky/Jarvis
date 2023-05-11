import datetime
import json
from distutils.sysconfig import get_python_lib
 



path = r"" + get_python_lib() +"\Jarvis\\static\\role.json"
f = open(path,'r',encoding='utf-8')
# with open(path,'r',encoding="utf-8") as f:
roleAndPrompt = json.load(f)
f.close()

