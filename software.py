from tkinter import *
import StockProgram

# pass the desired stock tickers and the amount of desired output files into the StockProgram, which will grab and output the data
def passValues():
    StockProgram.stockFunc(numberEntry.get(), stockEntry.get())
    
# create a new window, and add labels, entries, and button for use
window = Tk()
window.title("Stock Software")
window.geometry("400x200+560+200")
window.config(bg="white")

title = Label(window, text="Live stock data in files", font=30, width=35, height=3,bg="white")
title.grid(row=0, columnspan=2)

stockLabel = Label(window, text="Enter Stock Symbols (separated by commas):")
stockLabel.grid(row=1,column=0)

# entry bar for the stock symbols, separated by commas 
stockEntry = Entry(window)
stockEntry.grid(row=1,column=1)

numberLabel = Label(window, text="# of Files:")
numberLabel.grid(row=2,column=0)

# entry bar for the number of desired output files
numberEntry = Entry(window)
numberEntry.grid(row=2,column=1)

blank = Label(window,bg="white")
blank.grid(row=3, columnspan=2)

# create files with currently inputted data
getButton = Button(window, text="GET DATA", command=lambda: passValues())
getButton.grid(row=4, columnspan=2)

window.mainloop()
