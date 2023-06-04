import datetime
import os

name = ''
date = ''


def get_logs(str_to_find, date_to_find):
    # \\ARHIV\Arhiv\ARHIV_PLAYLISTs\LOG\
    # \\ONAIR-02\D$\SoftLab-NSK\Data\AirLog.txt

    global date
    date = date_to_find[:]

    path_to_dir = rf'\\ARHIV\Arhiv\ARHIV_PLAYLISTs\LOG\{date_to_find}'
    print(path_to_dir)
    for entry in os.scandir(path_to_dir):
        if entry.is_file() and entry.name.endswith('.txt'):

            with open(entry.path, 'r') as text_log_01:
                text_onair_01 = text_log_01.readlines()
            line_list_01 = get_strings(text_onair_01, str_to_find)

            with open(entry.path, 'r') as text_log_02:
                text_onair_02 = text_log_02.readlines()
            line_list_02 = get_strings(text_onair_02, str_to_find)

    write_file(line_list_01, line_list_02)


def get_result_str(onair_log):
    res = ''
    for line in onair_log:
        res += ' '.join(line) + '\n'
    return res


def write_file(onair_01_log, onair_02_log):

    res_01 = get_result_str(onair_01_log)

    res_02 = get_result_str(onair_02_log)

    res_00 = f'\n\nONAIR-01:\n{res_01}\n\nONAIR-02:\n{res_02}'
    file_name = f'{date} - {name}.txt'

    with open(file_name, 'w') as file:
        file.write(res_00)


def get_strings(log, str_to_find):
    result = []
    for line in log:
        if str_to_find in line:
            line_list = line.split(';')
            line_list[1] = line_list[1][:-3]

            if len(line_list) > 3:
                line_list = line_list[:3]
            elif len(line_list) == 3:
                line_list.pop()

            result.append(line_list)

    global name
    name = result[0][2][:]

    result = sorted(result, key=lambda x: datetime.datetime.strptime(x[0], '%Y-%m-%d'), reverse=False)
    return result


# get_logs('7455', '03 2021')