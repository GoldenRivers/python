# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
功能:利用xlrd，将excel中某列数据中，含有指定字符串的记录取出，并生成用这个字符串命名的txt文件
author:gjh
date:2016/10/27
version:1.0.0
'''
import os
import xlrd,sys
import matplotlib.pyplot as plt
import numpy as np
import string

'''
功能:读取excel文件,返回指定字符串的位置并将结果写到以该字符串命名的TXT文件中
author:gjh
data:2016-10-31
version:1.0.0
'''
        
def read_excel(Filename):
    #open the excel file
    bk=xlrd.open_workbook(Filename)
    #get the sheets number
    shnum=bk.nsheets  #输出sheet的个数
    shxrange = range(bk.nsheets)  #生成sheet的索引列表
    #get the sheets name
    for x in shxrange:
        p=bk.sheets()[x].name.encode('utf-8')
        #print "Sheets Number(%s): %s" %(x,p.decode('utf-8'))
    
    #遍历excel中的所有内容,寻找匹配的字段
    for x in shxrange:
        sh=bk.sheets()[x]
        nrows=sh.nrows  #行数
        ncols=sh.ncols  #列数
        #print "file:%s--sheet:%d line:%d col:%d" %(Filename,x,nrows,ncols) #显示文件名,sheet名,每个sheet的行数,列数
        nrows_range=range(sh.nrows)
        ncols_range=range(sh.ncols)
        outputfile=open(outputfilename,'a')
        for y in nrows_range:
            for z in ncols_range:
                #写入SVN版本号
                if str(sh.cell_value(y,z)) == "svn version":
                    outputfile.write(str(sh.cell_value(y,z+1))+':')
                if testin in str(sh.cell_value(y,z)):
                    print "sheet:%d line:%d col:%d equal" %(x+1,y+1,z+1)
                    outputs=str(sh.cell_value(y,z+1))
                    #此处需要考虑该字符串对应的数值不存在的情况
                    if outputs.strip()=='':
                        outputs="0"
                    outputfile.write(str(outputs)+'\n')   #此处需要加类型转换,如果excel中单元格的内容为数值格式,不转换会出错
                    outputfile.close()
                    return
                    


'''
功能:可以统计文件夹下某种后缀的文件的数量
author:gjh
data:2016-10-31
version:1.0.0
'''
#已调通
#def file_count(dirname,filter_types=[]):
#     '''
#     Count the files in a directory includes its subfolder's files
#        You can set the filter types to count specific types of file
#     '''
#     count=0
#     filter_is_on=False
#     if filter_types!=[]: filter_is_on=True
#     for item in os.listdir(dirname):
#         abs_item=os.path.join(dirname,item)
#         #print item
#         if os.path.isdir(abs_item):
#             #Iteration for dir
#             count+=file_count(abs_item,filter_types)
#         elif os.path.isfile(abs_item):
#             if filter_is_on:
#                 #Get file's extension name
#                 extname=os.path.splitext(abs_item)[1]
#                 if extname in filter_types:
#                     count+=1
#             else:
#                 count+=1
#     return count
#
#filepath = 'C:\\Users\\guojinhe\\Desktop\\statics\\matplotlib_example\\test' #此处需要注意转译字符,程序中 \ 是转义符
#filters=['.xlsx']
#file_count(filepath,filters)
#print "the total file num is: %d\n"%file_count(filepath,filters)

'''
功能:遍历文件夹下所有excel文件,顺序打开,获取所需数据并存储到TXT文件中
author:gjh
date:2016-10-31
version:1.0.0
'''

def readfile(dir):
    for f in os.listdir(dir):
		file = os.path.join(dir, f)
		if os.path.isdir(file):
			readfile(file)
		elif os.path.isfile(file):
		    read_excel(file)


'''
功能:打开一个TXT文件,分离数据和度量单位
author:gjh
date:2016-10-31
version:1.0.0
'''

def load_data(filename):
    x=[]
    y=[]
    ytemp=[]
    
    with open(filename) as f:
        for line in f:
            trainingSet = line.split(':')
            x.append(trainingSet[0])
            ytemp.append(trainingSet[1])
    
    #当数据带有单位kb时,需要拆分
    for i in ytemp:
        #print (i.split(' '))
        y.append(i.split(' ')[0])
                
    return (x,y)
    
    
'''
功能:根据TXT文件中的数据画图
author:gjh
date:2016-10-31
version:1.0.0
'''   
def plot(x,y):
    plt.figure(dpi=72,facecolor="white")
    axes = plt.subplot(111)
    axes.cla()  #清空坐标轴内的所有内容
        
#        font = {'family'    :   'serif',
#                'color'     :   'darkred',
#                'weight'    :   'normal',
#                'size'      :   10,
#               }

    plt.plot(x,y,'-o', mfc='orange') #显示数据点
    plt.grid(True)
    plt.xlabel('svn version')
    plt.ylabel(testin)
   
    plt.show()
    

if __name__=='__main__':
    dir = 'C:\Users\guojinhe\Desktop\statics\excel'  #excel文件所在的路径
    testin='mem used'  #需要统计的字符串
    outputfilename=testin + '.txt'
    readfile(dir)
    (x,y)=load_data(outputfilename)
    plot(x,y)
   
