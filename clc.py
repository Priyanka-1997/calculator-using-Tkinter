from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Calculator")
root.configure(bg="dark grey")

root.resizable(width=False, height=False)

operator = ""
scvalue = StringVar()
# scvalue.set("")


def button_click(number):
     global operator
     operator=operator+str(number)
     scvalue.set(operator)


def button_eqal():
    global operator
    add = str(eval(operator))
    scvalue.set(add)
    operator = ""


def button_eqal():
    global operator
    sub = str(eval(operator))
    scvalue.set(sub)
    operator = ""


def button_eqal():
    global operator
    mul = str(eval(operator))
    scvalue.set(mul)
    operator = ""


def button_eqal():
    global operator
    div = str(eval(operator))
    scvalue.set(div)
    operator = ""


def button_clear():
    screen.delete(0, END)

screen = Entry(root, textvar=scvalue, font=("lucida", 20, "bold"), bd=5)
screen.pack(fill=X, ipadx=18, pady=12, padx=10)



b1 = Button(root, text="9", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(9))
b1.place(x=20, y=65)

b2 = Button(root, text="8", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(8))
b2.place(x=90, y=65)

b3 = Button(root, text="7", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(7))
b3.place(x=160, y=65)

b4 = Button(root, text="-", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click("-"))
b4.place(x=230, y=65)

b5 = Button(root, text="6",  padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(6))
b5.place(x=20, y=150)

b6 = Button(root, text="5", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(5))
b6.place(x=90, y=150)

b7 = Button(root, text="4", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(4))
b7.place(x=160, y=150)

b8 = Button(root, text="/", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click("/"))
b8.place(x=230, y=150)

b9 = Button(root, text="3", padx=10, pady=10,
            font="lucida 20 bold", command=lambda: button_click(3))
b9.place(x=20, y=235)

b10 = Button(root, text="2", padx=10, pady=10,
             font="lucida 20 bold", command=lambda: button_click(2))
b10.place(x=90, y=235)

b11 = Button(root, text="1", padx=10, pady=10,
             font="lucida 20 bold", command=lambda: button_click(1))
b11.place(x=160, y=235)

b12 = Button(root, text="=", padx=6, pady=10,
             font="lucida 20 bold", command=lambda: button_eqal())
b12.place(x=230, y=235)

b13 = Button(root, text="0", padx=10, pady=10,
             font="lucida 20 bold", command=lambda: button_click(0))
b13.place(x=20, y=315)

b14 = Button(root, text="+", padx=10, pady=10,
             font="lucida 20 bold", command=lambda: button_click("+"))
b14.place(x=90, y=315)

b15 = Button(root, text="X", padx=10, pady=10,
             font="lucida 20 bold", command=lambda: button_click("x"))
b15.place(x=160, y=315)

b16 = Button(root, text="C", padx=5, pady=10,
             font="lucida 20 bold", command=button_clear)
b16.place(x=230, y=315)


root.mainloop()
