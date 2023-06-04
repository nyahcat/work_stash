import os

# d:\_Отчет\__ГТРФ\Материал для отчёта\2023\Часть1 Апрель\
# Новости Волгограда и области 03.04.2023 17-00

path_to = r'D:\_Отчет\__ГТРФ\Материал для отчёта\2023\Часть2 Май'

def start(entity):
    if os.path.isdir(entity):
        for file in os.listdir(entity):
            path_file = os.path.join(entity, file)
            if file.startswith('Новости') and file.endswith('.mp4'):
                name_list = file.split(' ')
                date = name_list[-2].replace('.', '')[:4]
                clip_num = ''
                if '17' in name_list[-1]:
                    clip_num = '1'
                elif '20' in name_list[-1]:
                    clip_num = '2'
                else:
                    raise NameError(f' *** Check name of file! {file} ***')
                res_name = fr'{entity}\ВРЕМЯ НОВОСТЕЙ {date}23 - {clip_num}.mp4'
                os.rename(path_file, res_name)
                print(f'renamed {path_file} to {res_name}')


if __name__ == '__main__':

    for file in os.listdir(path_to):
        path = os.path.join(path_to, file)
        start(path)