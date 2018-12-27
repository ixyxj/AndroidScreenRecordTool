#!/usr/bin/env python
# encoding=utf-8

# 输入文字刷屏

import os
import subprocess
import platform
import time

# 判断系统
sys_str = platform.system()
adb_path = os.path.abspath('.')
out_file_name = time.strftime("shot_%Y_%m_%d_%H_%M_%S.png", time.localtime())

if 'Windows' == sys_str:
    adb_path += '\\win-tools\\adb.exe'
elif 'Linux' == sys_str:
    adb_path += ''
elif 'Mac' == sys_str:
    adb_path += ''


# 执行adb
def cmd(command):
    print("===>" + command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.stdout.read()


# 手机录制文件
print("===>发文字")
count = 1
while count <= 100:
    cmd("%s shell input text %s" % (adb_path, "\"hello\""))
    #time.sleep(0.01)
    cmd("%s shell input tap 1000 1475" % adb_path)
    count += 1
