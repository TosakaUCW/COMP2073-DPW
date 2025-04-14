from tkinter import *
root = Tk()
im = PhotoImage(file='cat.gif') # Create a PhotoImage widget
# Create a canvas widget
myCanvas = Canvas(root, width=225, height=325)
# Draw 2 lines on the canvas
myCanvas.create_line(0, 0, 225, 100)
myCanvas.create_line(0, 100, 225, 0, fill='pink', dash=(4, 4))
# Add the image to the canvas
myCanvas.create_image(0, 100, anchor=NW, image=im)
myCanvas.image = im
# change the background color of the canvas to “yellow”
myCanvas.configure(bg='yellow')
myCanvas.pack()
root.mainloop() # Start the event loop