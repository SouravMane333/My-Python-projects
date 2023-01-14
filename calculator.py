from tkinter import *


def click(event):
    global value

    button_Txt = event.widget.cget("text")
    print(button_Txt)

    if button_Txt == "=":
        if value.get().isdigit():
            val = int(value.get())
        else:
            try:
                val = eval(value.get())
            except Exception as e:
                print(e)
                val = "error"

        value.set(val)
        screen.update()

    elif button_Txt == "C":
        value.set("")
        screen.update()

    else:
        value.set(value.get() + button_Txt)
        screen.update()


root = Tk()
root.configure(background="cadet blue")
root.geometry("400x375")
root.minsize(400, 375)
root.maxsize(400, 375)

root.title("Calculator")

value = Label(root, text="This is a GUI for a calculator.", bg="black", fg="white",
              padx=5, pady=10, font="arial 15 bold", borderwidth=5, relief=SUNKEN)
value.grid()

value = StringVar()
value.set("")
screen = Entry(root, textvariable=value, bg="cadet blue",
               fg="black", font="arial 30 bold", borderwidth=20, relief=RIDGE, justify=RIGHT)
screen.grid(columnspan=1, sticky="news")

f = Frame(root, bg="black")


b = Button(f, text="(", fg="black", bg="white", height=2, width=7)
b.grid(row=2, column=1, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text=")", fg="black", bg="white", height=2, width=7)
b.grid(row=2, column=2, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="%", fg="black", bg="white", height=2, width=7)
b.grid(row=2, column=3, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="/", fg="black", bg="white", height=2, width=7)
b.grid(row=2, column=4, sticky="news")
b.bind("<Button-1>", click)


b = Button(f, text="7", fg="black", bg="white", height=2, width=7)
b.grid(row=3, column=1, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="8", fg="black", bg="white", height=2, width=7)
b.grid(row=3, column=2, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="9", fg="black", bg="white", height=2, width=7)
b.grid(row=3, column=3, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="*", fg="black", bg="white", height=2, width=7)
b.grid(row=3, column=4, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="4", fg="black", bg="white", height=2, width=7)
b.grid(row=4, column=1, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="5", fg="black", bg="white", height=2, width=7)
b.grid(row=4, column=2, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="6", fg="black", bg="white", height=2, width=7)
b.grid(row=4, column=3, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="-", fg="black", bg="white", height=2, width=7)
b.grid(row=4, column=4, sticky="news")
b.bind("<Button-1>", click)


b = Button(f, text="1", fg="black", bg="white", height=2, width=7)
b.grid(row=5, column=1, sticky="we")
b.bind("<Button-1>", click)

b = Button(f, text="2", fg="black", bg="white", height=2, width=7)
b.grid(row=5, column=2, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="3", fg="black", bg="white", height=2, width=7)
b.grid(row=5, column=3, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="+", fg="black", bg="white", height=2, width=7)
b.grid(row=5, column=4, sticky="news")
b.bind("<Button-1>", click)


b = Button(f, text="0", fg="black", bg="white", height=2, width=7)
b.grid(row=6, column=1, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text=".", fg="black", bg="white", height=2, width=7)
b.grid(row=6, column=2, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="C", fg="black", bg="white", height=2, width=7)
b.grid(row=6, column=3, sticky="news")
b.bind("<Button-1>", click)

b = Button(f, text="=", fg="black", bg="white", height=2, width=7)
b.grid(row=6, column=4, sticky="news")
b.bind("<Button-1>", click)

f.grid(sticky="news")

root.mainloop()
