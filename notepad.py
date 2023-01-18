# Import the required libraries
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def openfile():

    if not text.edit_modified():
        try:
            path = filedialog.askopenfile(filetypes=(
                ("Text files", "*.txt"), ("All files", "*.*"))).name

            root.title('Notepad - ' + path)

            with open(path, 'r') as f:
                content = f.read()
                text.delete('1.0', END)
                text.insert('1.0', content)

                text.edit_modified(0)

        except:
            pass


def savefile():
    try:

        path = root.title().split('-')[1][1:]

    except:
        path = ''

    if path != '':

        with open(path, 'w') as f:
            content = text.get('1.0', END)
            f.write(content)

    else:
        saveasfile()

    text.edit_modified(0)


def saveasfile():
    try:
        path = filedialog.asksaveasfile(filetypes=(
            ("Text files", "*.txt"), ("All files", "*.*"))).name
        root.title('Notepad - ' + path)

    except:
        return

    with open(path, 'w') as f:
        f.write(text.get('1.0', END))


def quitfile():
    root.destroy()


def cut():
    text.event_generate(("<<Cut>>"))


def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "This notepad is made by using the tkinter.\n Tkinter is a Python binding to the Tk GUI toolkit.")


if __name__ == '__main__':

    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("600x600")

    text = Text(root, font="arial 25", bg="white", fg="black")
    file = None
    text.pack(fill=BOTH, expand=TRUE)

    menuBar = Menu(root)

    # File start
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_command(label="Save As", command=saveasfile)
    fileMenu.add_separator()  # separates by a line
    fileMenu.add_command(label="Exit", command=quitfile)
    menuBar.add_cascade(label="File ", menu=fileMenu)
    # File ends

    # Edit start
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    # Edit  ends

    # Help start
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)
    # Help ends

    root.config(menu=menuBar)

    # Adding scroll bar
    scroll = Scrollbar(text, orient='vertical')
    scroll.pack(side=RIGHT, fill=BOTH)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    root.mainloop()
