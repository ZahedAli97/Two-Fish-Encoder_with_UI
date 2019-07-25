from twofish import Twofish
import binascii
import math
import pandas
from Tkinter import Tk, Button, Label, Text, Message
import Tkinter as tk


inputs = []
encryptedinput = []
# decryptedinput = []


def inputmessage(inputmessage):
    for i in range(0, len(inputmessage), 16):
        tempinput = inputmessage[i:i+16]
        inputs.append(tempinput)

    for i in range(len(inputs)):
        if (len(inputs[i]) < 16):
            addinginput = inputs[i]
            while(len(addinginput) < 16):
                addinginput = addinginput + ' '
            inputs[i] = addinginput

    for i in range(len(inputs)):
        inputs[i] = str(inputs[i])
        inputs[i] = inputs[i].replace('\n', ' ')

    encrypting()


def encrypting():
    T = Twofish(b'*secret*')

    for i in range(len(inputs)):
        tempencrypted = T.encrypt(inputs[i])
        encryptedinput.append(tempencrypted)

    # encryptgui()


# def encryptgui():
#     encryptwindow = Tk()
#     encryptwindow.geometry("400x400")
#     encryptwindow.title('Encrypted Message')
#     exitbutton = Button(encryptwindow, text='Exit', width=25,
#                         command=encryptwindow.destroy)

#     # grid(row=0, column=0)
#     Label(encryptwindow, text="Encrypted Message : ").pack()

#     ourMessage = ''
#     for i in range(len(encryptedinput)):
#         ourMessage += encryptedinput[i]
#     messageVar = Message(encryptwindow, text=ourMessage)
#     messageVar.config(bg='lightgray')
#     messageVar.config(aspect=400)
#     messageVar.pack()

#     exitbutton.pack()  # place(relx=0.5, rely=0.9, anchor=tk.CENTER)

#     encryptwindow.mainloop()


# def decryptedinputs():
#     for i in range(len(encryptedinput)):
#         tempdecrypted = T.decrypt(encryptedinput[i])
#         decryptedinput.append(tempdecrypted)

#     for i in range(len(decryptedinput)):
#         decryptedinput[i] = str.rstrip(decryptedinput[i])
#         if i != 0 and decryptedinput[i][0] != ' ':
#             decryptedinput[i] = decryptedinput[i].rjust(
#                 len(decryptedinput[i])+1)


def inputgui():
    inputwindow = Tk()
    inputwindow.geometry("400x400")
    inputwindow.title('Input Message')
    exitbutton = Button(inputwindow, text='Exit', width=25,
                        command=inputwindow.destroy)

    Label(inputwindow, text="Input Message : ").grid(row=0, column=0)

    inputtext = Text(inputwindow, height=10, width=56,
                     bg='lightgray', highlightcolor='black')

    sendtbutton = Button(inputwindow, text='Send',
                         width=25, command=lambda: retrieve_input())

    encryptbutton = Button(inputwindow, text='Encrypt',
                           width=25, command=lambda: encrypt_input())

    inputtext.grid()

    sendtbutton.grid()

    encryptbutton.grid()

    exitbutton.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def retrieve_input():
        inputValue = inputtext.get("1.0", tk.END)
        inputmessage(inputValue)

    def encrypt_input():
        ourMessage = ''
        for i in range(len(encryptedinput)):
            ourMessage += encryptedinput[i]
        messageVar = Message(inputwindow, text=ourMessage)
        messageVar.config(bg='lightgray')
        messageVar.config(aspect=400)
        messageVar.grid()

    inputwindow.mainloop()


def outputgui():
    outputwindow = Tk()
    outputwindow.geometry("400x400")


if __name__ == '__main__':
    inputgui()
