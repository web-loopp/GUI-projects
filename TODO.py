from tkinter import *
root=Tk()
root.geometry('700x600')
def add():
    a=uservalue.get()
    if a.strip()!="":
        lst.insert(END,a)
        userentry.set('')

    
    lst.insert(END,a)
def dele():
    lst.delete(ACTIVE)

uservalue=StringVar()


userentry=Entry(root,textvar=uservalue,bg='grey')
userentry.pack()
Label(root,text='TODO LIST ').pack()
lst=Listbox(root)
lst.pack()
lst.insert(END,'add the first todo item')

Button(root,text='ADD',command=add).pack()
Button(root,text='delete',command=dele).pack()
root.mainloop()
