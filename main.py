import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def changeColor():
    color = colorchooser.askcolor(title="Choose color")
    text_area.config(fg=color[1])

def changeFont(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def newFile():
    window.title("Untitled")
    text_area.delete(1.0, END)

def openFile():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)
            f = open(file, "r")
            text_area.insert(1.0, f.read())

        except:
            showerror("Error", "Error while opening file")

        finally:
            f.close()

def saveFile():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                    ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            f = open(file, "w")
            f.write(text_area.get(1.0, END))
        except:
            showerror("Error", "Error while saving file")

        finally:
            f.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About", "This is a text editor in python")

def quitApp():
    window.destroy()

window = Tk()
window.title("Text Editor")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("22")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="Color", command=changeColor)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=changeFont)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=changeFont)
size_box.grid(row=0, column=2)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quitApp)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About", command=about)




window.mainloop()