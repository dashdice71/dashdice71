{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3b6a639b-d2e8-47f3-9f38-7e027afae79e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlitNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "  Downloading streamlit-1.3.0-py2.py3-none-any.whl (9.2 MB)\n",
      "Requirement already satisfied: attrs in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (21.2.0)\n",
      "Collecting gitpython!=3.1.19\n",
      "  Downloading GitPython-3.1.24-py3-none-any.whl (180 kB)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (1.3.3)\n",
      "Collecting click<8.0,>=7.0\n",
      "  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (8.3.1)\n",
      "Collecting altair>=3.2.0\n",
      "  Downloading altair-4.1.0-py3-none-any.whl (727 kB)\n",
      "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (3.17.2)\n",
      "Collecting pympler>=0.9\n",
      "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "Requirement already satisfied: numpy in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (1.21.2)\n",
      "Requirement already satisfied: toml in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: blinker in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (1.4)\n",
      "Collecting pyarrow\n",
      "  Downloading pyarrow-6.0.1-cp38-cp38-win_amd64.whl (15.5 MB)\n",
      "Collecting tzlocal\n",
      "  Downloading tzlocal-4.1-py3-none-any.whl (19 kB)\n",
      "Collecting pydeck>=0.1.dev5\n",
      "  Downloading pydeck-0.7.1-py2.py3-none-any.whl (4.3 MB)\n",
      "Requirement already satisfied: packaging in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (21.0)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: astor in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (0.8.1)\n",
      "Requirement already satisfied: watchdog in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (1.0.2)\n",
      "Collecting validators\n",
      "  Downloading validators-0.18.2-py3-none-any.whl (19 kB)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Collecting base58\n",
      "  Downloading base58-2.1.1-py3-none-any.whl (5.6 kB)\n",
      "Requirement already satisfied: requests in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from streamlit) (2.26.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: toolz in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.3)\n",
      "Requirement already satisfied: jsonschema in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.2.0)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)\n",
      "Requirement already satisfied: typing-extensions>=3.7.4.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19->streamlit) (3.10.0.2)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\n",
      "Requirement already satisfied: six>=1.9 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.16.0)\n",
      "Requirement already satisfied: ipykernel>=5.1.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\n",
      "Requirement already satisfied: traitlets>=4.3.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
      "Requirement already satisfied: ipywidgets>=7.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
      "Requirement already satisfied: ipython<8.0,>=7.23.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.27.0)\n",
      "Requirement already satisfied: ipython-genutils in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: debugpy<2.0,>=1.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.4.1)\n",
      "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: jupyter-client<8.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.0.1)\n",
      "Requirement already satisfied: decorator in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.1.0)\n",
      "Requirement already satisfied: jedi>=0.16 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.17.2)\n",
      "Requirement already satisfied: setuptools>=18.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (58.0.4)\n",
      "Requirement already satisfied: colorama in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.4.4)\n",
      "Requirement already satisfied: pickleshare in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
      "Requirement already satisfied: backcall in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\n",
      "Requirement already satisfied: pygments in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.10.0)\n",
      "Requirement already satisfied: nbformat>=4.2.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
      "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
      "Requirement already satisfied: widgetsnbextension~=3.5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
      "Requirement already satisfied: parso<0.8.0,>=0.7.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: jupyter-core>=4.6.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\n",
      "Requirement already satisfied: pyzmq>=13 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.2.1)\n",
      "Requirement already satisfied: nest-asyncio>=1.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.5.1)\n",
      "Requirement already satisfied: pywin32>=1.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jupyter-core>=4.6.0->jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (228)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from jsonschema->altair>=3.2.0->streamlit) (0.17.3)\n",
      "Requirement already satisfied: wcwidth in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
      "Requirement already satisfied: notebook>=4.4.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.4.3)\n",
      "Requirement already satisfied: terminado>=0.8.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.9.4)\n",
      "Requirement already satisfied: Send2Trash>=1.5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
      "Requirement already satisfied: nbconvert in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.1.0)\n",
      "Requirement already satisfied: argon2-cffi in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (20.1.0)\n",
      "Requirement already satisfied: prometheus-client in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.11.0)\n",
      "Requirement already satisfied: pywinpty>=0.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from terminado>=0.8.3->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.7)\n",
      "Requirement already satisfied: cffi>=1.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.14.6)\n",
      "Requirement already satisfied: pycparser in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.20)\n",
      "Requirement already satisfied: defusedxml in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
      "Requirement already satisfied: jupyterlab-pygments in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: mistune<2,>=0.8.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
      "Requirement already satisfied: testpath in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
      "Requirement already satisfied: bleach in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.0.0)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.3)\n",
      "Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.3)\n",
      "Requirement already satisfied: async-generator in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.10)\n",
      "Requirement already satisfied: webencodings in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from packaging->streamlit) (2.4.7)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests->streamlit) (1.26.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests->streamlit) (3.2)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests->streamlit) (2.0.4)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2021.5-py2.py3-none-any.whl (339 kB)\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Collecting backports.zoneinfo\n",
      "  Downloading backports.zoneinfo-0.2.1-cp38-cp38-win_amd64.whl (38 kB)\n",
      "Installing collected packages: tzdata, smmap, backports.zoneinfo, pytz-deprecation-shim, gitdb, validators, tzlocal, pympler, pydeck, pyarrow, gitpython, click, base58, altair, streamlit\n",
      "  Attempting uninstall: click\n",
      "    Found existing installation: click 8.0.1\n",
      "    Uninstalling click-8.0.1:\n",
      "      Successfully uninstalled click-8.0.1\n",
      "Successfully installed altair-4.1.0 backports.zoneinfo-0.2.1 base58-2.1.1 click-7.1.2 gitdb-4.0.9 gitpython-3.1.24 pyarrow-6.0.1 pydeck-0.7.1 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 smmap-5.0.0 streamlit-1.3.0 tzdata-2021.5 tzlocal-4.1 validators-0.18.2\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
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
   "execution_count": 5,
   "id": "a6f7bbcc-cb9f-4d8a-8024-b4051985fcb5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: yfinance in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (0.1.67)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: lxml>=4.5.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from yfinance) (4.6.3)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from yfinance) (2.26.0)\n",
      "Requirement already satisfied: numpy>=1.15 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from yfinance) (1.21.2)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from yfinance) (0.0.10)\n",
      "Requirement already satisfied: pandas>=0.24 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from yfinance) (1.3.3)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pandas>=0.24->yfinance) (2021.3)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from pandas>=0.24->yfinance) (2.8.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance) (1.16.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (3.2)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (1.26.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\lenovo\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (2021.10.8)\n"
     ]
    }
   ],
   "source": [
    "pip install yfinance"
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
