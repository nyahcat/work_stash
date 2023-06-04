import os
import datetime
import time

command_list = []
capture_efir_path = r"\\ONAIR-02\D$\CAPTURE EFIR\SLStreamCapture"
video_numbers = [str(i) for i in range(7820, 7826 + 1)]


def ffmpeg_compiler(commands):
    for command in commands:
        os.system(command)
        time.sleep(40)


def ffmpeg_command_creator(file_name, date, date_reduced):
    global capture_efir_path, command_list
    lan_path = capture_efir_path + '\\' + date.strftime('%Y') + '\\' + date.strftime('%m') + '\\'

    for end_num in range(50):
        if not check_exist_file(lan_path + file_name):
            if end_num >= 10:
                file_name = file_name[:-6]
            else:
                file_name = file_name[:-5]
            file_name += f'{end_num}.mp4'
        else:
            break

    lan_path += file_name
    hours = date.hour
    if date_reduced:
        hours = date.hour - 1
    time_offset = (date - datetime.timedelta(hours=hours, minutes=2)).strftime("%H:%M:%S")
    temp = time_offset.split(':')
    if int(temp[0]) >= 2:
        time_offset = '00:00:00'
    if date_reduced:
        date = (date + datetime.timedelta(hours=1))
    output_file_name = '_MTV_GIBDD_ ' + datetime.datetime.strftime(date, '%Y-%m-%d %H.%M.%S') + '.mp4'
    command = f'ffmpeg -i "{lan_path}" -codec copy -ss {time_offset}.0  -t 270 "{output_file_name}"'
    command_list.append(command)


def get_video_name(date):
    date_reduced = False
    if not date.hour % 2 == 0:
        date = date - datetime.timedelta(hours=1)
        date_reduced = True
    file_name = f'EFIR _{date.strftime("%m_%d")}_{date.strftime("%H")}_00_00.mp4'

    ffmpeg_command_creator(file_name, date, date_reduced)


def check_exist_file(file_path):
    return True if os.path.exists(file_path) else False


def is_true(line):
    global video_numbers
    true_list = (i in line for i in video_numbers)
    return True if any(true_list) else False


def get_strings(log, date):
    if date in log[0]:
        for line in log:
            if is_true(line):
                line_list = line.split(' ', 2)
                date_obj = datetime.datetime.strptime(date + ' ' + line_list[0], '%Y-%m-%d %H:%M:%S')
                get_video_name(date_obj)
    else:
        return


if __name__ == '__main__':
    log_file_name = ''
    for file in os.listdir():
        if file.endswith('.txt'):
            log_file_name = file
    with open(log_file_name, 'r') as text_log:
        text = text_log.readlines()
    get_strings(log=text, date=text[0])
    command_tuple = (i for i in command_list)
    command_list = []
    for i in command_tuple:
        print(i)
    # ffmpeg_compiler(command_tuple)
