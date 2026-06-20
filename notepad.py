from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.title('Notepad')


def newfile():
    global file
    root.title('Untitled - Notepad')
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file

    file = askopenfilename(
        defaultextension='.txt',
        filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])

    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + '- Notepad')

        textarea.delete(1.0, END)

        f = open(file, 'r')
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file

    if file == None:
        file = asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])

        if file == '':
            file = None

        else:
            f = open(file, 'w')
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + '- Notepad')

    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")
    textarea.focus_set()

def copy():
    textarea.event_generate("<<Copy>>")
    textarea.focus_set()

def paste():
    textarea.event_generate("<<Paste>>")
    textarea.focus_set()
def about():
    tmsg.showinfo('notepad','thsi is notepad made by piyush')


file = None


root.geometry('700x600')


sc = Scrollbar(root)
sc.pack(side=RIGHT, fill=Y)


textarea = Text(root, font='lucida 13',undo=TRUE, yscrollcommand=sc.set)
textarea.pack(fill=BOTH, expand=True)

sc.config(command=textarea.yview)



# File Menu
mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)

m1.add_command(label='New', command=newfile)
m1.add_command(label='Open', command=openfile)
m1.add_command(label='Save', command=savefile)
m1.add_command(label='Exit', command=quitapp)

mainmenu.add_cascade(label='File', menu=m1)



# Edit Menu
m2 = Menu(mainmenu, tearoff=0)

m2.add_command(label='Cut', command=cut)
m2.add_command(label='Copy', command=copy)
m2.add_command(label='Paste', command=paste)

mainmenu.add_cascade(label='Edit', menu=m2)



# Help Menu
m3 = Menu(mainmenu, tearoff=0)

m3.add_command(label='About Notepad', command=about)

mainmenu.add_cascade(label='Help', menu=m3)



root.config(menu=mainmenu)

root.mainloop()
