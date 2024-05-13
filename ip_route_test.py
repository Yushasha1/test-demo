#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021-9-17
@author: wyb
"""

import time
import subprocess
from datetime import datetime

# 将ip route 参照strtype1和strtype2配置，开机后通过adb shell
# 读取 ip route结果，判断每次开机是否配置成功。
strtype1 = r"192.168.23.1 via 192.168.31.1 dev eth0  metric 99"
#strtype2 = r"192.168.22.0/24 via 192.168.23.1 dev eth0  metric 99"
#strtype3 = r"192.168.23.0/24 via 192.168.23.1 dev eth0  metric 99"

def rebootAndWait():
    # print("In rebootAndWait; ")
    cmd1 = "adb shell "
    cmd_reboot = "adb reboot"
    cmd_wait = "adb wait-for-device"
    cmd_logcat = "adb logcat -d -v time  | grep  'Vold 3.0' "
    cmd_iproute = "adb shell ip route "
    cmdres = subprocess.getoutput(cmd_reboot)
    cmdres = subprocess.getoutput(cmd_wait)
    time.sleep(10)
    cmdres = subprocess.getoutput(cmd_iproute)
    print(cmdres)
    if cmdres.find(strtype1) != -1:# and cmdres.find(strtype2) != -1      :
        time.sleep(3)
        print("Reboot and add sccueed")
        return True
    else:
        time.sleep(3)
        print("Reboot and add fail")
        return False



if __name__ == '__main__':
    j = 0
    loop_num = 100
    while j < loop_num:
        print("\n++++",j,"+++")
        ret = rebootAndWait()
        if ret == False:
            break
        j +=1

