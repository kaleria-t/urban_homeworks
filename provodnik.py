import tkinter
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title= 'Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='grey')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=3, width=10, background='white')
text.grid(column=1, row=1)
button_select=tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='white', command=file_select)
button_select.grid(column=2, row=1)
window.mainloop()