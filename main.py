import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from run_analysis import *



#define global variable
filename=''
# Create window Tkinter
window = tk.Tk()
 
# Name our Tkinter application title
window.title(" vehicles analysis tool ")
 
# Define window size in Tkinter python
window.geometry("700x500")
 
# Create a label widget in Tkinter
label = tk.Label(window, text="Welcome to vehicles monitoring system",
font=('Calibri 15 bold'))
label.pack(pady=20)


# def select_file():
#     filetypes = (
#         ('text files', '*.mp4'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)

    

# open_button = tk.Button(
#     window,
#     text='Open a File',
#     command=select_file
# )
# open_button.pack(expand=True)


def on_click_btn1():
    filetypes = (
        ('text files', '*.mp4'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    if filename != '':
        my_video_analyser(filename)
    else:
      showinfo(
        title='Selected File',
        message='You have not select any video, Please select a Video.'
    )      
     
# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked second button"
     
# Create 1st button to update the label widget
btn1 = tk.Button(window, text="Start Analysis", command=on_click_btn1)
#btn1.pack(pady=20)
btn1.pack(padx = 1, pady = 1,anchor='ne')
btn1.place( x = 20, y = 80) 
# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="All Video", command=on_click_btn2)
btn2.pack(padx = 1, pady = 1,anchor='ne')
btn2.place(x = 20, y = 120)
 
# Run main loop
window.mainloop()