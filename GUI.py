import tkinter as tk
from tkinter.constants import END

def tst(entry):
 print("just the first ",entry)
#def bind(self, sequence, func, add=''):
  #  print("just ",entry)

def run(entry):


    label = tk.Label(lower_frame,bg='pink',textvariable=name_storage)
    label.place(relwidth=1, relheight=1,)
    
    label.pack()


    
HEIGHT=500
WIDTH=600

root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
#background_image = tk.PhotoImage(file=':/newPrefix/a1.jpg')
#background_label = tk.Label(root, image=background_image)
#background_label.pace(relwidth=1, relheight=1)
#background_image.pack()
#background_label.pack()
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')
name_storage=tk.Listbox(root)
entry = tk.Entry(frame,font=40,textvariable=name_storage,fg='grey')
entry.place(relwidth=0.65, relheight=1)
entry.insert(0,'Try write something')
button = tk.Button(frame, text="test button", bg='pink',font=40,command=lambda:run(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Button(root, bg='#fff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

#listbox.insert(1,"Bread")  
#listbox.insert(2, "Milk")  
#listbox.insert(3, "Meat")  
#listbox.insert(4, "Cheese")
#listbox.insert(5, "Vegetables")  
listbox = tk.Listbox(lower_frame) 
listbox.insert(0,"hello") 
for line in range(1, 101): 
  listbox.insert(END,str(line))

listbox.pack() 

root.mainloop()