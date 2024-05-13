# -*- coding:utf-8 -*-
import os

import subprocess

#ADB命令#

#列出设备#
#command='adb devices'#
tt=os.popen('adb devices')
tmp=tt.read()
print("显示adb设备：")
print(tmp)

#查看root权限#
command='adb root'
aa=os.popen(command)
ro=aa.read()
print("显示root权限：")
print(ro)



#进shell的命令#
import subprocess
 
import subprocess
 
print("Shell命令获取：")

cmds = [
    "getprop | grep ro.build.type",
    'getenforce',
    "wm size",
    "getprop | grep ro.sf.lcd_density",
    "getprop ro.build.version.release",
    "getprop | grep ro.build.display.id",
    "getprop | grep ro.product.name",
    "getprop ro.product.cpu.abi",
    "dumpsys package com.android.settings | grep signatures",
    "exit",#退出
]
obj = subprocess.Popen("adb shell", shell= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
info = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'));
for item in info:
    if item:
        print(item.decode('utf-8'))
 


