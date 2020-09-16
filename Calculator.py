from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0,columnspan=4,  padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clr():
    e.delete(0, END)

def button_equal():
    s_num = int(e.get())
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + s_num)
    if math == "sub":
        e.insert(0, f_num - s_num)
    if math == "mul":
        e.insert(0, f_num * s_num)
    if math == "div":
        if s_num != 0:
            e.insert(0, f_num / s_num)
        else:
            e.insert(0, "Error")

def button_add():
    global f_num, math
    math = "add"
    f_num = int(e.get())
    e.delete(0,END)

def button_sub():
    global f_num, math
    math = "sub"
    f_num = int(e.get())
    e.delete(0, END)

def button_mul():
    global f_num, math
    math = "mul"
    f_num = int(e.get())
    e.delete(0, END)

def button_div():
    global f_num, math
    math = "div"
    f_num = int(e.get())
    e.delete(0, END)



button_1 = Button(root, text="1", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, fg="white",bg="#3f3f3f", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=28, pady=20, fg="white",bg="#3f3f3f", command=button_add)
button_sub = Button(root, text="-", padx=30, pady=20, fg="white",bg="#3f3f3f", command=button_sub)
button_mul = Button(root, text="*", padx=30, pady=20, fg="white",bg="#3f3f3f", command=button_mul)
button_div = Button(root, text="/", padx=30, pady=20, fg="white",bg="#3f3f3f", command=button_div)
button_equ = Button(root, text="=", padx=30, pady=20, fg="white",bg="#3f3f3f", command=button_equal)
button_clr = Button(root, text="C", padx=30, pady=20, fg="white",bg="#3f3f3f", command=button_clr)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)

button_equ.grid(row=4, column=1)
button_clr.grid(row=4, column=2)

root.mainloop()
