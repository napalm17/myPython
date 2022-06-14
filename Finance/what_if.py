import yfinance as yf
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from tkinter import *
import tkinter.font as font
from tkinter import ttk
import random as rn

with open('symbols.txt', 'r') as f:
    l = f.read()
    l = l.split('\n')
pers = ["1d","5d","1mo","3mo","6mo","1y", "2y", "5y", "10y"]

class Stock:
    per_int = {"1d": "15m", "5d": "1d", "1mo": "1d", "3mo": "1d", "6mo": "1d", "1y": "1d", "2y": "1wk", "5y": "1wk",
               "10y": "1wk"}
    def __init__(self, company, amount, period):
        self.company = company
        self.amount = amount
        self.period = period
    def get_date(self):
        comp = yf.Ticker(self.company)
        self.data = comp.history(period=self.period, interval=Stock.per_int[self.period])
        return np.array(self.data.index)
    def get_price(self):
        self.close = np.array(self.data['Close'])
        first = self.close[0]
        coef = self.amount / first
        return self.close * coef, round(coef, 2)

def plotting(comp, amo, per):
    prices, dates, first = 0, 0, 0
    try:
        myStock = Stock(comp, amo, per)
        dates = myStock.get_date()
        prices, first = myStock.get_price()
    except:
        print("failed")
    plt.close()
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot()
    ax.plot(dates, prices, label= comp, lw="0.75", color="#154360")
    delta = round(prices[-1] - amo, 2)
    gain_loss = "gained" if delta > 0 else "lost"
    ax.set_title(
        'You would have {}  {} USD, if you had bought {} USD worth of {} stocks ({} units) {} ago.'
            .format(gain_loss, delta, amo, comp, first, per))
    clr = "#28B463" if delta > 0 else "#CB4335"
    ax.plot([dates[-1], dates[-1]], [amo, prices[-1]], lw="3", color=clr, label=f'$ {delta}')

    plt.gcf().autofmt_xdate()
    ax.axhline(y=amo, color='gray', linestyle='--', lw="2")
    plt.fill_between(dates, amo, prices,
                     where=(prices < amo),
                     alpha=0.30, color='red', interpolate=True)
    plt.fill_between(dates, prices, amo,
                     where=(prices >= amo),
                     alpha=0.30, color='green', interpolate=True)

    date_format = mpl_dates.DateFormatter('%d %b %Y')
    #plt.gca().xaxis.set_major_formatter(date_format)
    #formatter = ticker.FormatStrFormatter('$ %1.2f')
    #ax.yaxis.set_major_formatter(formatter)
    ax.yaxis.tick_right()
    plt.legend()
    plt.tight_layout()
    plt.show()

def gui():
    root = Tk()
    root.geometry("+400+500")
    root.title("How much would I have made")
    general_font = ('Lato', 20)
    root.option_add("*Font", general_font)
    myfont = font.Font(size="50",family= "Lato")
    small = font.Font(size="1",family= "Lato")
    heading = Label(root, text=10*"-" + "How much would I have made?" + 10*"-", pady=10, fg="#0E6655")
    heading.grid()
    mainframe = LabelFrame(root)
    mainframe.grid()
    var1 = StringVar(mainframe)
    var1.set(rn.choice(l))
    var3 = StringVar(mainframe)
    var3.set(pers[2])
    am_var = IntVar(mainframe)
    am_var.set(1000)
    lbl = Label(mainframe,text="Company:", padx=10, fg="#0E6655")
    lbl.grid(row=0,column=0, sticky=E)
    comp1 = ttk.Combobox(mainframe, textvariable=var1, values=l, width=8)
    comp1.grid(row=0, column=1, padx=10, sticky=W)
    amount = Label(mainframe,text="Entry Money (USD):", padx=10, fg="#0E6655")
    amount.grid(row=1,column=0, pady=10, sticky=E)
    ent = Entry(mainframe, textvariable=am_var, width=9)
    ent.grid(row=1, column=1, padx=10, sticky=W)
    period = Label(mainframe,text="Period:", padx=10, fg="#0E6655")
    period.grid(row=2,column=0, sticky=E)
    per = ttk.Combobox(mainframe, textvariable=var3, values=pers, width=8)
    per.grid(row=2, column=1, padx=10, sticky=W)
    sm = Label(mainframe, text=100*" ")
    sm.grid(row=3, columnspan=2)
    button = Button(mainframe,text="Calculate",padx=10,bg="#45B39D", fg="#E5E7E9",border=1,
                    command=lambda: plotting(comp1.get(), int(ent.get()), per.get()), relief="groove",overrelief="sunken",cursor="hand2")
    button.grid(row=4,columnspan=2, column=0,sticky=W+E+N)

    mainloop()

gui()

