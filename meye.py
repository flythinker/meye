
import time
class MonitorItem:
    def doMonitor(self,meye):
        pass

class MEye:
    def __init__(self):
        print("MEye initing")
        #检测操作系统版本等
        self.mItemArr = []

    def setStatusData(self,itemName,val): #设置状态数据
        pass

    def getOldStatusData(self,itemName): #得到上一次的状态数据
        pass

    def email(self,body): # 发送电子邮件
        pass



    def startMonitor(self):
        pass

    def addItem(self,mItem):
        self.mItemArr.append(mItem)



