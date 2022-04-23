from tkinter import *

window=Tk()
width = 10
height = 50 
window.title('Paint')
window.state('zoomed')
window.config(bg='pink')
#window.rowconfigure(0, weight=10)
#window.columnconfigure(0, weight=10)
def buttonone():
    id = canvas2.create_rectangle(10, 10, 30, 30, fill='grey', width=1)
    canvas2.tag_bind(id, "<Button-1>")

canvas = Canvas(window, height=400, width=400, bg='white')
canvas2 = Canvas(window, height=40, width=400, bg='white')
one = Button(window, text='1 ',)#command=clearAll )
two= Button(window, text="2",)#command=SaveImage)
three = Button(window, text='3 ',) #command=clearAll)
four = Button(window, text="4",) #command=SaveImage)
five = Button(window, text='5',) #command=clearAll)
six = Button(window, text="6",)#command=SaveImage)
canvas.bind("<B1-Motion>" ,buttonon)
buttonone()

canvas.pack()
canvas2.pack()
window.mainloop()