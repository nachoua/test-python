from tkinter import *
root=Tk()
root.config(bg='#4299f5')
root.geometry("320x300")
root.title("hello")
def test():
    E=int(entry.get())
    a=int(2021-E)
    #label2.delete(0 ,END)
    text_input.set(a)
    #label2.insert(0 , a)
    print("you'are Age is :",a)
    
    if a<30:
     print("Try to Survive you'are Life")
    elif a>30:
     print("Life is short")


label=Label(root,text="Birthday",font=10,bg='#42f5bf',fg="black",bd=5)
label.place(x=30, y=100,relwidth=0.25,relheight=0.1)
text_input=StringVar()
entry=Entry(root,font=50)
entry.place(x=150,y=100,relheight=0.1,relwidth=0.48)
button=Button(root,text="Calculer",font=70,bg='#42f5bf',fg="black",bd=5,command=test)
button.place(x=80,y=200, relheight=0.14, relwidth=0.58)
label2=Label(root,text="",font=30,bg='#42f5bf',fg="black",bd=5,textvariable=text_input)
label2.place(x=30, y=160,relwidth=0.68,relheight=0.1)
root.mainloop()