import os
from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image
import pytesseract

# Create the main window
root= Tk()
root.geometry('350x200')
root.resizable(0,0)
root.title('Photo To Text Converter Doruk Tarhan')

# Define exit function to close the application
def exit():
    root.destroy()

# Define function to convert image to text
def convert_to_text():
    # Define file types that the user can open
    filetypes = (('JPG files', '*.jpg'),('PNG files', '*.png'))

    # Open file dialog and store the selected filename
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    
    # Show a message box with the selected file name
    showinfo(title='Selected File',message=filename)
    
    # Get the base name of the file
    basename = os.path.basename(filename)

    # Get the selected language and replace the string with the appropriate language code
    language = language_combo.get()
    if language=='English':
        language=language.replace('English','eng')
    elif language=='German':
        language=language.replace('German','deu')
    elif language=='French':
        language=language.replace('French','fra')
    elif language=='Italian':
        language=language.replace('Italian','ita')
    elif language=='Spanish':
        language=language.replace('Spanish','spa')
    elif language=='Turkish':
        language=language.replace('Turkish','tur')
    elif language=='Ukrainian':
        language=language.replace('Ukrainian','ukr')
    elif language=='Romanian':
        language=language.replace('Romanian','ron')

    # Convert the image to text using pytesseract
    a=pytesseract.image_to_string(Image.open(basename),lang=language)
    
    # Show a message box with the converted text and ask the user if they want to save the file
    response = messagebox.askyesno('Press Yes To Save The File Or No To Quit',a)
    if response == True:
        file=f'{basename}.txt'
        with open(file,'w',encoding='utf-8') as f:
            f.write(a)
        # Show a message box informing the user that the file is saved
        messagebox.showinfo('The File is saved',f'The file of {file} is saved into your directory of {os.getcwd()}')
    else:
        # Show a message box informing the user that the file is not saved
        messagebox.showinfo('The File is not saved',f'The file is not saved')

# Create a font for the labels and buttons
helv36 = font.Font(family='Helvetica',size=16, weight='bold')

# Create a frame for the labels and buttons
dosya_frame=Frame(root,width=350, height=200,bg='white') # Change background color to white
dosya_frame.place(x=0,y=0)

# Create a label and a combo box for the language selection
language_options=['English','Turkish']
category_label=Label(dosya_frame, text = 'Select Language=>',font=helv36, bg='white', fg='black') # Change text color to black
category_label.place(x=15, y=50)
language_combo = ttk.Combobox(dosya_frame, value=language_options,font=helv36,width=8)
language_combo.current(0)
language_combo.place(x=215, y=50)

# Create a button to execute the conversion process after selecting language
open_button2 = Button(dosya_frame,text='Choose Photo &\n Convert To Text',width=15, height=2,command=convert_to_text)
open_button2['font']=helv36
open_button2.place(x=70, y=100)

root.mainloop()

