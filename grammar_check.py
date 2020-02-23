from tkinter import *
import random

wnd = Tk()
wnd.title("Rick_and_Morty_Grammar (by St.Polishchuk)")
wnd.resizable(0,0)


frm1 = Frame(wnd)
frm1.pack()
frm2 = Frame(wnd)
frm2.pack()
frm3 = Frame(wnd)
frm3.pack()


to_be = {"I ... sorry, but your opinion means very little to me. – Rick": "am", 
"Nobody exists on purpose. Nobody belongs anywhere. \nWe ... all going to die. Come watch TV.  – Morty": "are", 
"Life ... effort and I’ll stop when I die! - Jerry": "is", 
"I ... tell you how I feel about school, Jerry: it’s a waste of time.": "will",
"'Dad, ... I evil?' 'Worse. You’re smart.'": "am",
"It ... a new machine. It detects stuff all the way up your butt.":"is",
"That’s it! That’s it, Rick! I ... taking the wheel!": "am",
"I ...n't born into the God business, I fucking earned it.": "was", 
"When you know nothing matters, the universe is yours. \nAnd I’ve never met a universe that ... into it.": "was", 
"There is no god, Summer;\n gotta rip that band-aid off now you ... thank me later.": "will",
"Concentrated dark matter? They ... asking about that in class.":"were",
"Weddings ... basically funerals with cake. - Rick":"are",
"Do not call me that! Snuffles ... my slave name. \nYou shall now call me Snowball, \nbecause my fur is pretty and white.":"was"}

class game:
    def random_choice():
        global text
        text = random.choice(list(to_be))
        labl.config(text=text,font=("bold",16))
        labl1.config(text="",)
    def check():
        value = var.get()
        key = text
        if key in to_be and value == to_be[text]:
            labl1.config(text="Well done!",font=("bold",16),fg='green',)
        else:
            labl1.config(text="Nope!",font=("bold",16),fg='red',)


labl = Label(frm1,width=50,bg = 'grey',fg = 'white')
labl.pack()

labl1 = Label(frm2)
labl1.pack()

labl2 = Label(frm2,text="Insert the correct \nform of the verb 'to be':",font=('italics',14))
labl2.pack()

tobe_lst = ['is','are','am','was','were','will']
var = StringVar()
spnb = Spinbox(frm2,values=tobe_lst,textvariable=var,font=('italics',14))
spnb.pack()


btn = Button(frm3,width=15,height=1,text="Next",command=game.random_choice,
activeforeground='green',font=('italics',14))
btn.grid(row=0,column=0,pady=5)

btn_check = Button(frm3,width=15,height=1,text="Check",command=game.check,
activeforeground='red',font=('italics',14))
btn_check.grid(row=0,column=1,pady=5)

game.random_choice()

wnd.mainloop()