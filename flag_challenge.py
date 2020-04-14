from tkinter import *
from tkinter.messagebox import showinfo
import random
import os

wnd = Tk()
engl = os.path.join(os.path.dirname(__file__), os.path.dirname('flgs+/'), 'the UK.ico')
ukr = os.path.join(os.path.dirname(__file__), os.path.dirname('flgs+/'), 'ukr.ico')
wnd.iconbitmap(engl)
wnd.title('Flag_Challenge by St.Polishchuk')
wnd.rowconfigure(0, weight = 1)
wnd.columnconfigure(0, weight = 1)

flags = {'belgium.png':'brussels',
'france.png':'paris', 
'georgia.png': 'tbilisi',
'germany.png': 'berlin',
'india.png': 'dehli',
'norway.png': 'oslo',
'poland.png': 'warsaw',
'spain.png':'madrid',
'sweden.png':'stockholm',
'the UK.png':'london',
'ukraine.png':'kyiv',
'usa.png':'washington',
'canada.png':'ottawa',
'egypt.png':'cairo',
'iceland.png':'reykjavik',
'japan.png':'tokio',
'portugal.png':'lisbon',
'romania.png':'bucharest',
'serbia.png':'belgrade',
'slovakia.png':'bratislava',
'switzerland.png':'bern',
'greece.png':'athens',
'austria.png':'vienna',
'finland.png':'helsinki',
'turkey.png':'ankara'}

flags_ua = {'belgium.png':'брюсель',
'france.png':'париж', 
'georgia.png': 'тбілісі',
'germany.png': 'берлін',
'india.png': 'делі',
'norway.png': 'осло',
'poland.png': 'варшава',
'spain.png':'мадрид',
'sweden.png':'стокгольм',
'the UK.png':'лондон',
'ukraine.png':'київ',
'usa.png':'вашингтон',
'canada.png':'оттава',
'egypt.png':'каїр',
'iceland.png':'рейкявік',
'japan.png':'токіо',
'portugal.png':'лісабон',
'romania.png':'бухарест',
'serbia.png':'белград',
'slovakia.png':'братислава',
'switzerland.png':'берн',
'greece.png':'афіни',
'austria.png':'відень',
'finland.png':'хельсінкі',
'turkey.png':'анкара'}

flags_ua_cap = {'belgium.png':'бельгії',
'france.png':'франції', 
'georgia.png': 'грузії',
'germany.png': 'німеччини',
'india.png': 'індії',
'norway.png': 'норвегії',
'poland.png': 'польщі',
'spain.png':'іспанії',
'sweden.png':'швеції',
'the UK.png':'великобританії',
'ukraine.png':'україни',
'usa.png':'сша',
'canada.png':'канади',
'egypt.png':'єгипту',
'iceland.png':'ісландії',
'japan.png':'японії',
'portugal.png':'португалії',
'romania.png':'румунії',
'serbia.png':'сербії',
'slovakia.png':'словаччини',
'switzerland.png':'швейцарії',
'greece.png':'греції',
'austria.png':'австрії',
'finland.png':'фінляндії',
'turkey.png':'туреччини'}

def eng():
    sound_lbl.config(text = 'Music: ')
    sound_btn_on.config(text = 'On')
    sound_btn_off.config(text = 'Off')
    wnd.iconbitmap(engl)
    lang_lbl.config(text = lang_eng)
    global ua_state
    global eng_state
    ua_state = False
    eng_state = True
    wnd.title('Flag_Challenge by St.Polishchuk')
    lang_btn_ua.config(relief = RAISED)
    lang_btn_eng.config(relief = SUNKEN)
    nxt.config(text = next_eng)
    check.config(text = check_eng)
    task_labl.config(text = task_eng)
    next_()

def ua():
    sound_lbl.config(text = 'Музика: ')
    sound_btn_on.config(text = 'Вкл')
    sound_btn_off.config(text = 'Викл')
    wnd.iconbitmap(ukr)
    lang_lbl.config(text = lang_ua)
    global ua_state
    global eng_state
    ua_state = True
    eng_state = False
    wnd.title("Прапори та столиці. Ст.Поліщук")
    lang_btn_eng.config(relief = RAISED)
    lang_btn_ua.config(relief = SUNKEN)
    nxt.config(text = next_ua)
    check.config(text = check_ua)
    task_labl.config(text = task_ua)
    next_()

def rand_flag():
    global country
    global capital
    global flag
    fl = flags
    if ua_state:
        fl = flags_ua
    elif eng_state:
        fl = flags
    country, capital = random.choice(list(fl.items()))
    d = os.path.join(os.path.dirname(__file__), os.path.dirname('flgs+/'), country)
    flag = PhotoImage(file = d)

cach = []
num_of_items = len(flags.keys())
count = 0

def next_():
    global count
    rand_flag()
    if count < num_of_items:
        if country not in cach:
            flag_label.config(image = flag)
            mark_label.config(text = '')
            entry.delete(0, 'end')
            cach.append(country)
            count +=1
        elif country in cach:
            next_()
    else:
        result = (right-wrong)*100/num_of_items
        if result >=70.0:
            if eng_state:
                showinfo('Your result', f"You are a flag expert!\n{result}%")
            elif ua_state:
                showinfo('Ваш результат', f"Та ви експерт!\n{result}%")
        elif result <= 69.0 and result >= 40.0:
            if eng_state:
                showinfo('Your result', f"You are good at flags!\n{result}%")
            elif ua_state:
                showinfo('Ваш результат', f"Ви добре знаєтесь на прапорах!\n{result}%")
        elif result <=40.0:
            if eng_state:
                showinfo('Your result', f"You could do better!\n{result}%")
            elif ua_state:
                showinfo('Ваш результат', f"Ви могли б і краще!\n{result}%")

right = 0
wrong = 0

def chk():
    if eng_state:
        result_eng()
    elif ua_state:
        result_ua()
def result_eng():
    global right, wrong
    input_ = var.get()
    input_ = input_.lower()
    if input_ == "":
        mark_label.config(text = f"Oops!\nDon't leave the input blank!", 
        font = ('Arial', 14), fg = 'orange')
    elif input_ == capital:
        cntr = country.capitalize()
        cntr = cntr.split('.')
        cptl = capital.capitalize()
        mark_label.config(text = f"Right!\nThe capital of {cntr[0]} is {cptl}", 
        font = ('Arial', 14), fg = 'green')
        right += 1
        result.config(text = f"Score:\nRight: {right}\nWrong: {wrong}\n{len(cach)} / {num_of_items}")
    else:
        mark_label.config(text = 'Wrong!', font = ('Arial', 14), fg = 'red')
        wrong += 1
        result.config(text = f"Score:\nRight: {right}\nWrong: {wrong}\n{len(cach)} / {num_of_items}")
def result_ua():
    global right, wrong
    input_ = var.get()
    input_ = input_.lower()
    if input_ == "":
        mark_label.config(text = f"Овва!\nНе залишайте цю стрічку порожньою!", 
        font = ('Arial', 14), fg = 'orange')
    elif input_ == capital:
        cntr = country.capitalize()
        cntr = flags_ua_cap[country]
        cptl = capital.capitalize()
        mark_label.config(text = f"Вірно!\n{cptl} це столиця {cntr.capitalize()}", 
        font = ('Arial', 14), fg = 'green')
        right += 1
        result.config(text = f"Рахунок:\nВірно: {right}\nНевірно: {wrong}\n{len(cach)} / {num_of_items}")
    else:
        mark_label.config(text = 'Невірно!', font = ('Arial', 14), fg = 'red')
        wrong += 1
        result.config(text = f"Рахунок:\nВірно: {right}\nНевірно: {wrong}\n{len(cach)} / {num_of_items}")


frm1 = Frame(wnd)
frm1.pack(pady=4,padx=4)
frm2 = Frame(wnd)
frm2.pack(pady=4,padx=4)
frm3 = Frame(wnd)
frm3.pack(pady=4,padx=4)
frm4 = Frame(wnd)
frm4.pack(pady=4,padx=4)

flag_label = Label(frm1, relief = RAISED)
flag_label.pack()

mark_label = Label(frm1)
mark_label.pack()

task_eng = "What is this country's capital?"
task_ua = "Яка столиця цієї країни?"
task_labl = Label(frm1, text = 'Choose the language\nВиберіть мову', font = ('Arial', 14), fg = 'red')
task_labl.pack()

var = StringVar()
entry = Entry(frm1, textvariable = var)
entry.pack()

check_eng = 'Check'
check_ua = 'Перевірити'
check = Button(frm2, text = check_eng, height = 1, width = 10, command = chk,
activeforeground = 'red', font = ('Arial', 14))
check.grid(row = 0, column = 0, padx = 4)

next_eng = 'Next'
next_ua = 'Далі'
nxt = Button(frm2, text = next_eng, height = 1, width = 10, command = next_,
activeforeground = 'green', font = ('Arial', 14))
nxt.grid(row= 0, column = 1, padx = 4)

result = Label(frm3,fg = 'grey', font = ('Arial', 14))
result.pack()

lang_eng = 'Language: '
lang_ua = 'Мова: '
lang_lbl = Label(frm4, text = lang_eng)
lang_lbl.grid(row = 0, column = 0)

lang_btn_eng = Button(frm4, text = 'Eng', font = ('Arial', 10), command = eng)
lang_btn_eng.grid(row = 0, column = 1, padx = 4)

lang_btn_ua = Button(frm4, text = 'Укр', font = ('Arial', 10), command = ua)
lang_btn_ua.grid(row = 0, column = 2, padx = 4)

import winsound

sound = os.path.join(os.path.dirname(__file__), os.path.dirname('flgs+/'), 'Shuka.wav')


sound_lbl = Label(frm4, text = 'Music: ')
sound_lbl.grid(row = 0, column = 3)

sound_btn_on = Button(frm4, text = 'On', command = lambda: winsound.PlaySound(sound, winsound.SND_ASYNC))
sound_btn_on.grid(row = 0, column = 4, padx = 4)

sound_btn_off = Button(frm4, text = 'Off', command = lambda: winsound.PlaySound(None, winsound.SND_LOOP))
sound_btn_off.grid(row = 0, column = 5, padx = 4)

wnd.mainloop()