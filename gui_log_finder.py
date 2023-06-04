from tkinter import *
import AirLog_finder_core
window = Tk()


def btn_click():
    str_to_find = string_input.get()
    date_to_find = date_input.get()
    a = str_to_find
    b = date_to_find
    print(a, b)

    s = AirLog_finder_core.get_logs(str_to_find, date_to_find)
    print(s)

def btn_info_click():
    info_str = 'В строку для поиска вводится ФРАГМЕНТ имени \nфайла или номер файла цифрами (Например: 7738)\n' \
               '\n\nВ строку "месяц и год" вводится номер месяца \n(01-12) и год через пробел в формате: ' \
               'mm yyyy \n   (в соответствии с именем папки, например: 03 2021)\n\n' \
               'После нажатия кнопки "Start" в той папке, где\nнаходится программа будет создан файл-отчёт\n' \
               'в формате .txt\n\n' \
               'Если в файле информация не соответствует\n ожидаемому или файл-отчёт не создаётся:\n\n' \
               'Внимательно проверьте параметры поиска \nили существование папки или логов в архиве по пути\n' \
               '\ARHIV\Arhiv\ARHIV_PLAYLISTs\LOG\<имя папки (дата)>\n\nВ случае других проблем обратитесь к инженерам\n' \
               'Нажмите "ОК" для выхода'

    window_info = Tk()
    window_info.title("Инструкция")
    window_info.geometry('450x430')
    window_info.resizable(width=False, height=False)
    frame_info = Frame(window_info, bg='gray')
    frame_info.pack()

    title_info = Label(frame_info, anchor='center', text=info_str, font=40)
    title_info.pack()

    close_btn = Button(frame_info, text='OK', command=lambda: window_info.destroy())
    close_btn.pack(anchor='center', expand=1)


window['bg'] = '#c0c0c0'
window.title('AirLog_finder v1.0')
window.geometry('300x450')

window.resizable(height=False, width=False)

canvas = Canvas(window, height=450, width=300)
canvas.pack()

frame = Frame(window, bg='gray')
frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)

title = Label(frame, text='Введите строку для поиска:', bg='#fff8dc', font=40)
title.place(rely=0.05, relheight=0.05, relx=0.120)

title_date = Label(frame, text='Введите месяц и год (03 2021):', bg='#fff8dc', font=40)
title_date.place(rely=0.22, relheight=0.05, relx=0.0725)

warning_text = 'Поиск по AirLog создаёт текстовый\nфайл в папке исполнения\nпрограммы!\n'
title_warning = Label(frame, text=warning_text, bg='#fff8dc', font=25, anchor='n')
title_warning.place(rely=0.8, relheight=0.19, relx=0.0105)

string_input = Entry(frame, bg='white', width=150)
string_input.place(rely=0.12, relheight=0.05, relx=0.05, relwidth=0.9)

date_input = Entry(frame, bg='white', width=150)
date_input.place(rely=0.29, relheight=0.05, relx=0.05, relwidth=0.9)

btn = Button(frame, text='Start', bg='white', width=30, command=btn_click)
btn.place(rely=0.7, relheight=0.05, relx=0.70, relwidth=0.2)

btn_info = Button(frame, text='Инструкция', bg='white', width=30, command=btn_info_click)
btn_info.place(rely=0.7, relheight=0.05, relx=0.05, relwidth=0.4)


window.mainloop()