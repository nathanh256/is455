import os, requests, json
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
from sklearn import preprocessing
import sys

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGXdTwEAAAAAr2%2BC9Wi6GHR8%2Bk%2FiDL2AIHaC1I8%3D86fg9nIXAt2MFp0QP1sXU0q1VFKHAGaD1da68qG4X0glvGSh4D"

def response_health(r):
  if r.status_code != 200:
    raise Exception(
    "Request returned an error: {} {}".format(
      r.status_code, r.text
    )
  )
    
def bearer_oauth(r):
  r.headers["Authorization"] = f"Bearer {bearer_token}"
  return r

def send_request(url, params=None):
  '''Send Request (url) with optional params. Returns json'''
  if params == None:
    response = requests.request("GET", url, auth=bearer_oauth)
  else:
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
  print("Request response status: ", response.status_code)
  response_health(response)
  return response.json()

def get_user_id(name):
  import pandas as pd
  user_json = send_request(f"https://api.twitter.com/2/users/by/username/{name}?user.fields=public_metrics,username,id,verified")
  data = {}
  data['verified'] = user_json["data"]['verified']
  data['id'] = user_json["data"]['id']
  data['name'] = user_json["data"]['name']
  data['username'] = user_json["data"]['username']
  data['followers_count'] = user_json["data"]['public_metrics']['followers_count']
  data['following_count'] = user_json["data"]['public_metrics']['following_count']
  data['tweet_count'] = user_json["data"]['public_metrics']['tweet_count']
  data['listed_count'] = user_json["data"]['public_metrics']['listed_count']
  print(data)
  df_user = pd.DataFrame(data)

  df_user

  return df_user

def get_tweets_by_user(id):
  return df_tweets
