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
   #entry.delete(0, END)
def btnclear():
    global operator
    operator=""
    text_input.set("")
root=Tk()
root.config(bg='grey')
root.geometry("525x250")
root.title("the first calculation")

operator=""
text_input=StringVar()
entry=Entry(root,font=70,justify='right',insertwidth=4,bd=1,width=59,border=10,textvariable=text_input).grid(columnspan=4,ipady=12)
#entry.place(relheight=0.3)

#///////////////////////////********************************///////////////
button1=Button(root,text="7",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run(7)).grid(row=1,column=0)
#button1.pack()

#button1.place(x=0,y=23,relheight=0.25, relwidth=0.35)
button2=Button(root,text="8",bg="#42f5bf",font=70,bd=5,padx=65,command=lambda:run(8)).grid(row=1,column=1)
#button2.place(x=100,y=23,relheight=0.25, relwidth=0.35)
#button2.pack()
button3=Button(root,text="9",bg="#42f5bf",font=70,bd=5,padx=57,command=lambda:run(9)).grid(row=1,column=2)
#button3.place(x=200,y=23,relheight=0.25, relwidth=0.35)
#button3.pack()
button4=Button(root,text="+",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run("+")).grid(row=1,column=3)
#button4.place(x=300,y=23, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button5=Button(root,text="4",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run(4)).grid(row=2,column=0)
#button5.place(x=0,y=76, relheight=0.25, relwidth=0.35)
button6=Button(root,text="5",bg="#42f5bf",font=70,bd=5,padx=65,command=lambda:run(5)).grid(row=2,column=1)
#button6.place(x=100,y=76, relheight=0.25, relwidth=0.35)
button7=Button(root,text="6",bg="#42f5bf",font=70,bd=5,padx=57,command=lambda:run(6)).grid(row=2,column=2)
#button7.place(x=200,y=76, relheight=0.25, relwidth=0.35)
button8=Button(root,text="-",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run("-")).grid(row=2,column=3)
#button8.place(x=300,y=76, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button9=Button(root,text="1",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run(1)).grid(row=3,column=0)
#button9.place(x=0,y=126, relheight=0.25, relwidth=0.35)
button10=Button(root,text="2",bg="#42f5bf",font=70,bd=5,padx=65,command=lambda:run(2)).grid(row=3,column=1)
#button10.place(x=100,y=126, relheight=0.25, relwidth=0.35)
button11=Button(root,text="3",bg="#42f5bf",font=70,bd=5,padx=57,command=lambda:run(3)).grid(row=3,column=2)
#button11.place(x=200,y=126, relheight=0.25, relwidth=0.35)
button12=Button(root,text="*",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run("*")).grid(row=3,column=3)
#button12.place(x=300,y=126, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button13=Button(root,text="0",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run(0)).grid(row=4,column=0)
#button13.place(x=0,y=179, relheight=0.25, relwidth=0.35)
button14=Button(root,text="Clear",bg="#42f5bf",padx=50,font=70,bd=5,command=btnclear).grid(row=4,column=1)
#button14=Button(root,text=".",bg="#42f5bf",padx=50,font=70,bd=5,command=lambda:run(".")).grid(row=4,column=1)
#button14.place(x=100,y=179, relheight=0.25, relwidth=0.35)
button15=Button(root,text=",",bg="#42f5bf",font=70,bd=5,padx=60,command=lambda:run(",")).grid(row=4,column=2)
#button15.place(x=200,y=179, relheight=0.25, relwidth=0.35)
button16=Button(root,text="/",bg="#42f5bf",font=70,bd=5,padx=50,command=lambda:run("/")).grid(row=4,column=3)
#button16.place(x=300,y=179, relheight=0.25, relwidth=0.35)
#///////////////////////////********************************///////////////
button17=Button(root,text="=",bg="#42f5bf",padx=262,font=70,bd=5,command=btninput,justify='right').grid(row=5,column=0,columnspan=4)
#button17.place(x=0,y=244, relheight=0.21, relwidth=0.99)

#button18.place(x=0,y=297, relheight=0.21, relwidth=0.99)
root.mainloop()