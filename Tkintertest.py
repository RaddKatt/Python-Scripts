from Tkinter import *

# create the root window
root = Tk()
root.title("This is my Title")
root.geometry("1000x500")

# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()

# create a button in the frame
button1 = Button(app, text = "I'm a button!")
button1.grid()

root.mainloop()
