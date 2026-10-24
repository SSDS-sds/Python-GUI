from tkinter import *
import random

player_score = 0
computer_score = 0

root = Tk()
root.geometry("700x300")
root.config(background="#36A58E")

root.title("Rocky vs Papier vs Scissory")
heading_lbl = Label(root, text="Rock, Paper, Scissors, Shoot!", bg="#36A58E", fg = "#F9D423", font = ("Fantasy", 35, "bold"))
heading_lbl.pack()

winner_lbl = Label(root, text = "Let the game begin!", bg = "#36A58E", fg = "#C01E28", font = ("Fantasy", 25))
winner_lbl.pack()

frame = Frame(root, bg = "#36A58E")
frame.pack()

options_lbl = Label(frame, text = "your options: ", bg = "#36A58E", fg = "#C5479C", font = ("Fantasy", 20))

options_lbl.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(frame, text = "ROCK", bg = "#5D4157", fg = "#FFFFFF", font = ("Crabbe"))












root.mainloop()