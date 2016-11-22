# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
时间：2016年10月17日16:52:01
功能：SSH2连接IPC
@author: yezhibin
版本：V1.0.0
'''
import SSHLibrary
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
from matplotlib.dates import AutoDateLocator, DateFormatter


class TestDemo:
    def __init__(self):
        pass

    def ssh_ex_cmd(self, ip, port, username, password, cmd_list, timeout=3):
        """
            功能：登录设备，连续重启三次，计算平均重启耗时，并返回该值\n
            参数：\n
                ip : 设备的IP地址\n
                port : 设备端口号\n
                username : 设备的用户名，支持中文\n
                password : 设备的密码，支持中文\n
                cmd_list : ssh命令列表\n
                timeout : 截止标志"#"（未出现时）延时等待时间，默认3s\n
            返回值：\n
            无\n
            """
        try:
            demo = SSHLibrary.SSHLibrary()
            demo.open_connection(host=ip, port=port)
            demo.set_client_configuration(timeout=timeout, prompt="#")
            demo.login(username, password)
            for item in cmd_list:
                demo.write(item)
                return_info = demo.read_until_prompt()
                print return_info
            print '%s\tOK\n' %(ip)
            demo.close_connection()

        except Exception,ex:
            print '%s\tError\n' %(ip)
            print Exception,":",ex

    def loadData(self,fileName):
        x = []
        y = []

        with open(fileName) as f:
            for line in f:
                trainingSet = line.split('    ')
                x_t = datetime.datetime.strptime(trainingSet[0],'%Y-%m-%d %H:%M:%S')
                x.append(x_t)
#                print x
                y.append(trainingSet[1])
        f.close()
        return (x,y)
        
    def plotData(self,x,y):
        length = len(y)
        plt.figure(figsize=(9,5),dpi=72,facecolor="white")
        axes = plt.subplot(111)
        axes.cla()  #清空坐标轴内的所有内容
        
#        font = {'family'    :   'serif',
#                'color'     :   'darkred',
#                'weight'    :   'normal',
#                'size'      :   10,
#               }

        plt.plot(x,y,)
        plt.xlabel('time')
        plt.ylabel('mem')
        plt.ylim([0,100])
        plt.title('cpu curve')
       
        plt.show()
        
#    #动态绘图程序
#    def dynamic_draw(self)
    


if __name__=='__main__':
    host = '10.10.34.237'
    port = 22
    username = 'admin'
    password = 'abcd1234'
    cmd_list = ["ifconfig", "free"]
    TestDemo().ssh_ex_cmd(host, port, username, password, cmd_list, 10)
#    (x,y) = TestDemo().loadData('C:\Users\guojinhe\Desktop\statics\cpu.txt')
#    TestDemo().plotData(x,y)
