import logging
import time
import yaml
import os,sys

class MonitorItem:
    def doMonitor(self,meye):
        pass

class MEye:
    def __init__(self):
        print("MEye initing")
        #检测操作系统版本等
        self.mItemArr = []
        yamlPath = "meye_default.yml"
        if os.path.exists("meye.yml"):
            yamlPath = meye.yml
        f = open(yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        self.config = yaml.load(cont)
        if 'interval' not in self.config:
            self.config['interval'] = 60
        self._interval = self.config['interval']
        if self._interval < 1:
            self._interval = 1
        #print(self.config)

    def setStatusData(self,itemName,val): #设置状态数据
        pass

    def getOldStatusData(self,itemName): #得到上一次的状态数据
        pass

    def email(self,body): # 发送电子邮件
        pass

    def addItem(self,mItem):
        self.mItemArr.append(mItem)

    def doInterval(self,cur_sec):
        print("doInterval ... %s" % cur_sec)
        count = len(self.mItemArr)
        if count == 0 :
            print("监控项为空(error_101)")
            return
        else:
            for monItem in self.mItemArr:
                monItem.doMonitor(self)

    def startMonitor(self):
        #init
        # 整除self._interval,取整
        last_sec = int(time.time())
        last_sec = int(int(last_sec / self._interval) * self._interval)

        while True:
            now = time.time()
            cur_sec = int(now)
            if cur_sec - last_sec >= self._interval :
                last_sec = int(int(cur_sec / self._interval) * self._interval)
                self.doInterval(last_sec)
            time.sleep(1)

if __name__ == "__main__":
    #dev run
    class DevMonItem(MonitorItem):
        def doMonitor(self, meye):
            print("DevMonItem ...")

    devMonItem = DevMonItem()
    meye = MEye()
    meye.addItem(devMonItem)
    meye.startMonitor()

