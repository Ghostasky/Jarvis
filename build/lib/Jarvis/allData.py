# 本地
# import role

#发布
import Jarvis.role as role
class allData():
    def __init__(self) :
        self.global_role =role.roleAndPrompt[0]["prompt"]
        self.messages = [{"role": "system", "content": self.global_role}]
        pass


    def changeRole(self,newrole):
        self.global_role = newrole


alldata = allData()

