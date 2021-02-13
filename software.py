from tkinter import *
import StockProgram

def passValues():
    StockProgram.stockFunc(numberEntry.get(), stockEntry.get())

window = Tk()
window.title("Stock Software")
window.geometry("400x200+560+200")

title = Label(window, text="Live stock data in files", font=30, width=35, height=3)
title.grid(row=0, columnspan=2)

stockLabel = Label(window, text="Enter Stock Symbols (separated by commas):")
stockLabel.grid(row=1,column=0)

stockEntry = Entry(window)
stockEntry.grid(row=1,column=1)

numberLabel = Label(window, text="# of Files")
numberLabel.grid(row=2,column=0)

numberEntry = Entry(window)
numberEntry.grid(row=2,column=1)

blank = Label(window)
blank.grid(row=3, columnspan=2)

getButton = Button(window, text="GET DATA", command=lambda: passValues())
getButton.grid(row=4, columnspan=2)

window.mainloop()
