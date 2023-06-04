import os
import datetime
import time

command_list = []
# file_path = os.path.abspath('РОЛИКИ ГИБДД 2023-04-10 .txt')

# Сетевой путь до папки с записями эфира
capture_efir_path = r"\\ONAIR-02\D$\CAPTURE EFIR\SLStreamCapture"

# Присвоенные номера видеороликов:
video_numbers = [str(i) for i in range(7820, 7826 + 1)]

# 2023-03-01;08:42:06.77;№7738 Прием на работу МТВ 12+.mp4;


def ffmpeg_compiler(commands):
    for command in commands:
        os.system(command)
        time.sleep(40)


def ffmpeg_command_creator(file_name, date, clip_num, date_reduced):
    # ' ffmpeg -i "{EFIR _03_17_18_00_00.mp4}" -ss {00:09:00}.0 -codec copy -t 270 "{output1.mp4}" '
    #                  {file_name}               {time_offset}                   {output_file_name}

    # рабочие команды:
    # ffmpeg -i "D:\PyCharm project\EFIR _03_17_22_00_00.mp4" -codec copy -ss 00:56:58.0 -t 270 "D:\PyCharm project\EFIR _03_17_22_00_00_cut.mp4"
    # ffmpeg -i "\\ONAIR-02\D$\CAPTURE EFIR\SLStreamCapture\2023\03\EFIR _03_31_22_00_00.mp4" -codec copy -ss 00:56:58.0 -t 270 "D:\PyCharm project\EFIR _03_17_22_00_00_cut.mp4"
    # ffmpeg -i "\\ONAIR-02\D$\CAPTURE EFIR\SLStreamCapture\2023\03\EFIR _03_31_22_00_00.mp4" -codec copy -ss 00:56:58.0 -t 270 "EFIR _03_17_22_00_00_cut.mp4"

    # temp_test:
    # ffmpeg -i "\\ONAIR-02\D$\CAPTURE EFIR\SLStreamCapture\2023\03\EFIR _03_24_22_00_00.mp4" -codec copy -ss 00:56:58.0  -t 270 "EFIR _03_24_22_00_00_cut.mp4" +++

    global capture_efir_path, command_list
    lan_path = capture_efir_path + '\\' + date.strftime('%Y') + '\\' + date.strftime('%m') + '\\' + file_name
    # print(f'ffmpeg_command_creator/lan_path: {lan_path}')

    hours = date.hour
    if date_reduced:
        hours = date.hour - 1

    time_offset = (date - datetime.timedelta(hours=hours, minutes=2)).strftime("%H:%M:%S")
    temp = time_offset.split(':')
    if int(temp[0]) >= 2:
        temp[0] = '00'
        temp[1] = '00'
        temp[2] = str(60 - int(temp[2]))
        time_offset = ':'.join(temp)

    # print(f'ffmpeg_command_creator/time_offset: {time_offset}')
    date = (date + datetime.timedelta(hours=1))
    # output_file_name = clip_num + ' ' + '.'.join(time_offset.split(':')) + ' from ' + file_name[:-4] + '_cut.mp4'
    output_file_name = '_MTV_GIBDD_ ' + datetime.datetime.strftime(date, '%Y-%m-%d %H.%M.%S') + '.mp4'
    print(f'ffmpeg_command_creator/output_file_name: {output_file_name}')

    command = f'ffmpeg -i "{lan_path}" -codec copy -ss {time_offset}.0  -t 270 "{output_file_name}"'
    # print(f'ffmpeg_command_creator/command: {command}')

    command_list.append(command)


def get_video_name(clip_num, date):
    # date_reduced - флаг переноса часа, если время не кратно двум
    date_reduced = False
    if not date.hour % 2 == 0:
        date = date - datetime.timedelta(hours=1)
        date_reduced = True
    # print(f'get_video_name/date: {date}')

    """ file_name is correct! """
    file_name = f'EFIR _{date.strftime("%m_%d")}_{date.strftime("%H")}_00_00.mp4'  # example: EFIR _03_24_14_00_00.mp4

    # print(f'get_video_name/file_name: {file_name}')                      # respond: EFIR _03_24_14_00_00.mp4
    ffmpeg_command_creator(file_name, date, clip_num, date_reduced)


def is_true(line):
    global video_numbers
    true_list = (i in line for i in video_numbers)
    return True if any(true_list) else False


def get_log_name():
    date_input = input('Введите дату в формате "yyyy-mm-dd" (Например: 2023-04-10): ')
    return os.path.abspath(f'РОЛИКИ ГИБДД {date_input} .txt'), date_input


def get_strings(log, date):
    if date in log[0]:
        for line in log:
            if is_true(line):
                line_list = line.split(' ', 2)
                clip_num = line_list[1]
                date_obj = datetime.datetime.strptime(date + ' ' + line_list[0], '%Y-%m-%d %H:%M:%S')
                # print('=' * 20)
                # print(date_obj)
                # print(line_list)

                get_video_name(clip_num, date_obj)
    else:
        return


if __name__ == '__main__':
    # log_file_name = get_log_name()
    log_file_name = ''
    for file in os.listdir():
        if file.endswith('.txt'):
            log_file_name = file
    with open(log_file_name, 'r') as text_log:
        text = text_log.readlines()
    get_strings(log=text, date=text[0])
    # print(f'len(command_list): {len(command_list)}')
    command_tuple = (i for i in command_list)
    command_list = []
    for i in command_tuple:
        print(i)
    # ffmpeg_compiler(command_tuple)
