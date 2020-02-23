from calendar import *
from tkinter import *

wnd = Tk()
wnd.title("Dates_Selector by St.Polishchuk")
wnd.geometry("370x450")
wnd.resizable(0,0)

frm1 = Frame(wnd,pady=5, padx=5)
frm1.grid(row=0,column=0)
frm3 = Frame(wnd)
frm3.grid(row=2)
frm2 = Frame(wnd,pady=5)
frm2.grid(row=1,column=0)

# Produses the output in Text widget 
# 1 line: month
# 2 line: weekday name
# 3 line: selected dates
def dates():
    months = {'January':1, 'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,
    'Septemper':9,'October':10, 'November':11, 'December':12}
    yy = year.get()
    mm = months[month.get()]

    cl = Calendar(0).monthdayscalendar(yy,mm)
    mnth = month_name[mm]
    mnthnm = "                 {0:20}".format(mnth)
    txt.insert(INSERT,mnthnm + '\n')

    ''' this piece assigns weekdays'''
    weekdays = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thurdsay':3, 'Friday':4, 'Saturday':5, 'Sunday':6}

    d1 = weekdays[day1.get()]
    d2= weekdays[day2.get()]
    d3 = weekdays[day3.get()]
    
    a = day_abbr[d1]
    b = day_abbr[d2]
    c = day_abbr[d3]
    days = "    {0:10}{1:10}{2:10}".format(a,b,c)
    txt.insert(INSERT, days + '\n')

    '''this loop prints out the dates'''
    for x in cl[0:5]:
        if x[d1] == 0:
            print("")
        else:
            ds = "{0:10}{1:10}{2:10}".format(x[d1],x[d2],x[d3])
            txt.insert(INSERT, ds) 
            txt.insert(INSERT, '\n')
            
#Delets the output in Text widget
def clear():
    txt.delete('1.0', END)



txt = Text(frm2,width=30,height=10,bg = 'grey', foreground='white',font = ('bold',14), borderwidth=2, relief='solid')
txt.pack()

scroll = Scrollbar(frm2, orient=VERTICAL, command=txt.yview)
txt['yscroll'] = scroll.set

scroll.pack(side="right", fill="y")
txt.pack(side="left", fill="both", expand=True)

yearlabel = Label(frm1,text="Choose year: ", font = ('Times New Roman',14))
yearlabel.grid(row=0,column=0)

year = IntVar()
spnb = Spinbox(frm1, from_=2018, to_=2025,textvariable=year,font = ('Times New Roman',14))
spnb.grid(row=0,column=1)

monthlabel = Label(frm1,text="Choose month: ", font = ('Times New Roman',14))
monthlabel.grid(row=1,column=0)

months = ['January', 'February','March','April','May','June','July','August',
'Septemper','October', 'November', 'December']
month = StringVar()
spnb = Spinbox(frm1, values=months,textvariable=month,font = ('Times New Roman',14))
spnb.grid(row=1,column=1)

daylabel = Label(frm1, text="Choose weekdays:", font = ('Times New Roman',14))
daylabel.grid(row=3,column=0)

day1 = StringVar()
day2 = StringVar()
day3 = StringVar()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thurdsay', 'Friday', 'Saturday', 'Sunday']

spb1 = Spinbox(frm1, value=weekdays, textvariable=day1,font = ('Times New Roman',14))
spb1.grid(row=4,column=1,padx=10)

spb2 = Spinbox(frm1, value=weekdays,textvariable=day2,font = ('Times New Roman',14))
spb2.grid(row=5,column=1,padx=10)

spb3 = Spinbox(frm1, value=weekdays,textvariable=day3,font = ('Times New Roman',14))
spb3.grid(row=6,column=1,padx=10)

showdates = Button(frm3,command = dates,text="Show dates", font = ('Times New Roman',12), activeforeground='green',width=15)
showdates.grid(row=0,column=1, pady=10)

clear = Button(frm3,command = clear,text="Clear", font = ('Times New Roman',12), activeforeground='red',width=15)
clear.grid(row=0,column=0, pady=10)

wnd.mainloop()