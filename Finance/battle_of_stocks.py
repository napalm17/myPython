import yfinance as yf
import numpy as np
import random as rn
from matplotlib import pyplot as plt
from tkinter import *
import tkinter.font as font
from tkinter import ttk
import matplotlib.ticker as ticker


with open('symbols.txt', 'r') as f:
    l = f.read()
    l = l.split('\n')

pers = ["1d","5d","1mo","3mo","6mo","1y", "2y", "5y", "10y"]

class Company:
    amount = 100
    per_int = {"1d": "15m","5d": "1d","1mo": "1d","3mo":"1d","6mo":"1d","1y":"1d", "2y":"1wk", "5y":"1wk", "10y":"1wk"}
    def __init__(self, symbol, period):
        self.symbol = symbol
        self.period = period
    def get_date(self):
        company = yf.Ticker(self.symbol)
        self.data = company.history(period=self.period, interval=Company.per_int[self.period])
        return np.array(self.data.index)
    def get_price(self):
        self.close = np.array(self.data['Close'])
        try:
            coef = Company.amount / self.close[0]
        except:
            coef = Company.amount / self.close[2]
        return self.close * coef - Company.amount


def plotting(comp1, comp2, period):
    plt.close()
    myComp1 = Company(comp1, period)
    dates1 = myComp1.get_date()
    prices1 = myComp1.get_price()
    myComp2 = Company(comp2, period)
    dates2 = myComp2.get_date()
    prices2 = myComp2.get_price()

    plt.style.use('seaborn-whitegrid')

    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot()
    ax.set_title(f"{comp1} vs {comp2}")
    ax.plot(dates1, prices1, label=comp1, color="#F1C40F", lw="0.75")
    ax.plot(dates2, prices2, label=comp2, color="#4A235A", lw="0.75")
    ax.axhline(y=0, color='gray', linestyle='--')


    formatter = ticker.FormatStrFormatter("%1.2f%%")
    ax.yaxis.set_major_formatter(formatter)
    plt.gcf().autofmt_xdate()
    ax.set_ylabel('Price in %', loc='top')
    #date_format = mpl_dates.DateFormatter('%d %b %Y')
    #plt.gca().xaxis.set_major_formatter(date_format)
    ax.yaxis.tick_right()
    plt.legend()
    plt.tight_layout()
    plt.show()

def gui():
    root = Tk()
    root.geometry("+400+500")
    root.title("Battle of Stocks")
    general_font = ('Lato', 20)
    root.option_add("*Font", general_font)
    myfont = font.Font(size="50",family= "Lato")
    small = font.Font(size="1",family= "Lato")
    heading = Label(root, text=20*"-" + "Battle of Stocks" + 20*"-", pady=10, fg="#4A235A")
    heading.grid()
    mainframe = LabelFrame(root, padx=60)
    mainframe.grid()

    var1 = StringVar(mainframe)
    var1.set(rn.choice(l))
    var2 = StringVar(mainframe)
    var2.set(rn.choice(l))
    var3 = StringVar(mainframe)
    var3.set(pers[2])

    comp1 = ttk.Combobox(mainframe, textvariable=var1, values=l, width=8)
    comp1.grid(row=0, column=0, padx=10)
    vs = Label(mainframe,text="vs", padx=10, fg="#4A235A")
    vs.grid(row=0,column=1)
    comp2 = ttk.Combobox(mainframe, textvariable=var2, values=l, width=8)
    comp2.grid(row=0, column=2, padx=10)
    period = Label(mainframe,text="Period:", padx=10)
    period.grid(row=1,column=0, pady=20)
    per = ttk.Combobox(mainframe, textvariable=var3, values=pers, width=8)
    per.grid(row=1, column=2, padx=10)
    button = Button(mainframe,text="Show Results",padx=10,bg="#460D50", fg="#F1C40F",border=1,command=lambda: plotting(comp1.get(), comp2.get(), per.get()), relief="groove",overrelief="sunken",cursor="hand2")
    button.grid(row=2,columnspan=3, column=0,sticky=W+E)

    mainloop()
gui()