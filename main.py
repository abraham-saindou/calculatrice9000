# importing tkinter library
from tkinter import *

# setting parameters of the user interface
root = Tk()
root.config(background='white')
root.resizable(width=False, height=False)
root.geometry("474x317")
root.title('Calculatrice')

# storing data input by user and creating array to display it
numericEq = StringVar()
calcValue = ""
dataField = Entry(root, textvariable=numericEq, font="Serif 15", bg="grey", width=32)
dataField.grid(row=0, columnspan=5, rowspan=2)

# an empty list to store the result, use to display historic
historique = []


def btn_click(x):
    global calcValue
    calcValue = calcValue + str(x)  # str() converts int type into string, then add is added to calcValue
    numericEq.set(calcValue)


def btn_click2():  #square root function
    global calcValue
    calcValue = str(float(numericEq.get())**0.5)
    numericEq.set(calcValue)


def btn_click3():  #square function
    global calcValue
    calcValue = str(float(numericEq.get())**2)
    numericEq.set(calcValue)


def clearInput():  # clear function
    global calcValue
    calcValue = ""
    numericEq.set("")


def btn_equal():  # function calculating result
    global calcValue
    global historique

    total = str(eval(calcValue))
    numericEq.set(total)
    calcValue = total
    historique.append(calcValue)

    # initializing a listbox to display historic
    histon = Listbox(root, width=13, height=15, listvariable=historique)
    histon.place(x=362, y=2)
    for x in historique:
        y = x
        histon.insert(0, y)


# line 1
button_mod = Button(root, text="%", width=5, height=2, command=lambda: btn_click("%"))
button_mod.grid(row=2, column=0, pady=2)
button_div = Button(root, text="/", width=5, height=2, command=lambda: btn_click("/"))
button_div.grid(row=2, column=1, pady=2)
button_mult = Button(root, text="*", width=5, height=2, command=lambda: btn_click("*"))
button_mult.grid(row=2, column=2, pady=2)
button_less = Button(root, text="-", width=5, height=2, command=lambda: btn_click("-"))
button_less.grid(row=2, column=3, pady=2)
button_clear = Button(root, text="C", width=5, height=2, command=lambda: clearInput())
button_clear.grid(row=2, column=4, pady=2)

# line 2
button7 = Button(root, text="7", width=5, height=2, command=lambda: btn_click(7))
button7.grid(row=3, column=0, pady=2)
button8 = Button(root, text="8", width=5, height=2, command=lambda: btn_click(8))
button8.grid(row=3, column=1, pady=2)
button9 = Button(root, text="9", width=5, height=2, command=lambda: btn_click(9))
button9.grid(row=3, column=2, pady=2)
button_plus = Button(root, text="+", width=5, height=5, command=lambda: btn_click("+"))
button_plus.grid(row=3, column=3, rowspan=2, pady=2)
button_squareroot = Button(root, text="√", width=5, height=2, command=lambda: btn_click2())
button_squareroot.grid(row=3, column=4, pady=2)

# line 3
button4 = Button(root, text="4", width=5, height=2, command=lambda: btn_click(4))
button4.grid(row=4, column=0, pady=2)
button5 = Button(root, text="5", width=5, height=2, command=lambda: btn_click(5))
button5.grid(row=4, column=1, pady=2)
button6 = Button(root, text="6", width=5, height=2, command=lambda: btn_click(6))
button6.grid(row=4, column=2, pady=2)
button_square = Button(root, text="²", width=5, height=2, command=lambda: btn_click3())
button_square.grid(row=4, column=4, pady=2)

# line 4
button1 = Button(root, text="1", width=5, height=2, command=lambda: btn_click(1))
button1.grid(row=5, column=0, pady=2)
button2 = Button(root, text="2", width=5, height=2, command=lambda: btn_click(2))
button2.grid(row=5, column=1, pady=2)
button3 = Button(root, text="3", width=5, height=2, command=lambda: btn_click(3))
button3.grid(row=5, column=2, pady=2)
button_sum = Button(root, bg="blue", activebackground="blue", text="=", width=5, height=5, command=lambda: btn_equal())
button_sum.grid(row=5, column=3, rowspan=2, pady=2)
button_leftparen = Button(root, text="(", width=5, height=2, command=lambda: btn_click("("))
button_leftparen.grid(row=5, column=4, pady=2)

# line 5
button0 = Button(root, text="0", width=14, height=2, command=lambda: btn_click(0))
button0.grid(row=6, column=0, columnspan=2, pady=2)
button_dot = Button(root, text=".", width=5, height=2, command=lambda: btn_click("."))
button_dot.grid(row=6, column=2, pady=2)
button_rightparen = Button(root, text=")", width=5, height=2, command=lambda: btn_click(")"))
button_rightparen.grid(row=6, column=4, pady=2)

root.mainloop()