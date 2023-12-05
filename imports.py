# standard libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.metrics.pairwise import *
from sklearn.preprocessing import *
from sklearn.pipeline import *
from sklearn.base import *

import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

import requests
from bs4 import BeautifulSoup

os.environ['SPOTIPY_CLIENT_SECRET']='dcffd029266947f1b019245ec3a8aabd'
os.environ['SPOTIPY_CLIENT_ID']='847de36f322d48cfb6b22f213925fd71'
os.environ['MONGO_USERNAME']='striver'
os.environ['MONGO_PASSWORD']='Fg08jbi49zxb8j3I'
