from tkinter import *

root = Tk()
root.geometry("350x400")
root.config(background= "#CDB953")
root.title("square calculator")

def calc_area():
    area = int(width.get())*int((length.get())) 
    unit_used = unit.get()
    answer = Label(root, text = "Area: "+ str(area) + " " + unit_used + "²", background = "#CDB953", fg = "#000000", font = ("Consolas", 10, "bold"))
    answer.pack()

def calc_peri():
    peri = 2*(int(width.get()) + int(length.get()))
    unit_used = unit.get()
    answer = Label(root, text = "Perimeter: "+ str(peri) + " " + unit_used, background = "#CDB953", fg = "#000000", font = ("Consolas", 10, "bold"))
    answer.pack()


heading_lbl = Label(root, text = "SQUARE CALCULATOR", bg = "#CDB953", fg = "#000000", font = ("Calibri", 28, "bold"))
heading_lbl.pack()

width_lbl = Label(root, text = "WIDTH", bg = "#CDB953", fg = "#0E2E4A", font = ("Calibri", 15))
width_lbl.pack()

width = Entry(root, justify = "center")
width.pack()

length_lbl = Label(root, text = "LENGTH", bg = "#CDB953", fg = "#4A0E0E", font = ("Calibri", 15))
length_lbl.pack()

length = Entry(root, justify = "center") 
length.pack()

unit_lbl = Label(root, text = "UNIT", bg = "#CDB953", fg = "#E5FF00", font = ("Calibri", 15))
unit_lbl.pack()

unit = Entry(root, justify = "center") 
unit.pack() 

calc_area_button = Button(root, text = "Calculate area", bg = "#EB3737", fg = "#F6BABA", font = ("Calibri", 18, "bold"), width = 15, command = calc_area)
calc_area_button.pack(pady = 5) 

calc_peri_button = Button(root, text = "Calculate perimeter", bg = "#3779EB", fg = "#F6BABA", font = ("Calibri", 18, "bold"), width = 15, command = calc_peri)
calc_peri_button.pack(pady = 1) 

root.mainloop()