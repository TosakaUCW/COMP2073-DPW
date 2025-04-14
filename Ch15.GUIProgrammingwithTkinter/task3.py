from tkinter import *
def selected(event):
    listbox = event.widget
    selection = listbox.curselection()
    if selection:
        id = selection[0]
        s.set("You love " + listbox.get(id) + "!")
root = Tk()
Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "Ruby")
Lb1.insert(6, "Python")
Lb1.insert(7, "Perl")
Lb1.insert(8, "C")
Lb1.insert(9, "PHP")
Lb1.insert(10, "Ruby")

# A label at the bottom saying “What do you love?” when the program starts
# and changes to “You love <language>!” when a language is selected.
# This label should be updated when a language is selected from the listbox.
s = StringVar()
s.set("What do you love?")
w = Label(root, textvariable=s)
Lb1.pack()
w.pack()
Lb1.bind("<<ListboxSelect>>", selected)
root.mainloop()