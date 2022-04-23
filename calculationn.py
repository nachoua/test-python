from tkinter import *
def run(numbers):
    global operator
    operator= operator + str(numbers)
    #En1=entry.get()
    #btn1=button1.get()
    text_input.set(operator)
def btninput():
   global operator
   sumup=str(eval(operator))
   text_input.set(sumup)
   operator=""
root=Tk()
root.config(bg='grey')
root.geometry("470x310")
root.title("the first calculation")

operator=""
text_input=StringVar()
entry=Entry(root,font=70,justify='right',insertwidth=4,bd=1,width=55,textvariable=text_input).grid(columnspan=4)
#entry.place(relheight=0.3)

#///////////////////////////********************************///////////////
button1=Button(root,text="7",font=70,bd=5,command=lambda:run(7))
#button1.pack()

button1.place(x=0,y=23,relheight=0.25, relwidth=0.35)
button2=Button(root,text="8",font=70,bd=5,command=lambda:run(8))
button2.place(x=100,y=23,relheight=0.25, relwidth=0.35)
#button2.pack()
button3=Button(root,text="9",font=70,bd=5,command=lambda:run(9))
button3.place(x=200,y=23,relheight=0.25, relwidth=0.35)
#button3.pack()
button4=Button(root,text="+",font=70,bd=5,command=lambda:run("+"))
button4.place(x=300,y=23, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button5=Button(root,text="4",font=70,bd=5,command=lambda:run(4))
button5.place(x=0,y=76, relheight=0.25, relwidth=0.35)
button6=Button(root,text="5",font=70,bd=5,command=lambda:run(5))
button6.place(x=100,y=76, relheight=0.25, relwidth=0.35)
button7=Button(root,text="6",font=70,bd=5,command=lambda:run(6))
button7.place(x=200,y=76, relheight=0.25, relwidth=0.35)
button8=Button(root,text="-",font=70,bd=5,command=lambda:run("-"))
button8.place(x=300,y=76, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button9=Button(root,text="1",font=70,bd=5,command=lambda:run(1))
button9.place(x=0,y=126, relheight=0.25, relwidth=0.35)
button10=Button(root,text="2",font=70,bd=5,command=lambda:run(2))
button10.place(x=100,y=126, relheight=0.25, relwidth=0.35)
button11=Button(root,text="3",font=70,bd=5,command=lambda:run(3))
button11.place(x=200,y=126, relheight=0.25, relwidth=0.35)
button12=Button(root,text="*",font=70,bd=5,command=lambda:run("*"))
button12.place(x=300,y=126, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button13=Button(root,text="0",font=70,bd=5,command=lambda:run(0))
button13.place(x=0,y=179, relheight=0.25, relwidth=0.35)
button14=Button(root,text=".",font=70,bd=5,command=run("."))
button14.place(x=100,y=179, relheight=0.25, relwidth=0.35)
button15=Button(root,text=",",font=70,bd=5,command=lambda:run(","))
button15.place(x=200,y=179, relheight=0.25, relwidth=0.35)
button16=Button(root,text="/",font=70,bd=5,command=lambda:run("/"))
button16.place(x=300,y=179, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button17=Button(root,text="=",font=70,bd=5,command=btninput,justify='right')
button17.place(x=0,y=244, relheight=0.21, relwidth=0.99)

root.mainloop()