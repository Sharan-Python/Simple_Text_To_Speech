from tkinter import *
from tkinter import ttk
import pyttsx3
win=Tk()
win.geometry('800x180')
win.title("Text to Speech")
text = Entry(win, width=100, bg="White")
text.place(x=180, y=30)
but1 = ttk.Button(win, text="Speak", command=lambda: buttonpressed(1))
but1.grid(row=0, column=0, ipadx=50, ipady=50)


def buttonpressed(buttonnumber):
    if buttonnumber == 1:
        friend = pyttsx3.init()
        friend.say(text.get())
        friend.runAndWait()
win.mainloop()
