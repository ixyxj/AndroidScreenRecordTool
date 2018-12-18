#!/usr/bin/env python
# encoding=utf-8

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
print("===>开始截图")
sdcard_file_path = '/sdcard/' + out_file_name
cmd("%s shell screencap -p %s" % (adb_path, sdcard_file_path))

# 保存截图
png_out_file_path = os.path.abspath('.') + '\\' + out_file_name
cmd("%s pull %s %s" % (adb_path, sdcard_file_path,
                       png_out_file_path))
# 删除截图
cmd("%s shell rm -f %s" % (adb_path, sdcard_file_path))

print("===>截图结束")
