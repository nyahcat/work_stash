import datetime


def get_logs():

    range_in = 7820
    range_out = 7826

    date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    with open(r'\\ONAIR-02\D$\SoftLab-NSK\Data\AirLog.txt', 'r') as text_log_02:
        text_onair_02 = text_log_02.readlines()
    line_list_02 = get_strings(text_onair_02, date, range(range_in, range_out + 1))

    with open(r'\\ONAIR-01\D$\SoftLab-NSK\Data\AirLog.txt', 'r') as text_log_01:
        text_onair_01 = text_log_01.readlines()
    line_list_01 = get_strings(text_onair_01, date, range(range_in, range_out + 1))

    write_file(line_list_01, line_list_02, date)


def get_result_str(onair_log):
    res = ''
    for line in onair_log:
        res += ' '.join(line[1:]) + '\n'
    return res


def write_file(onair_01_log, onair_02_log, date):

    res_01 = get_result_str(onair_01_log)

    res_02 = get_result_str(onair_02_log)

    res_00 = f'{date}\n\nONAIR-01:\n{res_01}\n\nONAIR-02:\n{res_02}'
    file_name = rf'\\videoserver\ONAIR_TEMP\_ОТЧЕТ ГИБДД_\РОЛИКИ ГИБДД {date} .txt'

    with open(file_name, 'w') as file:
        file.write(res_00)


def get_strings(log, date, file_n_range):
    result = []
    for file_num in file_n_range:
        for line in log:
            if date in line and f'№{file_num}' in line:
                line_list = line.split(';')
                line_list[1] = line_list[1][:-3]
                line_list.pop()
                result.append(line_list)
    result = sorted(result, key=lambda x: datetime.datetime.strptime(x[1], '%H:%M:%S'), reverse=False)
    return result


if __name__ == '__main__':
    get_logs()
