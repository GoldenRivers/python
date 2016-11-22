#!/bin/sh

##################################################
#设备性能统计脚本
#统计项目:总内存,可用内存,CPU使用率,后续再增加
##################################################

while true
do
    #################################################
    #剩余内存统计
    #################################################
    
    MemoryInfo=$(cat /proc/meminfo | awk '{print $2}')
    
    Total=$(echo $MemoryInfo | awk '{print $1}')
    Free=$(echo $MemoryInfo | awk '{print $2}')
    buffer=$(echo $MemoryInfo | awk '{print $3}')
    cache=$(echo $MemoryInfo | awk '{print $4}')
    
    Mem_Used=`echo "$Total $Free $buffer $cache"|awk '{printf("%g",($1-$2-$3-$4))}'`
    Mem_Used_Rate=`echo "$Mem_Used $Total"|awk '{printf("%4.2f",($1/$2*100))}'`

    echo -n `date +"%Y-%m-%d %H:%M:%S"` "   " >> /dav/mem.txt
    echo $Mem_Used_Rate >> /dav/mem.txt
    
    #################################################
    #CPU使用率统计
    #################################################
    #方法1:采用读取cat /proc/stat的方法
    
    CPULOG_1=$(cat /proc/stat | awk -F: '/cpu0/' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8" "$9}')

    SYS_USE_1=$(echo $CPULOG_1 | awk '{print $1+$2+$3+$5+$6+$7+$8}') #$4为idle

    Total_1=$(echo $CPULOG_1 | awk '{print $1+$2+$3+$4+$5+$6+$7+$8}')

    
    sleep 3
    
    CPULOG_2=$(cat /proc/stat | awk -F: '/cpu0/' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8" "$9}')

    SYS_USE_2=$(echo $CPULOG_2 | awk '{print $1+$2+$3+$5+$6+$7+$8}')

    Total_2=$(echo $CPULOG_2 | awk '{print $1+$2+$3+$4+$5+$6+$7+$8}')

    
    SYS_USE=`echo "$SYS_USE_2 $SYS_USE_1"|awk '{printf("%4.2f",($1-$2))}'`

    Total=`echo "$Total_2 $Total_1"|awk '{printf("%4.2f",($1-$2))}'`
    
    #use_rate
    SYS_USE_RATE=`echo "$SYS_USE $Total"|awk '{printf("%4.2f",($1/$2*100))}'`
    
    echo -n `date +"%Y-%m-%d %H:%M:%S"` "   " >> /dav/cpu.txt #-n 表示不换行
    
    echo $SYS_USE_RATE >> /dav/cpu.txt
done



