{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (1.5.1)\n",
      "Requirement already satisfied: packaging in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (20.4)\n",
      "Requirement already satisfied: astor in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (0.8.1)\n",
      "Requirement already satisfied: pandas>=0.21.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (1.0.5)\n",
      "Requirement already satisfied: blinker in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (1.4)\n",
      "Requirement already satisfied: python-dateutil in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (2.8.1)\n",
      "Requirement already satisfied: validators in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (3.19.4)\n",
      "Requirement already satisfied: toml in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (0.10.1)\n",
      "Requirement already satisfied: pympler>=0.9 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (7.2.0)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (0.7.1)\n",
      "Requirement already satisfied: attrs in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (19.3.0)\n",
      "Requirement already satisfied: cachetools>=4.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (5.0.0)\n",
      "Requirement already satisfied: tornado>=5.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (6.0.4)\n",
      "Requirement already satisfied: numpy in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (1.18.5)\n",
      "Requirement already satisfied: base58 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (2.1.1)\n",
      "Requirement already satisfied: requests in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (2.24.0)\n",
      "Requirement already satisfied: click>=7.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (7.1.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (3.1.26)\n",
      "Requirement already satisfied: altair>=3.2.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (4.2.0)\n",
      "Requirement already satisfied: pyarrow in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (7.0.0)\n",
      "Requirement already satisfied: tzlocal in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from streamlit) (4.1)\n",
      "Requirement already satisfied: six in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from packaging->streamlit) (1.15.0)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from packaging->streamlit) (2.4.7)\n",
      "Requirement already satisfied: pytz>=2017.2 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pandas>=0.21.0->streamlit) (2020.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from validators->streamlit) (4.4.2)\n",
      "Requirement already satisfied: ipykernel>=5.1.2; python_version >= \"3.4\" in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (5.3.2)\n",
      "Requirement already satisfied: traitlets>=4.3.2 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (4.3.3)\n",
      "Requirement already satisfied: jinja2>=2.10.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (2.11.2)\n",
      "Requirement already satisfied: ipywidgets>=7.0.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (7.5.1)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (3.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (2020.6.20)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (1.25.9)\n",
      "Requirement already satisfied: idna<3,>=2.5 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from requests->streamlit) (2.10)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from gitpython!=3.1.19->streamlit) (4.0.9)\n",
      "Requirement already satisfied: entrypoints in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.3)\n",
      "Requirement already satisfied: toolz in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.10.0)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (3.2.0)\n",
      "Requirement already satisfied: backports.zoneinfo; python_version < \"3.9\" in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from tzlocal->streamlit) (0.2.1)\n",
      "Requirement already satisfied: pytz-deprecation-shim in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from tzlocal->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: jupyter-client in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (6.1.6)\n",
      "Requirement already satisfied: appnope; platform_system == \"Darwin\" in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.1.0)\n",
      "Requirement already satisfied: ipython>=5.0.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (7.16.1)\n",
      "Requirement already satisfied: ipython-genutils in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from traitlets>=4.3.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jinja2>=2.10.1->pydeck>=0.1.dev5->streamlit) (1.1.1)\n",
      "Requirement already satisfied: nbformat>=4.2.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.0.7)\n",
      "Requirement already satisfied: widgetsnbextension~=3.5.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: setuptools in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (49.2.0.post20200714)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.16.0)\n",
      "Requirement already satisfied: tzdata; python_version >= \"3.6\" in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pytz-deprecation-shim->tzlocal->streamlit) (2021.5)\n",
      "Requirement already satisfied: pyzmq>=13 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jupyter-client->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (19.0.1)\n",
      "Requirement already satisfied: jupyter-core>=4.6.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jupyter-client->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (4.6.3)\n",
      "Requirement already satisfied: pickleshare in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
      "Requirement already satisfied: backcall in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (3.0.5)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pexpect; sys_platform != \"win32\" in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
      "Requirement already satisfied: jedi>=0.10 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.17.1)\n",
      "Requirement already satisfied: pygments in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
      "Requirement already satisfied: notebook>=4.4.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.0.3)\n",
      "Requirement already satisfied: wcwidth in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from pexpect; sys_platform != \"win32\"->ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
      "Requirement already satisfied: parso<0.8.0,>=0.7.0 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from jedi>=0.10->ipython>=5.0.0->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
      "Requirement already satisfied: nbconvert in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
      "Requirement already satisfied: Send2Trash in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
      "Requirement already satisfied: terminado>=0.8.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.3)\n",
      "Requirement already satisfied: prometheus-client in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.0)\n",
      "Requirement already satisfied: testpath in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.4.4)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.2)\n",
      "Requirement already satisfied: defusedxml in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
      "Requirement already satisfied: bleach in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.1.5)\n",
      "Requirement already satisfied: mistune<2,>=0.8.1 in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
      "Requirement already satisfied: webencodings in /Users/spandanatammineedi/Desktop/Anaconda/anaconda3/lib/python3.8/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-10-c7a1b683aa76>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-c7a1b683aa76>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    streamlit hello\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit hello"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "EOL while scanning string literal (<ipython-input-4-fa2d135cda3c>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-fa2d135cda3c>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    Hello *World!*\"\"\"\")\u001b[0m\n\u001b[0m                       \n^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m EOL while scanning string literal\n"
     ]
    }
   ],
   "source": [
    "st.write(\"\"\"# My First App\n",
    "          Hello *World!*\"\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
