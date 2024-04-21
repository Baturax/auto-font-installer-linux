import tkinter as tk
from tkinter import filedialog, messagebox
import os

fontfolder = "myinstalledfonts"
folder = "~/.local/share/fonts"

os.system('clear')

if fontfolder not in os.listdir('/usr/share/fonts'):
    os.mkdir(f'{folder}{fontfolder}')

def install_font():
    selected_font = filedialog.askopenfilename(title='Select Font', filetypes=[('Font Files', '*.ttf'), ('Font Files', '*.otf')])
    if selected_font:
        font_name = os.path.basename(selected_font)
        os.system(f'cp "{selected_font}" "{folder}{fontfolder}/{font_name}"')
        os.system(f'fc-cache -f -v')
        messagebox.showinfo('Success', 'Font installed successfully!')

root = tk.Tk()
root.title('Install Font')
root.geometry('300x300')
root.resizable(False, False)

install_button = tk.Button(root, text='Install Font', command=install_font)
install_button.pack()

root.mainloop()