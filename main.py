from tkinter import *


root = Tk()
root.config(background='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
root.title('Calculatrice')
root.geometry("800x600+20+20")

numericEq = StringVar()
calcValue = ""
dataField = Entry(root, textvariable=numericEq, font="Serif 15")
dataField.grid(row=0,columnspan=3, ipadx=80, ipady=15)

def btn_click(x):
    global calcValue
    calcValue = calcValue + str(x)
    numericEq.set(calcValue)

def clearInput():
    global calcValue
    calcValue = ""
    numericEq.set("")

def btn_equal():
    global calcValue
    somme = eval(calcValue)
    total = str(somme)
    numericEq.set(total)

button1 = Button(root, text="1", width=5, height=3, command=lambda: btn_click(1))
button2 = Button(root, text="2", width=5, height=3, command=lambda: btn_click(2))
button3 = Button(root, text="3", width=5, height=3, command=lambda: btn_click(3))
button4 = Button(root, text="4", width=5, height=3, command=lambda: btn_click(4))
button5 = Button(root, text="5", width=5, height=3, command=lambda: btn_click(5))
button6 = Button(root, text="6", width=5, height=3, command=lambda: btn_click(6))
button7 = Button(root, text="7", width=5, height=3, command=lambda: btn_click(7))
button8 = Button(root, text="8", width=5, height=3, command=lambda: btn_click(8))
button9 = Button(root, text="9", width=5, height=3, command=lambda: btn_click(9))
button0 = Button(root, text="0", width=10, height=3, command=lambda: btn_click(0))
button_dot = Button(root, text=".", width=5, height=3, command=lambda: btn_click("."))

button_plus = Button(root, text="+", width=5, height=7, command=lambda: btn_click("+"))
button_less = Button(root, text="-", width=5, height=3, command=lambda: btn_click("-"))
button_mult = Button(root, text="*", width=5, height=3, command=lambda: btn_click("*"))
button_div = Button(root, text="/", width=5, height=3, command=lambda: btn_click("/"))

button_mod = Button(root, text="%", width=5, height=3, command=lambda: btn_click("%"))
button_sum = Button(root, text="=", width=5, height=6, command=lambda: btn_equal())
button_clear = Button(root, text="C", width=5, height=3, command=lambda: clearInput())

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=5, column=0, columnspan=2)
button_dot.grid(row=4, column=2)


button_plus.grid(row=2, column=3, rowspan=2)
button_less.grid(row=1, column=3)
button_mult.grid(row=1, column=2)
button_div.grid(row=1, column=1)

button_mod.grid(row=1, column=0)
button_sum.grid(row=4, column=3, rowspan=2)
button_clear.grid(row=1, column=4)

root.mainloop()

"""class calc():
    def __init__(self):
        self.expression = 0
        self.operator = ' '
        self.

    def choicenum(self):
        input_text() = expression"""




