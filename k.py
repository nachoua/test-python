from tkinter import *

root=Tk()
root.title("coucou")

root.config(bg='pink')
Label=Label(root,text="hey miss nachoua")
button=Button(root,text='just text for test')
button.config(command="click")
image= PhotoImage(file="a1.jpg")
button.config(Image=image)
button.config(font=('italic',30,'bold'))
button.config(bg='red')
button.config(fg='white')
button.pack()
Label.config(bg='white')
Label.pack()

root.mainloop()