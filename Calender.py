from tkinter import *
import calendar

root = Tk()
root.geometry("350x400")
root.config(background= "#CFF477")
root.title("calendar")

heading_lbl = Label(root, text = "calendar", bg = "#CFF477", fg = "#4A0E0E", font = ("Calibri", 35, "bold"))
heading_lbl.pack()

year_lbl = Label(root, text = "Enter your year: ", bg = "#CFF477", fg = "#532F76", font = ("Calibri", 20))
year_lbl.pack(pady = 15)

year_box = Entry(root, justify = "center")
year_box.pack(pady = 15)

show_btn = Button(root, text = "show", bg = "#EFC59B", fg = "#F04155", font = ("Calibri", 20, "bold"), width = 15)
show_btn.pack(pady = 10)

exit_btn = Button(root, text = "exit", bg = "#EFC59B", fg = "#F04155", font = ("Calibri", 20, "bold"), width = 15)
exit_btn.pack(pady = 10)
root.mainloop()