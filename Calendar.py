from tkinter import *
import calendar

def show_cal():
    new_root = Tk()
    new_root.geometry("550x600")
    new_root.title("cal_window")
    new_root.config(background = "#FAD185")
    # Fetch the calendar year
    year = int(year_box.get())
    cal = calendar.calendar(year)

    cal_lbl = Label(new_root, text = cal, background = "#FAD185", fg = "#000000", font = ("Consolas", 10, "bold"))
    cal_lbl.pack()

    new_root.mainloop()



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

show_btn = Button(root, text = "show", bg = "#EFC59B", fg = "#F04155", font = ("Calibri", 20, "bold"), width = 15, command = show_cal)
show_btn.pack(pady = 10)

exit_btn = Button(root, text = "exit", bg = "#EFC59B", fg = "#F04155", font = ("Calibri", 20, "bold"), width = 15)
exit_btn.pack(pady = 10)




















root.mainloop()