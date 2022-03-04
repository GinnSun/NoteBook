# Блокнот
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def open_file():
    file_open =  fd.askopenfilename()
    file = open(file_open)
    s = file.read() # считывает полностью весь файл
    user_text_join.insert(1.0, s)
    file.close() #После закрытия файла (файлового объекта)
    # для него более не будут доступны ни чтение, ни запись.
    # Попытка их произвести приведёт к возбуждению ValueError.
def save_file():
    filename = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('Python Files', '*.py; *.python'), ('All Files', '*.*')))
     #Опция filetype позволяет перечислить типы файлов,
    # которые будут сохраняться или открываться, и их расширения.
    open(filename, 'w').write(user_text_join.get('1.0', 'end'))
def press_key(event):
    UT = user_text.get()
    if event.char == '\r':
        user_text_join.insert(END,f'{UT}\n')
        user_text.delete(0, END)
    if not UT and event.char == '\r':
        messagebox.showinfo('Attention', 'You didnt enter anything in the input line!')

win = Tk()
win.title('Notebook')
win.geometry('700x700+590+60')
win.resizable(False, False)
#Entry
user_text = Entry(win,font=('Comic Sans MS',), width=55, relief=SOLID, bg='#FFFFFF')
user_text_join = Text(win, width=55, height=21, bg='#FFFFFF', relief=SOLID, wrap=WORD, font=('Comic Sans MS',),)
#Photo
photo_note = PhotoImage(file='notebook-438-818119.png')
win.iconphoto(False, photo_note)
#File menu
main_menu = Menu(win)
filemenu = Menu(main_menu, tearoff=0)
filemenu.add_command(label='Save file', command=save_file)
filemenu.add_command(label='Open File', command=open_file)
win.config(menu=main_menu, bg='#E4C0C0')
main_menu.add_cascade(label='File', menu=filemenu)
main_menu.add_cascade(label='Settings')
#Scroll
scroll_bar = Scrollbar(command=user_text_join.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
user_text_join.config(yscrollcommand=scroll_bar.set)
#Pack
user_text.pack(pady=5)
user_text_join.pack(pady=5)
#Bind
win.bind('<Key>', press_key)
win.mainloop()
