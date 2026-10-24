from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("temp converta")
root.config(background = "#DAF038")

def convert():
    celsius = float(temp_box.get())
    f = (celsius*9/5)+32
    result_lbl.config(text=f"{celsius}°C is equal to {f}°F")



heading_lbl = Label(root, text = "Temperature Converter", bg = "#DAF038", fg = "#000000", font = ("Arial", 25, "bold"))
heading_lbl.pack()

temp_lbl = Label(root, text = "temperature enter: ", bg = "#DAF038", fg = "#821902", font = ("Arial", 18))
temp_lbl.pack(pady = 15)

temp_box = Entry(root, justify = "center", font = ("Arial", 25))
temp_box.pack(pady = 5)

convert_btn = Button(root, text = "CONVERT", bg = "#AAB0F9", fg = "#fa1015", font = ("Fantasy", 20, "bold"), command = convert)
convert_btn.pack(pady = 10)

result_lbl = Label(root, text = "", bg = "#DAF038", fg = "#7183C6", font = ("Arial", 20))
result_lbl.pack(pady = 10)
root.mainloop()