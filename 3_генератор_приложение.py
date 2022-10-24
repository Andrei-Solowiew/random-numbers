import sys
from tkinter import *
from random import randint

num_list = []
with open('num_list.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents:
        current_place = line[:-1]
        num_list.append(current_place)
num_file = open('num_list.txt', 'a')
qua_file = open('qua.txt', 'r+')
flag = False


def clicked():
    if open('qua.txt').readline() == '':
        lbl = Label(window, text="Введите количество студентов", font=('Arial Bold', 20))
        lbl.grid(column=0, row=0, padx=(25, 0))
        inp = Entry(window, width=10)
        inp.grid(column=0, row=20, padx=(25, 0), pady=(0, 0))
        result_text = Label(window, text="Номер", font=('Arial Bold', 20))
        result_text.grid(column=0, row=60, padx=(25, 0))

        def gen():
            qua = format(inp.get())
            rand = randint(1, int(qua))
            if len(num_list) == int(qua):
                qua_file = open('qua.txt', 'w')
                qua_file.write("")
                num_file = open('num_list.txt', 'w')
                num_file.write("")
                sys.exit()
            if rand not in num_list:
                num_list.append(rand)
                result.configure(text=rand)
                with open('num_list.txt', 'w') as filehandle:
                    filehandle.writelines("%s\n" % place for place in num_list)
            else:
                while rand in num_list:
                    rand = randint(1, int(qua))
                num_list.append(rand)
                with open('num_list.txt', 'w') as filehandle:
                    filehandle.writelines("%s\n" % place for place in num_list)
                result.configure(text=rand)

            qua_file = open('qua.txt', 'r+')
            qua_file.close()
            qua_file = open('qua.txt', 'w')
            qua_file.write(qua)
            resume = Button(window, text="Продолжить!", command=gen)
            resume.grid(column=0, row=40, padx=(25, 0), pady=(5, 0))

            def cleaned():
                qua_file = open('qua.txt', 'w')
                qua_file.write("")
                num_file = open('num_list.txt', 'w')
                num_file.write("")
                sys.exit()

            clean = Button(window, text="Отчистить!", command=cleaned)
            clean.grid(column=0, row=100, padx=(25, 0), pady=(5, 0))

        btn = Button(window, text="Отправить!", command=gen)
        btn.grid(column=0, row=40, padx=(25, 0), pady=(5, 0))
    else:
        qua = int(float(open('qua.txt').readline()))  # без этой строчки программа будет работать неправильно
        inv.configure(text='Генератор продолжает работу')
        result_text = Label(window, text="Номер", font=('Arial Bold', 20))
        result_text.grid(column=0, row=60, padx=(25, 0))

        def gen_else():
            qua = int(float(open('qua.txt').readline()))
            rand = randint(1, int(qua))
            if len(num_list) == int(qua):
                qua_file = open('qua.txt', 'w')
                qua_file.write("")
                num_file = open('num_list.txt', 'w')
                num_file.write("")
                sys.exit()
            if str(rand) not in num_list:
                num_list.append(str(rand))
                with open('num_list.txt', 'w') as filehandle:
                    filehandle.writelines("%s\n" % place for place in num_list)
                result.configure(text=rand)
            else:
                while str(rand) in num_list:
                    rand = randint(1, int(qua))
                num_list.append(str(rand))
                with open('num_list.txt', 'w') as filehandle:
                    filehandle.writelines("%s\n" % place for place in num_list)
                result.configure(text=rand)

            qua_file = open('qua.txt', 'r+')
            qua_file.close()
            qua_file = open('qua.txt', 'w')
            qua_file.write(str(qua))
            resume = Button(window, text="Продолжить!", command=gen_else)
            resume.grid(column=0, row=40, padx=(25, 0), pady=(5, 0))

        resume = Button(window, text="Продолжить!", command=gen_else)
        resume.grid(column=0, row=40, padx=(25, 0), pady=(5, 0))

        def cleaned():
            qua_file = open('qua.txt', 'w')
            qua_file.write("")
            num_file = open('num_list.txt', 'w')
            num_file.write("")
            sys.exit()

        clean = Button(window, text="Отчистить!", command=cleaned)
        clean.grid(column=0, row=100, padx=(25, 0), pady=(5, 0))


window = Tk()
window.title("Генератор случайных чисел")
window.geometry('450x250')
inv = Label(window, text="Нажмите чтобы начать", font=('Arial Bold', 20))
inv.grid(column=0, row=0, padx=(25, 0))
start = Button(window, text="Старт!", command=clicked)
start.grid(column=0, row=40, padx=(25, 0), pady=(5, 0))
result = Label(window, text='')
result.grid(column=0, row=80, padx=(25, 0))
me = Label(window, text='Работу выполнил студент группы П9021 Соловьев Андрей Владимирович', fg='#B5B8B1')
me.grid(column=0, row=150, padx=(25, 0), pady=(70, 0))
window.mainloop()
