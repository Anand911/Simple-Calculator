from tkinter import *
import mathcalc as c 
root= Tk()
root.title("CALCULATOR")
ent=Entry(root,width=35)
ent.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#ent.grid(row=0,column=0)
ch=''
num=ent.get()
def clicked(num):
	current=ent.get()
	ent.delete(0,END)
	ent.insert(0,str(current)+str(num))
def click_clear():
	ent.delete(0,END)

def add():
	global ch
	ch='+' 
	clicked('+')

def subtract():
	global ch
	ch='-' 
	clicked('-')

def multiply():
	global ch
	ch='*' 
	clicked('*')

def divide():
	global ch
	ch='/' 
	clicked('/')
def equals():
	f_num,s_num=ent.get().split(ch)
	res=c.calculate(float(f_num),float(s_num),ch)
	ent.delete(0,END)
	ent.insert(0,res)

#buttons
but1=Button(root,text="1",padx=40,pady=20,command=lambda: clicked(1))
but2=Button(root,text="2",padx=40,pady=20,command=lambda: clicked(2))
but3=Button(root,text="3",padx=40,pady=20,command=lambda: clicked(3))
but4=Button(root,text="4",padx=40,pady=20,command=lambda: clicked(4))
but5=Button(root,text="5",padx=40,pady=20,command=lambda: clicked(5))
but6=Button(root,text="6",padx=40,pady=20,command=lambda: clicked(6))
but7=Button(root,text="7",padx=40,pady=20,command=lambda: clicked(7))
but8=Button(root,text="8",padx=40,pady=20,command=lambda: clicked(8))
but9=Button(root,text="9",padx=40,pady=20,command=lambda: clicked(9))
but0=Button(root,text="0",padx=40,pady=20,command=lambda: clicked(0))

but_plus=Button(root,text="+",padx=39,pady=20,command=add)
but_sub=Button(root,text="-",padx=40,pady=20,command=subtract)
but_mul=Button(root,text="*",padx=40,pady=20,command=multiply)
but_div=Button(root,text="/",padx=40,pady=20,command=divide)
but_eq=Button(root,text="=",padx=89,pady=20,command=equals)
but_clr=Button(root,text="C",padx=89,pady=20,command=click_clear)
#button place
but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

but0.grid(row=4,column=0)
but_plus.grid(row=5,column=0)
but_sub.grid(row=6,column=0)
but_mul.grid(row=6,column=1)
but_div.grid(row=6,column=2)
but_eq.grid(row=4,column=1,columnspan=2)
but_clr.grid(row=5,column=1,columnspan=2)
root.mainloop()
