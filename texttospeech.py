import gtts
from playsound import playsound
from tkinter import *

window=Tk()

text=StringVar()

def listen():
    a=text.get()
    tts=gtts.gTTS(a)
    tts.save("hellow.mp3")

    playsound("hellow.mp3")

photo=PhotoImage(file=r"img.png")
photoimage=photo.subsample(15,20)


L1=Label(window,text="enter the word to be spoken")
L1.grid(row=0,column=0)


E1=Entry(window,textvariable=text)
E1.grid(row=0,column=1)

B1=Button(window,text="listen",image=photoimage,compound=BOTTOM,command=listen)
B1.grid(row=1,column=0)



window.mainloop()
