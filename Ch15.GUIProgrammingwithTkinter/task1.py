#pack_sample.py
from tkinter import *
# Hold onto a global reference for the root window
root = None
count = 0 # Click counter
def addButton(root, sideToPack):
    global count
    name = "Button "+ str(count) +" "+sideToPack
    button = Button(root, text=name)
    button.pack(side=sideToPack)
    count +=1
def main():
    global root
    root = Tk() # Create the root (base) window where all widgets go
    
    frametop = Frame(root)
    addButton(frametop, TOP) # 0
    
    framemiddle = Frame(root)
    
    frameleft = Frame(framemiddle)
    addButton(frameleft, TOP) # 1
    addButton(frameleft, TOP) # 2
    addButton(frameleft, TOP) # 3
    
    frameright = Frame(framemiddle)
    addButton(frameright, TOP) # 4
    addButton(frameright, TOP) # 5
    
    framebottom = Frame(root)
    addButton(framebottom, TOP) # 6
    
    frameleft.pack(side=LEFT)
    frameright.pack(side=LEFT)
    frametop.pack(side=TOP)
    framemiddle.pack(side=TOP)
    framebottom.pack(side=TOP)
    
    root.mainloop() # Start the event loop
main()