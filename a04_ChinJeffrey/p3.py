from tkinter import *
root = Tk()
root.geometry("350x350")
root.title("Calculator")

def button_click(number):
    current = entry.get()
    if number == "DEL":
        entry.delete(len(current)-1, END)
        return
    elif number == "C":
        entry.delete(0, END)
        result.delete(0, END)
        return
    elif number == "=":
        result.delete(0, END)
        try:
            result.insert(0, eval(current))
        except:
            result.insert(0, "Error")
        return
    elif current == "0" and number == 0:
        return
    elif current == "0" and number != 0:
        current = ""
        entry.delete(0, END)

    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# def button_clear():
#     entry.delete(0, END)



num1 = Button(root, text="1", height=2, width=4, command=lambda: button_click(1))
num2 = Button(root, text="2", height=2, width=4, command=lambda: button_click(2))
num3 = Button(root, text="3", height=2, width=4, command=lambda: button_click(3))
num4 = Button(root, text="4", height=2, width=4, command=lambda: button_click(4))
num5 = Button(root, text="5", height=2, width=4, command=lambda: button_click(5))
num6 = Button(root, text="6", height=2, width=4, command=lambda: button_click(6))
num7 = Button(root, text="7", height=2, width=4, command=lambda: button_click(7))
num8 = Button(root, text="8", height=2, width=4, command=lambda: button_click(8))
num9 = Button(root, text="9", height=2, width=4, command=lambda: button_click(9))
num0 = Button(root, text="0", height=2, width=4, command=lambda: button_click(0))
add = Button(root, text="+", height=2, width=4, command=lambda: button_click("+"))
sub = Button(root, text="-", height=2, width=4, command=lambda: button_click("-"))
mul = Button(root, text="*", height=2, width=4, command=lambda: button_click("*"))
div = Button(root, text="/", height=2, width=4, command=lambda: button_click("/"))
paren1 = Button(root, text="(", height=2, width=4, command=lambda: button_click("("))
paren2 = Button(root, text=")", height=2, width=4, command=lambda: button_click(")"))
clear = Button(root, text="C", height=2, width=4, command=lambda: button_click("C"))
equal = Button(root, text="=", height=2, width=4, command=lambda: button_click("="))
delete = Button(root, text="DEL", height=2, width=4, command=lambda: button_click("DEL"))

entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=3)
result = Entry(root, width=30, borderwidth=5)
result.grid(row=1, column=0, columnspan=3, padx=10, pady=3)

num1.grid(row=2, column=0)
num2.grid(row=2, column=1)
num3.grid(row=2, column=2)
num4.grid(row=2, column=3)

num5.grid(row=3, column=0)
num6.grid(row=3, column=1)
num7.grid(row=3, column=2)
num8.grid(row=3, column=3)

num9.grid(row=4, column=0)
num0.grid(row=4, column=1)
add.grid(row=4, column=2)
sub.grid(row=4, column=3)

mul.grid(row=5, column=0)
div.grid(row=5, column=1)
paren1.grid(row=5, column=2)
paren2.grid(row=5, column=3)

delete.grid(row=6, column=0)
clear.grid(row=6, column=1)
equal.grid(row=6, column=2)

root.mainloop()