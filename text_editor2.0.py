from tkinter import *
from tkinter import filedialog
from tkinter import font


root = Tk()
root.title("AteachZ.com TextPad!")
#root.iconbitmap('')
root.geometry("1200x660")

#Create New File Function

def new_file():
    my_text.delete('1.0' , END)
    root.title('New File - TextPad!')
    status_bar.config(text = "New File    ")

# Open File
def open_file():
    #delete previous text
    my_text.delete("1.0", END)

    #grab filename
    text_file = filedialog.askopenfilename(initialdir = "", title="")
    
    

#create Main Frame
my_frame = Frame(root)
my_frame.pack(pady = 5)

#Create Scrollbar for the text box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#Create Text Box
my_text = Text(my_frame, width = 1200, height = 660 , 
	font = ("Arial", 16), selectbackground = "yellow", 
	selectforeground = "black", undo = True, yscrollcommand = text_scroll.set)
my_text.pack()

#config scrollbar
text_scroll.config(command = my_text.yview)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add file Menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)

file_menu.add_command(label = "New", command = file_menu)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = saveas_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#Add Edit Menu

edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)

edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo")


#Add status bar to the Bottom of the App
status_bar = Label(root, text="Ready ", anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

root.mainloop()
