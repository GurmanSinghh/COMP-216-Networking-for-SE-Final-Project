from tkinter import *
from data_generator import temperature_day_records

class Gauge(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()
         
    def initUI(self, temperature = 15):
        
        self.master.title('Thermometer')
        self.pack(fill=BOTH, expand=1)
        temperatureList = ['50°C','40°C','30°C','20°C','10°C','0°C','10°C','20°C','30°C']
        canvas = Canvas(self)
        
        # draw oval
        canvas.create_oval(100, 100,   #top left
        500, 500,                      #bottom right
        outline='#f11', fill='#1f1', width=2)
         
        # draw mark
        canvas.create_line(100, 300, 120, 300,width=3)
        canvas.create_text(130, 300, anchor=W, font='Purisa', text='-20°C')
        
        canvas.create_line(300, 100, 300, 120,width=3)
        canvas.create_text(300, 130, anchor=W, font='Purisa', text='0°C')
        
        canvas.create_line(480, 300, 500, 300,width=3)
        canvas.create_text(430, 300, anchor=W, font='Purisa', text='20°C')
        
        canvas.create_line(159, 441, 179, 421,width=3)
        canvas.create_text(182, 413, anchor=W, font='Purisa', text='-30°C')
        
        canvas.create_line(441, 441, 421, 421,width=3)
        canvas.create_text(401, 411, anchor=W, font='Purisa', text='30°C')
        
        canvas.create_line(159, 159, 179, 179,width=3)
        canvas.create_text(189, 189, anchor=W, font='Purisa', text='-10°C')
        
        canvas.create_line(441, 159, 421, 179,width=3)
        canvas.create_text(401, 189, anchor=W, font='Purisa', text='10°C')
        
        # draw arc
        angle = 90 - (temperature / 80)*360
        self.arc = canvas.create_arc(100, 100,    #top left
        500, 500,                      #bottom right
        start = angle, extent=0,          #start angle how far to go
        outline='#77f', fill='blue', width=2)
        canvas.pack(fill=BOTH, expand=1)
        
        # input temperature
        canvas.create_text(10, 60, anchor=W, font='Purisa', text='Input current temperature')
        e1 = Entry(canvas)
        canvas.create_window(130,80,window=e1)
        
        # refresh temperature
        button1 = Button(self, text = "Refresh", command = lambda: canvas.itemconfig(self.arc,start = 90 - (int(e1.get()) / 80)*360), anchor = W)
        button1_window = canvas.create_window(100, 100, anchor=NW, window=button1)
        
root = Tk()
Gauge = Gauge()
root.geometry('600x600')
root.mainloop()
