import yfinance as yf
import numpy as np
import random as rn
from matplotlib import pyplot as plt, dates as mpl_dates
from tkinter import *
import tkinter.font as font
from tkinter import ttk


with open('symbols.txt', 'r') as f:
    l = f.read()
    l = l.split('\n')

class Stock:
    per_int = {"3mo":"1d","6mo":"1d","1y":"1d", "2y":"1d"}
    def __init__(self, symbol, period):
        self.symbol = symbol
        self.period = period
    def get_date(self):
        company = yf.Ticker(self.symbol)
        self.data = company.history(period=self.period, interval=Stock.per_int[self.period])
        return np.array(self.data.index)
    def get_price(self):
        self.close = np.array(self.data['Close'])
        self.open = np.array(self.data['Open'])
        return self.open, self.close
    def get_average(self, time):
        self.avg = np.array([])
        for i in range(len(self.close)):
            total = 0
            for j in self.close[i-time:i]:
                total += j
            if total != 0:
                self.avg = np.append(self.avg, total / time)
        return self.avg

def plotting(comp, period):
    plt.close()
    myComp = Stock(comp, period)
    dates = myComp.get_date()
    open, close = myComp.get_price()
    avg5 = myComp.get_average(5)
    avg10 = myComp.get_average(10)
    avg30 = myComp.get_average(30)

    plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot()
    ax.set_title(comp)

    for t, open, close in zip(dates, open, close):
        color = "#ec7063" if close < open else "#58d68d"
        linewidth = "3" if "y" in period else "6"
        ax.plot([t, t], [open, close], color=color, lw=linewidth)
    ax.plot(dates[len(dates) - len(avg5):], avg5, label="5 day average", lw="0.75", color="#f39c12")
    ax.plot(dates[len(dates)-len(avg10):], avg10, label="10 day average", lw="0.75", color="#2980b9")
    ax.plot(dates[len(dates) - len(avg30):], avg30, label="30 day average", lw="0.75", color="#7d3c98")

    plt.gcf().autofmt_xdate()
    ax.set_ylabel('Price in USD', loc='top')
    date_format = mpl_dates.DateFormatter('%d %b %Y')
    plt.gca().xaxis.set_major_formatter(date_format)
    ax.yaxis.tick_right()
    plt.legend()
    plt.tight_layout()
    plt.show()

def gui():
    root = Tk()
    root.geometry("+400+500")
    root.title("Show Averages")
    general_font = ('Lato', 20)
    root.option_add("*Font", general_font)
    myfont = font.Font(size="50",family= "Lato")
    small = font.Font(size="1",family= "Lato")
    heading = Label(root, text=10*"-" + "Candlestick Stock Chart" + 10*"-", pady=10, fg="#34495e")
    heading.grid()
    mainframe = LabelFrame(root, padx=60)
    mainframe.grid()
    pers = ["3mo","6mo","1y", "2y"]
    var1 = StringVar(mainframe)
    var1.set(rn.choice(l))
    var3 = StringVar(mainframe)
    var3.set(pers[2])
    comp_name = Label(mainframe,text="Company:", padx=10)
    comp_name.grid(row=0,column=0, pady=20)
    comp1 = ttk.Combobox(mainframe, textvariable=var1, values=l, width=8)
    comp1.grid(row=0, column=1, padx=10)
    period = Label(mainframe,text="Period:", padx=10)
    period.grid(row=1,column=0, pady=20)
    per = ttk.Combobox(mainframe, textvariable=var3, values=pers, width=8)
    per.grid(row=1, column=1, padx=10)
    button = Button(mainframe,text="Show Results",padx=10,bg="#34495e", fg="#f2f3f4",border=1,
                    command=lambda: plotting(comp1.get(), per.get()), relief="groove",overrelief="sunken",cursor="hand2")
    button.grid(row=2,columnspan=3, column=0,sticky=W+E)

    mainloop()

gui()






