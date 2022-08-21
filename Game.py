# from tkinter import *
# root = Tk()

# my_label = Label(root, text = "testing testing 1123")

# my_label.pack()

# root.mainloop()

response = ""

start = input("Welcome to my game, Type 'start' to start")\


def startGame():

    name = input("what is your name ")

    print("welcome" + name)

if start == "start":
    startGame()