from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Event Handler")
window.geometry("100x100")
def func1(event):
    print(event.char)
window.bind("<Key>",func1)
def func2(a):
    print("The button was clicked") 
    messagebox.show
    info("Success","The button was clicked")   
btn=Button(text="Click Me!")   
btn.pack() 
btn.bind("<Button-1>",func2)
window.mainloop()