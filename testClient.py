import requests
import json
import random
import time
from time import gmtime, strftime
import datetime
import threading
import numpy as np
import pdb
gServerUrl = 'http://localhost:3000/v2'


def query1(serverName='Test', severity=0):
    #pdb.set_trace()
    url = gServerUrl + '/alarm/query?limit=100&offset=0'
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {"ServerName":serverName, "Severity":severity}
    ss = requests.session()
    d = ss.post(url, headers = headers, data = json.dumps(data) );
    jd = json.loads(d.content)

    
def postData():
    url = 'http://localhost:8081/alarm'
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    time1 = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
    ss = requests.session()
    print(time1)
    for i in range(10000):
        s1 = str(i)
        s2 = str( random.random() )
        data = {
          "TicksTimeStamp": time.time() * 1000,
          "EventCategory": "digital",
          "Message": "Message" + s2,
          "Priority": "high",
          "SourceID": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
          "SourceName": "SourceName"+ s2,
          "Severity": i,
          "SourcePath": "SourcePath" + s2 ,
          "State": i%100,
          "Quality": i%1000,
          "ServerName": "ServerName",
          "EventID": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
          "EventTimeStamp": strftime("%Y-%m-%dT%H:%M:%S.000+00:00", gmtime())
        }
        s = json.dumps(data)
        d = ss.post(url, headers=headers, data=s)
        print(d)
        
    time2 = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
    print(time2-time1)
    
postData()