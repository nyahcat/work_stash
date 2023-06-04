import os
import time

path = r'D:\PyCharm project\ffmpeg_encode_dir'
for file in os.listdir(path):
    print(path+file, type(file))
    if file.endswith('.avi'):
        command_ffmpeg = rf'ffmpeg -i "{path}\{file}" -b 1000k "{path}\{file}_new.mp4"'
        os.system(command_ffmpeg)
        time.sleep(30)
