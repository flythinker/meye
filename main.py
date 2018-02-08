#!/usr/bin/env python
# coding=utf-8

import os, sys
import time
from collections import OrderedDict
import datetime
import smtplib
from email.mime.text import MIMEText
import logging

logger = logging.getLogger('server-run-log')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


def send_mail(context):
    sender = "send@163.com"  
    receiver = ['receive@163.com']
    host = 'smtp.163.com'
    port = 465
    msg = MIMEText(context)
    msg['Form'] = 'send@163.com'
    msg['To'] = 'receive@163.com'
    msg['Subject'] = 'system error & warning'

    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender, 'yoursendmailpasswd')
        smtp.sendmail(sender, receiver, msg.as_string())
        logger.info('send email success')
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    while True:
        time.sleep(3)
        try:
            #ret = os.popen('ps -ef|grep -v grep|grep redis').readlines()
            ret = os.popen('ps -ef|grep -v grep|grep tomcat').readlines()
            if len(ret) < 1:
                print('tomcat 进程异常退出， 5秒后重新启动')
                logger.info('tomcat 进程异常退出， 5秒后重新启动')
                send_mail('tomcat服务进程异常 准备重新启动')

                time.sleep(5)
		#os.system("/etc/init.d/redis_6379 restart")
                os.system("/usr/local/tomcat/bin/shutdown.sh ")
                os.system("/usr/local/tomcat/bin/startup.sh ")
                logger.info('tomcat 重新启动')
                send_mail('tomcat 已执行 重新启动')
        except:
            print("Error", sys.exc_info()[1])
            logger.info('Error occured!')
