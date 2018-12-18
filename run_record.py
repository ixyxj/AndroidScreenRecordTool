#!/usr/bin/env python
# encoding=utf-8

import os
import subprocess
import platform
import time

# 判断系统
sys_str = platform.system()
current_path = os.path.abspath('.')
adb_path = current_path
ffmpeg_path = current_path
out_file_name = time.strftime("record_%Y_%m_%d_%H_%M_%S.mp4", time.localtime())

if 'Windows' == sys_str:
    adb_path += '\\win-tools\\adb.exe'
    ffmpeg_path += '\\win-tools\\ffmpeg.exe'
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
print("===>开始录制")
sdcard_file_path = '/sdcard/' + out_file_name
cmd("%s shell screenrecord --time-limit 10 --verbose %s" % (adb_path, sdcard_file_path))
print("===>录制结束")


# 录制完成获取视频
mp4_out_file_path = os.path.abspath('.') + '\\' + out_file_name
pull_file_info = cmd("%s pull %s %s" % (adb_path, sdcard_file_path,
                                        mp4_out_file_path))
# 删除手机里面的视频
cmd("%s shell rm -f %s" % (adb_path, sdcard_file_path))

# 开始转换成gif
print("===>开始转换")
gif_out_file_path = os.path.abspath('.') + '/' + out_file_name.replace(".mp4", ".gif")
cmd("%s -i %s -vf scale=iw/2:ih/2 -r 10 %s" % (ffmpeg_path, mp4_out_file_path,gif_out_file_path))
print("===>转换成功")







