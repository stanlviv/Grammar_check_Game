from tkinter import *
import pyowm
from pyowm import timeutils

api = "3f152ae62a9f057cdb1a9851e3b676cd"
owm = pyowm.OWM("3f152ae62a9f057cdb1a9851e3b676cd", language='ua')
class Weather:
    def __init__(self, city):
        self.city = city
    def show_weather(self):
        try:
            point = owm.weather_at_place(self.city)
            p_n = point.get_location()
            point_name = p_n.get_name()
            place = point.get_weather()
            place_temp = place.get_temperature('celsius')
            place_hum = place.get_humidity()
            place_wind = place.get_wind()
            place_status = place.get_detailed_status() 
            result = f"{place_status.capitalize()} у місті {point_name}.\nТемпература: {place_temp['temp']}°C\nmax: {place_temp['temp_max']} min: {place_temp['temp_min']}\nВологість: {place_hum}%\nШвидкість вітру: {place_wind['speed']}"
            lbl2.config(text = result)
        except Exception as ex:
            lbl2.config(text = f"Вкажіть вірну назву!")
    def show_forecast(self):
        try:
            place = owm.three_hours_forecast(self.city)
            tomorrow9 = timeutils.tomorrow(9)
            tomorrow12 = timeutils.tomorrow(12)
            tomorrow18 = timeutils.tomorrow(18)
            t9 = place.get_weather_at(tomorrow9)
            t12 = place.get_weather_at(tomorrow12)
            t18 = place.get_weather_at(tomorrow18)
            temp9 = t9.get_temperature('celsius')['temp']
            temp12 = t12.get_temperature('celsius')['temp']
            temp18 = t18.get_temperature('celsius')['temp']
            if place.will_be_rainy_at(tomorrow12):
                rain = 'Дощитиме'
            else: 
                rain = 'Буде сухо'
            if place.will_be_sunny_at(tomorrow12):
                sun = 'та сонячно.'
            else: sun = 'та хмарно.'
            lbl2.config(text=f"{rain} {sun}\n9:00 - {temp9}℃\n12:00 - {temp12}℃\n18:00 - {temp18}℃")
        except Exception as ex:
            lbl2.config(text = f"Вкажіть вірну назву!")

def show_fc():
    town = var.get()
    city = Weather(town)
    city.show_forecast()

def show():
    town = var.get()
    city = Weather(town)
    city.show_weather()


wnd = Tk()
wnd.title('Weather by St.Polishchuk')

frm1 = Frame(wnd)
frm1.grid(row = 0, column = 0,pady=5, padx=5)

frm2 = Frame(wnd)
frm2.grid(row = 1, column = 0,pady=5, padx=5)

lbl1 = Label(frm1, text = 'Де шукати?', font=('Arial', 12))
lbl1.grid(row = 0, column = 0,pady=5, padx=5)

var = StringVar()
entry = Entry(frm1, textvariable = var, width = 15)
entry.grid(row = 0, column = 1,pady=5, padx=5)

btn = Button(frm1, text = 'Сьогодні', command = show, activeforeground='green')
btn.grid(row = 0, column = 2,pady=5, padx=5)

btn2 = Button(frm1, text = 'Завтра', command=show_fc, activeforeground='green')
btn2.grid(row = 0, column = 3,pady=5, padx=5)

lbl2 = Label(frm2, font=('Arial', 16), fg='darkgreen', height=5)
lbl2.grid(row = 0, column = 0,pady=5, padx=5)

wnd.mainloop()