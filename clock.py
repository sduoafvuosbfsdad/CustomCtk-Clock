import time
import datetime
import threading
import customtkinter as ctk

golden_ratio = 1.618

window = ctk.CTk(fg_color = '#3A3A3A')
window.geometry(f'{80*11}x{80*6}')

frame = ctk.CTkFrame(window, fg_color = 'transparent')

class NumberFrame(ctk.CTkFrame):
    def __init__(self, parent):
        width = 125
        super().__init__(parent, width = width, height = int(width * 1.5), fg_color = '#2F2F2F', corner_radius = 20)
        self.number = ctk.StringVar()
        self.number.set('0')
        ctk.CTkLabel(
            self,
            textvariable = self.number,
            font = ctk.CTkFont(
                'Consolas',
                size = width+25,
                weight = 'bold'
            )
        ).place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

class IntervalFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'transparent')
        ctk.CTkFrame(
            self,
            width=20,
            height=20,
            fg_color='#dce4ee',
            corner_radius=10,
        ).grid(row = 0, column = 0, sticky = ctk.NSEW, padx = 5, pady = 3)
        ctk.CTkFrame(
            self,
            width=20,
            height=20,
            fg_color='#dce4ee',
            corner_radius=10,
        ).grid(row = 1, column = 0, sticky = ctk.NSEW, padx = 5, pady = 3)

Tens_Hour = NumberFrame(frame)
Ones_Hour = NumberFrame(frame)
Hour_Minute_Interval = IntervalFrame(frame)
Tens_Minutes = NumberFrame(frame)
Ones_Minutes = NumberFrame(frame)
Minute_Second_Interval = IntervalFrame(frame)
Tens_Seconds = NumberFrame(frame)
Ones_Seconds = NumberFrame(frame)
Date = ctk.StringVar()
ctk.CTkLabel(
    frame,
    textvariable = Date,
    font = ctk.CTkFont(
        'Consolas',
        30,
        'bold'
    )
).grid(row = 1, column = 0, columnspan = 8, sticky = ctk.NSEW)

def update_time():
    while True:
        now = datetime.datetime.now()
        string_time = now.strftime('%H%M%S')
        Tens_Hour.number.set(string_time[0])
        Ones_Hour.number.set(string_time[1])
        Tens_Minutes.number.set(string_time[2])
        Ones_Minutes.number.set(string_time[3])
        Tens_Seconds.number.set(string_time[4])
        Ones_Seconds.number.set(string_time[5])

        Date.set(datetime.datetime.now().strftime('%d %B %Y, %A'))

        time.sleep(0.1)

Tens_Hour.grid(row = 0, column = 0, padx = 5, pady = 10)
Ones_Hour.grid(row = 0, column = 1, padx = 5, pady = 10)
Hour_Minute_Interval.grid(row = 0, column = 2)
Tens_Minutes.grid(row = 0, column = 3, padx = 5, pady = 10)
Ones_Minutes.grid(row = 0, column = 4, padx = 5, pady = 10)
Minute_Second_Interval.grid(row = 0, column = 5)
Tens_Seconds.grid(row = 0, column = 6, padx = 5, pady = 10)
Ones_Seconds.grid(row = 0, column = 7, padx = 5, pady = 10)


frame.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)

threading.Thread(target = update_time).start()
window.mainloop()