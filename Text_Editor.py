from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, ttk, WORD

#root from main window
root = Tk(className = "Text Editor")
textArea = scrolledtext.ScrolledText(root, wrap = WORD, width=100, height=80, font = ("Arial", 15))


#Functions

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def openNewWindow():
    
    newTextArea = scrolledtext.ScrolledText(root, width=100, height=80)

def openFile():
	file = filedialog.askopenfile(parent=root, title = "Select a text file", filetypes=(("Text file", "*.txt"), ("All files", "*.")))

	if file != None:
		contents = file.read()
		textArea.insert('1.0', contents)
		file.close()

def saveFile():
	file = filedialog.asksaveasfile(mode='w')

	if file != None:
	# slice off the last character from get, as an extra return(enter) is added
		data = self.textArea.get('1.0', END+'-1c')
		file.write(data)
		file.close

def about():
	messagebox.showinfo("About", "A Python alternative to Notepad!")

def exitRoot():
	if messagebox.askyesno("Quit", "Are you sure you to quit?"):
		root.quit()




#menu
menu = Menu(root)
fileMenu=Menu(menu,tearoff = 0)

menu.add_cascade(label="File", menu = fileMenu)

#menu options
fileMenu.add_command(label = "New", command=openNewWindow)
fileMenu.add_command(label = "Open", command = openFile)
fileMenu.add_command(label = "Save", command = saveFile)
fileMenu.add_command(label=  "Save as...", command = donothing)
fileMenu.add_command(label=  "Close", command = donothing)

fileMenu.add_separator()


fileMenu.add_command(label = "Exit", command = exitRoot)



editMenu = Menu(menu, tearoff=0)
editMenu.add_command(label="Undo", command=donothing)

editMenu.add_separator()

editMenu.add_command(label="Cut", command=donothing)
editMenu.add_command(label="Copy", command=donothing)
editMenu.add_command(label="Paste", command=donothing)
editMenu.add_command(label="Delete", command=donothing)
editMenu.add_command(label="Select All", command=donothing)

menu.add_cascade(label="Edit", menu=editMenu)

helpMenu = Menu(menu, tearoff=0)


menu.add_cascade(label = "Help", menu=helpMenu)
menu.add_cascade(label = "About", menu=about)





textArea.pack()
root.config(menu=menu)

# Placing cursor in the text area 
textArea.focus() 

#keep window
root.mainloop()
