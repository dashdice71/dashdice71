{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6c5fa3f0-13be-426f-8d3f-82feac16e92a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import streamlit as st\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "90cff9ef-3bdc-4efa-ba27-f0037d6b944f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b6e593bf-b11e-4b70-bebe-13efa2eac6de",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "82e48fce-9b62-4bd6-b3af-054c8ef23c04",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c0fab207-4917-41ee-848f-2e7ead46dd7f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.write(\"\"\"\n",
    "# Simple Stock Price app\n",
    "\n",
    "Shown are the stock closing price and volume of Google!\n",
    "\n",
    "\"\"\")\n",
    "\n",
    "# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75\n",
    "# define the ticker symbol\n",
    "tickerSymbol = 'GOOGL'\n",
    "\n",
    "# get data on this ticker\n",
    "tickerData = yf.Ticker(tickerSymbol)\n",
    "\n",
    "# get historical prices for this ticker\n",
    "tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-05-31')\n",
    "\n",
    "# Open   High   Low   Close  Volume  Dividends  Stock Splits\n",
    "\n",
    "st.line_chart(tickerDf.Close)\n",
    "st.line_chart(tickerDf.Volume)                             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d45636fc-d969-4521-8098-c667168f8fad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
