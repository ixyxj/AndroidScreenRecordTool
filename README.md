### AndroidScreenRecordTool

> Python写的Android屏幕录制工具并转换成gif



### 开始

- 安装python3运行环境
- 当前是windows版本,后续增加Mac

### 使用

录屏,并转gif: run_record.py

命令: 

- adb shell screenrecord --time-limit 10 -verbose
- adb pull /sdcard/xxx.mp4 c:\\xxx.mp4
- adb shell rm -f /sdcard/xxx.mp4
- ffmpeg -i xxx.mp4 -vf scale=iw/2:ih/2 -r 10 xxx.gif

运行结果:

```
$ python /c/Users/silen/Desktop/AndroidScreenRecoderTools/run_record.py

===>开始录制
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe shell screenrecord --time-limit 10 --verbose /sdcard/record_2018_12_19_00_25_22.mp4
===>录制结束
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe pull /sdcard/record_2018_12_19_00_25_22.mp4 C:\Users\silen\Desktop\AndroidScreenRecoderTools\record_2018_12_19_00_25_22.mp4
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe shell rm-f /sdcard/record_2018_12_19_00_25_22.mp4
===>开始转换
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\ffmpeg.exe -i C:\Users\silen\Desktop\AndroidScreenRecoderTools\record_2018_12_19_00_25_22.mp4 -r 10 C:\Users\silen\Desktop\AndroidScreenRecoderTools/record_2018_12_19_00_25_22.gif
===>转换成功

```

截图: run_shot.py

命令:adb shell screencap -p xxx.png

```
$ python /c/Users/silen/Desktop/AndroidScreenRecoderTools/run_shot.py
===>开始截图
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe shell screencap -p /sdcard/shot_2018_12_19_00_25_07.png
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe pull /sdcard/shot_2018_12_19_00_25_07.png C:\Users\silen\Desktop\AndroidScreenRecoderTools\shot_2018_12_19_00_25_07.png
===>C:\Users\silen\Desktop\AndroidScreenRecoderTools\win-tools\adb.exe shell rm-f /sdcard/shot_2018_12_19_00_25_07.png
===>截图结束
```



> 看到这里,点个赞呗!