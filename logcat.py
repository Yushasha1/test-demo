import chardet
import subprocess
obj = subprocess.Popen("adb logcat", shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
for item in iter(obj.stdout.readline,'b'):
    encode_type = chardet.detect(item)
    if encode_type['encoding'] == 'utf-8':
        print(item.decode('utf-8'))
    elif encode_type['encoding'] == 'Windows-1252':
        print(item.decode('Windows-1252'))
    else:
        print(item.decode('gbk'))
