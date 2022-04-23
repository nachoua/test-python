from tkinter import *
from tkinter.font import BOLD

root=Tk()
root.config(bg='black')
root.geometry("500x400")
root.title("hello miss nachoua")
def uk():
    
    En1=entry.get()
    En2=entry2.get()
    text_input3.set("the first name is :"+En1)
    text_input4.set("the first name is :"+En2)
    print("The FirstName is  :",En1)
    print("The LastName is :",En2)

label=Label(root,text="firstname",font=10,bg='purple',fg="white")
label.place(x=45, y=80,relwidth=0.25,relheight=0.1)

entry=Entry(root,font=50)
entry.place(x=150,y=80,relheight=0.1,relwidth=0.48)

label2=Label(root,text="lastname",font=50,bg='purple',fg="white")
label2.place(x=45, y=150,relwidth=0.25,relheight=0.1)

entry2=Entry(root,font=50)
entry2.place(x=150,y=150,relheight=0.1,relwidth=0.48)
text_input3=StringVar()
text_input4=StringVar()
label3=Label(root,text=" ",font=10,bg='pink',fg="purple",textvariable=text_input3)
label3.place(x=90, y=250,relwidth=0.65,relheight=0.1)
label4=Label(root,text=" ",font=10,bg='pink',fg="purple",textvariable=text_input4)
label4.place(x=90, y=300,relwidth=0.65,relheight=0.1)
button=Button(root,text="Valider",font=70,bg='purple',fg="white",command=uk)
button.place(x=120,y=350, relheight=0.14, relwidth=0.58)

root.mainloop()