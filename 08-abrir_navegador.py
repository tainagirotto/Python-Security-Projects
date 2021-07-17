# ferramenta gráfica para abrir navegador

import webbrowser
from tkinter import *

# criar um objeto para representar o tkinter:
root = Tk( )
root.title('Abrir Browser')
root.geometry('300x200') #tamanho

def google():
    webbrowser.open('https://www.google.com/')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20) #o command chama a função

# abrir o programa
root.mainloop()

