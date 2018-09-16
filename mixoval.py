from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.geometry("800x600")
root.title("Color Mixing Guide")
canvas = Canvas(root, bg="Pale Green", height=600, width=800)


def colormix():
    primecolor = ["red","blue","yellow","black","white"]
    random.shuffle(primecolor)
    print (primecolor)

    oval1 = canvas.create_oval(150, 50, 350, 250,fill = primecolor[0])
    oval2 = canvas.create_oval(450, 50, 650, 250,fill = primecolor[1])

    leb2 = Label(root,text = "+" , font = " none 100",bg = "Pale Green",fg = "black").place(x = 360,y = 80)
    
    answer = []
    if primecolor[0] == "red":
        if primecolor[1] == "blue":
            answer.append ("Purple")
        elif primecolor[1] == "yellow":
            answer.append ("Orange")
        elif primecolor[1] == "black":
            answer.append ("Firebrick")
        elif primecolor[1] == "white":
            answer.append ("Pink")
    elif primecolor[0] == "blue":
        if primecolor[1] == "red":
            answer.append ("Purple")
        elif primecolor[1] == "yellow":
            answer.append ("Green")
        elif primecolor[1] == "black":
            answer.append ("Navy")
        elif primecolor[1] == "white":
            answer.append ("Sky Blue")
    elif primecolor[0] == "yellow":
        if primecolor[1] == "red":
            answer.append ("Orange")
        elif primecolor[1] == "blue":
            answer.append ("Green")
        elif primecolor[1] == "black":
            answer.append ("Dark Goldenrod")
        elif primecolor[1] == "white":
            answer.append ("Pale Goldenrod")
    elif primecolor[0] == "black":
        if primecolor[1] == "red":
            answer.append ("Firebrick")
        elif primecolor[1] == "yellow":
            answer.append ("Dark Goldenrod")
        elif primecolor[1] == "blue":
            answer.append ("Navy")
        elif primecolor[1] == "white":
            answer.append ("Grey")
    elif primecolor[0] == "white":
        if primecolor[1] == "red":
            answer.append ("Pink")
        elif primecolor[1] == "yellow":
            answer.append ("Pale Goldenrod")
        elif primecolor[1] == "blue":
            answer.append ("Sky Blue")
        elif primecolor[1] == "black":
            answer.append ("Grey")
        
    leb = Label(root,text = "=" , font = " none 100",bg = "Pale Green",fg = "Black").place(x = 150,y = 300)    
    #leb1 = Label(root,text = answer[0] , font = " none 300",bg = "Pale Green",fg = "Pale Green").place(x = 100,y = 300)
    #leb2 = Label(root,text = answer[0] , font = " none 70",bg = "Pale Green",fg = answer[0]).place(x = 100,y = 300)
    oval1 = canvas.create_oval(300, 300, 500, 500,fill = answer[0])
    print(primecolor[0])
    canvas.pack()

    
    nextbutt2 = ttk.Button(root, text="Next", command=colormix).place(x = 700,y = 530)

nextbutt1 = ttk.Button(root, text="Start",command=colormix).place(x = 700,y = 530)

root.mainloop()
