# from fastapi import FastAPI
# import torch
import requests
import json


URL =  'http://localhost:8080/2015-03-31/functions/function/invocations'


sample_json = {
  "time_series": [
    {
      "open": 2,
      "high": 0,
      "low": 0,
      "close": 0,
      "vol": 0,
      "value": 0,
      "agg_price": 0,
      "foreign_rate": 0,
      "agency_buy": 0,
      "agency_netbuy": 0
    },
		{
      "open": 1,
      "high": 0,
      "low": 0,
      "close": 0,
      "vol": 0,
      "value": 0,
      "agg_price": 0,
      "foreign_rate": 0,
      "agency_buy": 0,
      "agency_netbuy": 0
    }
  ]
}

response = requests.post(url= URL, json= sample_json)
body = response.json()['body']
prediction = json.loads(body)['prediction']

print(prediction)

# body = json.loads(response.json()['body'])

# # prediction 값을 추출
# prediction = json.loads(body['prediction'])
# print(prediction)
