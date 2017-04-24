from tkinter import *
import tkinter.messagebox

result = ""


root = Tk()

calculation = False

#Checking if provided text contain +-*/ and return true or false
def is_calculating(text):
    if "+" in text or "-" in text or "*" in text or "/" in text or len(text) == 0:
        return True
    else:
        return False

def calculate(event):

    index = 0
    if len(label["text"]) == 0 or is_calculating(label["text"]) == False:
        pass
    else:
        if "+" in label["text"]:
            index = label["text"].index("+")
        elif "-" in label["text"]:
            index = label["text"].index("-")
        elif "*" in label["text"]:
            index = label["text"].index("*")
        elif "/" in label["text"]:
            index = label["text"].index("/")
        part_1 = label["text"][0:index]
        part_2 = label["text"][index+1:]
        symbol = label["text"][index]
        if int(part_2) == 0:
            pass
        elif symbol == "+":
            label["text"] = str(int(part_1)+int(part_2))
        elif symbol == "-":
            label["text"] = str(int(part_1) - int(part_2))
        elif symbol == "*":
            label["text"] = str(int(part_1) * int(part_2))
        elif symbol == "/":
            label["text"] = str(int(part_1) / int(part_2))


def add_add(event):
    if is_calculating(label["text"]) == False:
        label["text"] += "+"
    else:
        pass

def add_subtract(event):
    if is_calculating(label["text"]) == False:
        label["text"] += "-"
    else:
        pass

def add_multiple(event):
    if is_calculating(label["text"]) == False:
        label["text"] += "*"
    else:
        pass

def add_divide(event):
    if is_calculating(label["text"]) == False:
        label["text"] += "/"
    else:
        pass

def cls(event):
    label["text"] = ""

def remove_last(event):
    label["text"] = label["text"][0:-1]

# Adds number to current label text
def add_1(event):
    label["text"] += "1"

# Adds number to current label text
def add_2(event):
    label["text"] += "2"

# Adds number to current label text
def add_3(event):
    label["text"] += "3"

# Adds number to current label text
def add_4(event):
    label["text"] += "4"

# Adds number to current label text
def add_5(event):
    label["text"] += "5"

# Adds number to current label text
def add_6(event):
    label["text"] += "6"

# Adds number to current label text
def add_7(event):
    label["text"] += "7"

# Adds number to current label text
def add_8(event):
    label["text"] += "8"

# Adds number to current label text
def add_9(event):
    label["text"] += "9"

# Adds number to current label text
def add_0(event):
    label["text"] += "0"


# ********* Section creating label and buttons in grid **************
label = Label(root, text=result, width=10, height=2)
label.grid(columnspan=3, row = 0, column = 0)

button_1 = Button(root, text="1", width=2, height=2)
button_1.bind("<Button-1>", add_1)
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", width=2, height=2)
button_2.bind("<Button-1>", add_2)
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", width=2, height=2)
button_3.bind("<Button-1>", add_3)
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", width=2, height=2)
button_4.bind("<Button-1>", add_4)
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", width=2, height=2)
button_5.bind("<Button-1>", add_5)
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", width=2, height=2)
button_6.bind("<Button-1>", add_6)
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", width=2, height=2)
button_7.bind("<Button-1>", add_7)
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", width=2, height=2)
button_8.bind("<Button-1>", add_8)
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", width=2, height=2)
button_9.bind("<Button-1>", add_9)
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", width=2, height=2)
button_0.bind("<Button-1>", add_0)
button_0.grid(row=4, columnspan=3)

button_add = Button(root, text="+", width=2, height=2)
button_add.bind("<Button-1>", add_add)
button_add.grid(row=1, column=3)

button_subtract = Button(root, text="-", width=2, height=2)
button_subtract.bind("<Button-1>", add_subtract)
button_subtract.grid(row=2, column=3)

button_multiple = Button(root, text="*", width=2, height=2)
button_multiple.bind("<Button-1>", add_multiple)
button_multiple.grid(row=3, column=3)

button_divide = Button(root, text="/", width=2, height=2)
button_divide.bind("<Button-1>", add_divide)
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=", width=2, height=2)
button_equal.bind("<Button-1>", calculate)
button_equal.grid(row=4, column=2)

button_cls = Button(root, text="CLS", width=2, height=2)
button_cls.bind("<Button-1>", cls)
button_cls.grid(row=5, column=1)

button_remove = Button(root, text="CLL", width=2, height=2)
button_remove.bind("<Button-1>", remove_last)
button_remove.grid(row=5, column=2)

root.mainloop()
