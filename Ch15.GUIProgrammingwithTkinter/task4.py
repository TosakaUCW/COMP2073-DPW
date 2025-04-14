from tkinter import *
from tkinter import filedialog

root = Tk()

test = False

if test == True:
    catname = "/Users/tosaka/Developments/COMP2073-DPW/Ch15.GUIProgrammingwithTkinter/cat2.gif"
    dogname = "/Users/tosaka/Developments/COMP2073-DPW/Ch15.GUIProgrammingwithTkinter/dog.gif"
else:
    catname = filedialog.askopenfilename(
        initialdir='./',
        title="Pick an image for cat",
        filetypes=(("image files", "*.gif"), ("image files", "*.jpg"),("all files", "*.*"))
    )
    dogname = filedialog.askopenfilename(
        initialdir='./',
        title="Pick an image for dog",
        filetypes=(("image files", "*.gif"), ("image files", "*.jpg"),("all files", "*.*"))
    )

imcat = PhotoImage(file=catname)
imdog = PhotoImage(file=dogname)

cat_votes = 0
dog_votes = 0

def update_votes(pet):
    global cat_votes, dog_votes
    if pet == 'cat':
        cat_votes += 1
        cat_vote_label.config(text=f"{cat_votes}")
    elif pet == 'dog':
        dog_votes += 1
        dog_vote_label.config(text=f"{dog_votes}")
        
# Title is 'Vote Machine'
root.title("Vote Machine") # Set the title of the window
whint = Label(root, text="Vote for your pet!")
whint.pack()
        
# Frame to hold cat
cat_frame = Frame(root)
cat_frame.pack(side=LEFT, padx=20)
# Label to show cat votes
cat_vote_label = Label(cat_frame, text=f"{cat_votes}")
cat_vote_label.pack()
# Image of cat
wcat = Label(cat_frame, image=imcat)
wcat.image = imcat
wcat.pack()
# Button to vote for cat
vote_cat_button = Button(cat_frame, text="Vote", command=lambda: update_votes('cat'))
vote_cat_button.pack()

# Frame to hold dog
dog_frame = Frame(root)
dog_frame.pack(side=RIGHT, padx=20)
# Label to show dog votes
dog_vote_label = Label(dog_frame, text=f"{dog_votes}")
dog_vote_label.pack()
# Image of dog
wdog = Label(dog_frame, image=imdog)
wdog.image = imdog
wdog.pack()
# Button to vote for dog
vote_dog_button = Button(dog_frame, text="Vote", command=lambda: update_votes('dog'))
vote_dog_button.pack()

root.mainloop()