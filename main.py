# importing tkinter library
from tkinter import *

# setting parameters of the user interface
calc = Tk()
calc.config(background='white smoke')
calc.resizable(width=False, height=False)
calc.geometry("474x317")
calc.title('Calculatrice')

# storing data input by user and creating array to display it
fieldMath = StringVar()
calcValue = ""
dataField = Entry(calc, textvariable=fieldMath, font="Serif 15", bg="white", width=32)
dataField.grid(row=0, columnspan=5, rowspan=2)

# initializing a listbox to display historic with historique as an empty list
historique = []
histon = Listbox(calc, width=15, height=13, listvariable=historique)
histon.place(x=360, y=0)


def get_value(x):
    global calcValue
    calcValue = calcValue + str(x)  # str() converts int type into string, then add is added to calcValue
    fieldMath.set(calcValue)


def square_rt():  # square root function
    global calcValue
    operation = calcValue
    calcValue = str(float(fieldMath.get()) ** 0.5)
    fieldMath.set(calcValue)

    stringresult = operation + " = " + calcValue  # create a new string inserted to histon
    histon.insert(0, stringresult)


def square():  # square function
    global calcValue
    operation = calcValue
    calcValue = str(float(fieldMath.get()) ** 2)
    fieldMath.set(calcValue)

    stringresult = operation + " = " + calcValue  # create a new string inserted to histon
    histon.insert(0, stringresult)


def clearInput():
    global calcValue
    calcValue = ""
    fieldMath.set("")


def clearHistorique():
    histon.delete(0, END)


def equal():  # function calculating result
    try:
        global calcValue

        operation = calcValue  # getting calculation before it is evaluated
        total = str(eval(calcValue))
        fieldMath.set(total)
        calcValue = total

        stringresult = operation + " = " + calcValue  # create a new string inserted to histon
        histon.insert(0, stringresult)

    except:
        fieldMath.set('erreur')
        calcValue = ''


# lines of buttons :
# line 1
button_mod = Button(calc, text="%", width=5, height=2, bg="light slate blue", activebackground="slate blue", command=lambda: get_value("%"), relief=RAISED)
button_mod.grid(row=2, column=0, pady=2)
button_div = Button(calc, text="/", width=5, height=2, bg="light slate blue", activebackground="slate blue", command=lambda: get_value("/"))
button_div.grid(row=2, column=1, pady=2)
button_mult = Button(calc, text="*", width=5, bg="light slate blue", activebackground="slate blue", height=2, command=lambda: get_value("*"))
button_mult.grid(row=2, column=2, pady=2)
button_less = Button(calc, text="-", width=5, bg="light slate blue", activebackground="slate blue", height=2, command=lambda: get_value("-"))
button_less.grid(row=2, column=3, pady=2)
button_clear = Button(calc, text="C", width=5, height=2, activebackground="grey23", bg="grey28", command=lambda: clearInput())
button_clear.grid(row=2, column=4, pady=2)

# line 2
button7 = Button(calc, text="7", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(7))
button7.grid(row=3, column=0, pady=2)
button8 = Button(calc, text="8", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(8))
button8.grid(row=3, column=1, pady=2)
button9 = Button(calc, text="9", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(9))
button9.grid(row=3, column=2, pady=2)
button_plus = Button(calc, text="+", width=5, height=5, bg="light slate blue", activebackground="slate blue", command=lambda: get_value("+"))
button_plus.grid(row=3, column=3, rowspan=2, pady=2)
button_squareroot = Button(calc, text="√", width=5, height=2, command=lambda: square_rt())
button_squareroot.grid(row=3, column=4, pady=2)

# line 3
button4 = Button(calc, text="4", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(4))
button4.grid(row=4, column=0, pady=2)
button5 = Button(calc, text="5", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(5))
button5.grid(row=4, column=1, pady=2)
button6 = Button(calc, text="6", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(6))
button6.grid(row=4, column=2, pady=2)
button_square = Button(calc, text="²", width=5, height=2, command=lambda: square())
button_square.grid(row=4, column=4, pady=2)

# line 4
button1 = Button(calc, text="1", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(1))
button1.grid(row=5, column=0, pady=2)
button2 = Button(calc, text="2", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(2))
button2.grid(row=5, column=1, pady=2)
button3 = Button(calc, text="3", bg="AntiqueWhite1", activebackground="AntiqueWhite3", width=5, height=2, command=lambda: get_value(3))
button3.grid(row=5, column=2, pady=2)
button_sum = Button(calc, bg="light slate blue", activebackground="slate blue", text="=", width=5, height=5, command=lambda: equal())
button_sum.grid(row=5, column=3, rowspan=2, pady=2)
button_leftparen = Button(calc, text="(", width=5, height=2, command=lambda: get_value("("))
button_leftparen.grid(row=5, column=4, pady=2)

# line 5
button0 = Button(calc, text="0", width=15, height=2, bg="AntiqueWhite1", activebackground="AntiqueWhite3", command=lambda: get_value(0))
button0.grid(row=6, column=0, columnspan=2, pady=2)
button_dot = Button(calc, text=".", width=5, height=2, command=lambda: get_value("."))
button_dot.grid(row=6, column=2, pady=2)
button_rightparen = Button(calc, text=")", width=5, height=2, command=lambda: get_value(")"))
button_rightparen.grid(row=6, column=4, pady=2)
button_delhisto = Button(calc, text="DEL", width=12, height=2, activebackground="grey23", bg="grey28", command=lambda: clearHistorique())
button_delhisto.grid(row=6, column=5, pady=2, padx=1)

calc.mainloop()