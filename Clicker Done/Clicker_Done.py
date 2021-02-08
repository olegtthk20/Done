from tkinter import *
import time
from tkinter.messagebox import *

root=Tk()
root.geometry('500x700')
M=Menu(root)
root.config(menu=M)

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()

def info():
    print("Double click purchases need 100 clicks!")

info()

click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")

def Plus_1():
    global click
    global mult
    if click < 100:
        print("Not enough clicks! It Costs 100")
        blankLine()
    elif click >= 100:
        mult = mult+1
        click = click - 100
        showinfo("Upgrader","Message: +1 Clicks Purchased!")
        blankLine()

def Plus_5():
    global click
    global mult
    if click < 1000:
        print("Not enough clicks! It Costs 1k")
        blankLine()
    elif click >= 1000:
        mult = mult+5
        click = click - 1000
        showinfo("Upgrader","Message: +5 Clicks Purchased!")
        blankLine()

def Plus_10():
    global click
    global mult
    if click < 5000:
        print("Not enough clicks! It Costs 5k")
        blankLine()
    elif click >= 5000:
        mult = mult+10
        click = click - 5000
        showinfo("Upgrader","Message: +10 Clicks Purchased!")
        blankLine()

def Plus_20():
    global click
    global mult
    if click < 10000:
        print("Not enough clicks! It Costs 10k")
        blankLine()
    elif click >= 10000:
        mult = mult+20
        click = click - 10000
        showinfo("Upgrader","Message: +20 Clicks Purchased!")
        blankLine()

def Plus_50():
    global click
    global mult
    if click < 20000:
        print("Not enough clicks! It Costs 20k")
        blankLine()
    elif click >= 20000:
        mult = mult+50
        click = click - 20000
        showinfo("Upgrader","Message: +50 Clicks Purchased!")
        blankLine()

def Plus_100():
    global click
    global mult
    if click < 50000:
        print("Not enough clicks! It Costs 50k")
        blankLine()
    elif click >= 50000:
        mult = mult+100
        click = click - 50000
        showinfo("Upgrader","Message: +100 Clicks Purchased!")
        blankLine()

def Plus_200():
    global click
    global mult
    if click < 100000:
        print("Not enough clicks! It Costs 100k")
        blankLine()
    elif click >= 100000:
        mult = mult+200
        click = click - 100000
        showinfo("Upgrader","Message: +200 Clicks Purchased!")
        blankLine()

def Plus_500():
    global click
    global mult
    if click < 200000:
        print("Not enough clicks! It Costs 200k")
        blankLine()
    elif click >= 200000:
        mult = mult+500
        click = click - 200000
        showinfo("Upgrader","Message: +500 Clicks Purchased!")
        blankLine()

def Plus_1000():
    global click
    global mult
    if click < 500000:
        print("Not enough clicks! It Costs 500k")
        blankLine()
    elif click >= 500000:
        mult = mult+1000
        click = click - 500000
        showinfo("Upgrader","Message: +1000 Clicks Purchased!")
        blankLine()

def Doubler():
    global click
    global mult
    if click < 1000000:
        print("Not enough clicks! It Costs 1 Mil")
        blankLine()
    elif click >= 1000000:
        mult = mult * 2
        click = click - 1000000
        showinfo("Upgrader","Message: Double Clicks Purchased!")
        blankLine()

def count():
    global click
    global mult
    click += mult 
    entry.delete(0, 'end')
    entry.insert(0,click)
    if click == 200:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS 100 Clicks')
        click += 100

    elif click == 1000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS 200 Clicks')
        click += 200

    elif click == 5000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS 1000 Clicks')
        click += 1000

    elif click == 9000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS 4000 Clicks')
        click+= 4000

    elif click == 25000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS x2 Clicks')
        mult = mult * 2

    elif click == 25000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS x3 Clicks')
        mult = mult * 3

    elif click == 500000:
        showinfo('Achievements','Message: Achievement Unlocked: Junior Clicker! BONUS +100000 Clicks')
        click += 100000


root.title("Clicker! v0.1")

m1=Menu(M,tearoff=0)
M.add_cascade(label='Click Upgrader', menu=m1)
m1.add_command(label='+1 points per click',command=lambda:Plus_1())
m1.add_command(label='+5 points per click',command=lambda:Plus_5())
m1.add_command(label='+10 points per click',command=lambda:Plus_10())
m1.add_command(label='+20 points per click',command=lambda:Plus_20())
m1.add_command(label='+50 points per click',command=lambda:Plus_50())
m1.add_command(label='+100 points per click',command=lambda:Plus_100())
m1.add_command(label='+200 points per click',command=lambda:Plus_200())
m1.add_command(label='+500 points per click',command=lambda:Plus_500())
m1.add_command(label='+1000 points per click',command=lambda:Plus_1000())
m1.add_command(label='Double points per click',command=lambda:Doubler())
button = Button(text="CLICK",command=lambda:count())
label = Label(text="SCORE",font = 'arial 20',bg = 'red')
entry = Entry(root)
label.pack(side = TOP , pady = 5)
entry.pack(side = TOP , pady = 5)
button.pack(side=TOP , pady = 5)
root.mainloop()