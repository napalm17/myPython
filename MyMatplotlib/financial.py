import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np
msft = yf.Ticker("FB")
comp2 = yf.Ticker("AMZN")


data = msft.history(period="1mo", interval="1h")
finance_date = list(data.index)
high = np.array(data['High'])
vol = data['Volume']

data2 = comp2.history(period="1mo", interval="1h")
finance_date2 = list(data2.index)
high2 = list(data2['High'])
vol2 = data2['Volume']

plt.style.use('ggplot')

#plt.yscale("symlog")
plt.plot(finance_date, high, linestyle='solid', label="google")
plt.plot(finance_date2, high2, linestyle='solid', label="apple")

plt.gcf().autofmt_xdate()

#plt.fill_between(finance_date, high)

date_format = mpl_dates.DateFormatter('%b %Y')
plt.gca().xaxis.set_major_formatter(date_format)

print([1, 3, 4, 5, 6][-1])
plt.tight_layout()
plt.legend()
plt.show()


