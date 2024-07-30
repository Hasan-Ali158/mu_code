import tkinter
from tkinter import *

root=Tk()
root.title('Rock , Paper And Scissor Game')
root.geometry('600x500')


Label(root,text='Rock Paper Scissor Game ',font=("Courier",20)).pack(pady=20)


frame=Frame(root)
frame.pack()

l1=Label(frame,text='User       ',font=('Courier',20),fg='Blue')
l2=Label(frame,text='vs      ',font=('Courier',20))
l3=Label(frame,text='AutoPlayer',font=('Courier',20),fg='Red')
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
l4.pack(pady=20)

frame1=Frame(root)
frame1.pack()
def rock():
    print('Rock')
b1 = Button(frame1, text="Rock",
			font=('Courier',20), width=7,command=rock)

def paper():
    print('Paper')
b2 = Button(frame1, text="Paper ",
			font=('Courier',20), width=7,command=paper)

def scissor():
    print('Scissor')
b3 = Button(frame1, text="Scissor",
			font=('Courier',20), width=7,command=scissor)


def reset():
    print('Reset Game')
Button(root, text="Reset Game",
	font=('Courier',20), fg="white",
	bg="black",command=reset).pack(pady=20)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

root.mainloop()

