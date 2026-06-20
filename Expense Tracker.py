from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title('Expense Tracker')
root.geometry('500x400')

def tracker():
    a=int(salaryvalue.get())
    b=int(foodvalue.get())
    c=int(clothesvalue.get())
    d=int(travelvalue.get())
    e=int(otherexpensevalue.get())
    
    f=a/2
    

    totalexpense=b+c+d+e
    remaining=a-totalexpense

    if totalexpense>=a:
        tmsg.showinfo('warn','you r running out of money bruh')
    elif totalexpense<=f:
        tmsg.showinfo('message','you r on a right way')
    else:
        tmsg.showinfo('message','you rdoing good')
    
    tmsg.showinfo('Report',f'your salary is{a}\n you spend total of{totalexpense} \n you have {remaining} money remainig')

Label(root,text='Total salary').grid()
Label(root,text='food expenses').grid()
Label(root,text='clothes expenses').grid()
Label(root,text='travel expenses').grid()
Label(root,text='other expenses').grid()

salaryvalue=StringVar()

otherexpensevalue=StringVar()

foodvalue=StringVar()

clothesvalue=StringVar()

travelvalue=StringVar()

salentry=Entry(root,textvar=salaryvalue)
salentry.grid(row=0,column=1)


foodentry=Entry(root,textvar=foodvalue)
foodentry.grid(row=1,column=1)

clothentry=Entry(root,textvar=clothesvalue)
clothentry.grid(row=2,column=1)

travelentry=Entry(root,textvar=travelvalue)
travelentry.grid(row=3,column=1)

otherentry=Entry(root,textvar=otherexpensevalue)
otherentry.grid(row=4,column=1)


b=Button(root,text='track expenses',command=tracker)
b.grid(column=1)



root.mainloop()
