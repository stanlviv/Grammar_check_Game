from tkinter import *
import random

def tobe():
    '''This function is called to depict Rock and Morty quotes 
    on 'to be' topic; it changes the font color of 'quote lable' to 
    'pale green', it nulls the 'check message', configurates the 'task lable'
    and randomly depicts the quote'''
    global text
    global tobe_btn_state
    global art_btn_state
    global vocab_btn_state
    global tenses_btn_state
    tobe_btn_state = True
    art_btn_state = False
    tenses_btn_state = False
    vocab_btn_state = False
    tobe_lst = ['is','are','am','was','were','will']
    text = random.choice(list(to_be))
    labl.config(text=text,font=("bold",20),fg='pale green')
    labl1.config(text="",)
    labl2.config(text = "Insert the correct \nform of the verb 'to be':")
    spnb.config(value = tobe_lst)
    btn_art.config(relief=RAISED)
    btn_tobe.config(relief=SUNKEN)
    btn_tns.config(relief=RAISED)
    btn_vocab.config(relief=RAISED)
    btn_art.config(fg='black')
    btn_tobe.config(fg='green')
    btn_tns.config(fg='black')
    btn_vocab.config(fg='black')

def art():
    '''This function is called to depict Rock and Morty quotes 
    on 'articles' topic; it changes the font color of 'quote lable' to 
    'yellow', it nulls the 'check message', configurates the 'task lable'
    and randomly depicts the quote'''
    global text
    global tobe_btn_state
    global art_btn_state
    global vocab_btn_state
    global tenses_btn_state
    tobe_btn_state = False
    art_btn_state = True
    tenses_btn_state = False
    vocab_btn_state = False
    artl = ['a', 'an', 'the']
    text = random.choice(list(articles))
    labl.config(text=text,font=("bold",20),fg='yellow')
    labl1.config(text="",)
    labl2.config(text = "Insert the correct article:")
    spnb.config(value = artl)
    btn_art.config(relief=SUNKEN)
    btn_tobe.config(relief=RAISED)
    btn_tns.config(relief=RAISED)
    btn_vocab.config(relief=RAISED)
    btn_art.config(fg='orange')
    btn_tobe.config(fg='black')
    btn_tns.config(fg='black')
    btn_vocab.config(fg='black')

def tns():
    '''This function is called to depict Rock and Morty quotes 
    on 'tenses' topic; it changes the font color of 'quote lable' to 
    'khaki', it nulls the 'check message', configurates the 'task lable'
    and randomly depicts the quote'''
    global text
    global tobe_btn_state
    global art_btn_state
    global vocab_btn_state
    global tenses_btn_state
    tobe_btn_state = False
    art_btn_state = False
    tenses_btn_state = True
    vocab_btn_state = False
    endings_lst = ['-ed','-ing']
    text = random.choice(list(tenses))
    labl.config(text=text,font=("bold",20),fg='khaki')
    labl1.config(text="",)
    labl2.config(text = "Choose -ed or -ing ending:")
    spnb.config(value = endings_lst)
    btn_art.config(relief=RAISED)
    btn_tobe.config(relief=RAISED)
    btn_tns.config(relief=SUNKEN)
    btn_vocab.config(relief=RAISED)
    btn_art.config(fg='black')
    btn_tobe.config(fg='black')
    btn_tns.config(fg='orange')
    btn_vocab.config(fg='black')

def voc():
    '''This function is called to depict Rock and Morty quotes 
    on 'vocabulary' topic; it changes the font color of 'quote lable' to 
    'linen', it nulls the 'check message', configurates the 'task lable'
    and randomly depicts the quote'''
    global text
    global tobe_btn_state
    global art_btn_state
    global vocab_btn_state
    global tenses_btn_state
    tobe_btn_state = False
    art_btn_state = False
    tenses_btn_state = False
    vocab_btn_state = True
    vocab_lst = ['out', 'for', 'up', 'in', 'down']
    text = random.choice(list(vocab))
    labl.config(text=text,font=("bold",20),fg='linen')
    labl1.config(text="",)
    labl2.config(text = "Choose the right preposition:")
    spnb.config(value = vocab_lst)
    btn_art.config(relief=RAISED)
    btn_tobe.config(relief=RAISED)
    btn_tns.config(relief=RAISED)
    btn_vocab.config(relief=SUNKEN)
    btn_art.config(fg='black')
    btn_tobe.config(fg='black')
    btn_tns.config(fg='black')
    btn_vocab.config(fg='maroon')

def nxt():
    ''' This function is aimed to change the quote inside the 
    chosen topic '''
    global text
    if tobe_btn_state:
        text = random.choice(list(to_be))
        labl.config(text=text,font=("bold",20))
        labl1.config(text="",)
    elif art_btn_state:
        text = random.choice(list(articles))
        labl.config(text=text,font=("bold",20))
        labl1.config(text="",)
    elif tenses_btn_state:
        text = random.choice(list(tenses))
        labl.config(text=text,font=("bold",20))
        labl1.config(text="",)
    elif vocab_btn_state:
        text = random.choice(list(vocab))
        labl.config(text=text,font=("bold",20))
        labl1.config(text="",)

r_answers = 0
w_answers = 0
def check():
    ''' This is the function to check the user's answer.
    It recives the value from the variable of a Spinbox and
    checks whether it corresponds with the value of corresponding
    key in chosen dictionary. In case of coinsidance it shows up the 
    appropriate 'right/wrong' notice. It also counts the amount of correct
    ans wrond answers. '''
    global r_answers
    global w_answers
    value = var.get()
    key = text
    if tobe_btn_state:
        if key in to_be and value == to_be[text]:
            r_answers +=1
            labl1.config(text="Well done!",font=("bold",16),fg='green')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
        else:
            w_answers +=1
            labl1.config(text="Nope!",font=("bold",16),fg='red')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
    elif art_btn_state:
        if key in articles and value == articles[text]:
            r_answers +=1
            labl1.config(text="Well done!",font=("bold",16),fg='green')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
        else:
            w_answers +=1
            labl1.config(text="Nope!",font=("bold",16),fg='red')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
    elif tenses_btn_state:
        if key in tenses and value == tenses[text]:
            r_answers +=1
            labl1.config(text="Well done!",font=("bold",16),fg='green')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
        else:
            w_answers +=1
            labl1.config(text="Nope!",font=("bold",16),fg='red')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
    elif vocab_btn_state:
        if key in vocab and value == vocab[text]:
            r_answers +=1
            labl1.config(text="Well done!",font=("bold",16),fg='green')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")
        else:
            w_answers +=1
            labl1.config(text="Nope!",font=("bold",16),fg='red')
            labl3.config(text = f"Score Counter\nCorrect: {r_answers}\nWrong: {w_answers}")


to_be = {"I ... sorry, but your opinion means very little to me. – Rick": "am", 
"Nobody exists on purpose. Nobody belongs anywhere. \nWe ... all going to die. Come watch TV.  – Morty": "are", 
"Life ... effort and I’ll stop when I die! - Jerry": "is", 
"I ... tell you how I feel about school, Jerry: \nit’s a waste of time.": "will",
"'Dad, ... I evil?' 'Worse. You’re smart.'": "am",
"It ... a new machine. It detects stuff \nall the way up your butt.":"is",
"That’s it! That’s it, Rick! I ... taking the wheel!": "am",
"I ...n't born into the God business, I fucking earned it.": "was", 
"When you know nothing matters, \nthe universe is yours. And I’ve never met \na universe that ... into it.": "was", 
"There is no god, Summer;\n gotta rip that band-aid off now you ... thank me later.": "will",
"Concentrated dark matter? \nThey ... asking about that in class.":"were",
"Weddings ... basically funerals with cake. - Rick":"are",
"Do not call me that! Snuffles ... my slave name. \nYou shall now call me Snowball, \nbecause my fur is pretty and white.":"was"}
articles = {"I think you have to think ahead and live in ... moment.":"the", 
"There's a lesson here and \nI'm not going to be ... one to figure it out.": "the",
"Rick, I don't like glowing rocks in ... kitchen trash!":"the",
"Morty, I'm ... drunk, not ... hack.":"a",
"Can somebody just let me out of here?\nIf I die in ... cage I lose ... bet.": "a",
"I can't wait to watch your \nadventure lay ... huge fart.":"a",
"Don't break ... arm jerking yourself off, Morty.":"an",
"To live is to risk it all, otherwise you're just ... inert chunk \nof randomly assembled molecules drifting \nwherever the universe blows you.":"an"}
tenses = {"That’s it! That’s it, Rick! \nI’m (take) the wheel!":"-ing", 
"I’m not staring at you. \nI’m (take) your mugshot.":"-ing",
"How do you feel about all the \ninnocent people that are (die) because of your choices?":"-ing",
"Is evil real, and if so, \ncan it be (measure)?":"-ed",
"Boom! Big reveal! \nI (turn) myself into a pickle!":"-ed",}
vocab = {"Hey, muchacho, does your planet \nhave wiper fluid yet or you gonna \nfreak ... and start worshipping us?":"out",
"Holy cow, Rick! I didn't \nknow hanging ... with you was making me smarter!":"out",
"Get ... of my head.":"out",
"Dad, I'm ... of excuses to not be who I am. \nSo who am I? What do I do?":"out",
"You sell weapons to killers ... money?":"for",
"Oh, these guys are looking ... us now. \nEarth will be swarming with them.":"for",
"You do your thing, but I can't afford \nto get my pride wrapped ... in your shame. \nYou know what I'm saying?":"up",
"I mean one of these days, you know, \nyou're gonna—you're gonna—you're \ngonna end ... seeing something.":"up",
"How about next time you be ... charge, \nand then we'll talk about how simple and fun it is?":"in",
"Grandpa goes around and he does his \nbusiness ... public, because Grandpa isn't shady.":"in",
"So you're trapped ... there and you can only \ncome out in the form of Tiny Rick's teen angst!":"in",
"Take it easy. This is \na blessing ... disguise.":"in",
"I think you should put ... the gun \nand we should get you to a doctor.":"down",
"Here's the adventure: some kind of alien \nhas infested the Kennedy Sex Tunnels. \nI want it hunted ... and taken out.":"down",}

wnd = Tk()
wnd.title("Rick_and_Morty_Grammar (by St.Polishchuk)")
wnd.resizable(0,0)

frm1 = Frame(wnd)
frm1.pack()
frm2 = Frame(wnd)
frm2.pack()
frm3 = Frame(wnd)
frm3.pack()
frm0 = Frame(wnd)
frm0.pack()
frm4 = Frame()
frm4.pack()
frm5 = Frame()
frm5.pack()

labl = Label(frm1,width=50, bg = 'grey')
labl.pack()

labl1 = Label(frm2)
labl1.pack()

labl2 = Label(frm2,font=('italics',14))
labl2.pack()

labl3 = Label(frm5,font=('italics',14))
labl3.pack()

labl0 = Label(frm0, text = "Choose category:", font=('italics',14))
labl0.pack()

var = StringVar()
spnb = Spinbox(frm2,textvariable=var,font=('italics',14))
spnb.pack()

btn = Button(frm3,width=15,height=1,text="Next",command=nxt,
activeforeground='green',font=('italics',14))
btn.grid(row=0,column=0,pady=5)

btn_check = Button(frm3,width=15,height=1,text="Check", command = check,
activeforeground='red',font=('italics',14))
btn_check.grid(row=0,column=1,pady=5)

btn_tobe = Button(frm4,width=15,height=1,text="VERB 'TO BE'", command = tobe,
activeforeground='green',font=('underlined',14))
btn_tobe.grid(row=0,column=0,pady=5)

btn_art = Button(frm4,width=15,height=1,text="ARTICLES", command = art,
activeforeground='green',font=('underlined',14))
btn_art.grid(row=0,column=1,pady=5)

btn_tns = Button(frm4,width=15,height=1,text="TENSES", command = tns,
activeforeground='green',font=('underlined',14))
btn_tns.grid(row=1,column=0,pady=5)

btn_vocab = Button(frm4,width=15,height=1,text="VOCABULARY", command = voc,
activeforeground='green',font=('underlined',14))
btn_vocab.grid(row=1,column=1,pady=5)

wnd.mainloop()