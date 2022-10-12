
import pandas as pd
import requests
import json
import hashlib

address="http://gateway.marvel.com/v1/public/characters"
private_key = input("Enter private Key: ")
public_key = input(" Enter public Key: ")
Hash= input("Enter Hash Key: ")
ts='2'
o=[]
p=[]

n=0
for i in range(4):
    param={'apikey' : public_key,
    'nameStartsWith': 'Sp',
    'ts' : ts,
    'hash' : Hash, 'offset': n,
    'limit' : 100}
    n+=100
    headers = {'Content-Type':'application/json'}
    response = requests.get(address,params=param,headers=headers)

    res = response.json()

    for i in res['data']['results']:
      o.append(i['id'])
      o.append(i['name'])
      o.append(i['description'])
      o.append(i['comics']['available'])
      o.append(i['series']["available"])
      o.append(i["stories"]["available"])
      o.append(i["events"]["available"])
      p.append(o)
      o=[]
    



df = pd.DataFrame(p,columns=['id','Character_Name','Description','Comics','Series','Stories','Events'])



def marvel_function(api_key,Hash,namewith):
        address="http://gateway.marvel.com/v1/public/characters"
        a=[]
        b=[]

        n=0
        for i in range(4):
            param={'apikey' : api_key,
            'nameStartsWith': namewith,
            'ts' : '2',
            'hash' : Hash, 'offset': n,
            'limit' : 100}
            n+=100
            headers = {'Content-Type':'application/json'}
            response = requests.get(address,params=param,headers=headers)

            res = response.json()

            for i in res['data']['results']:
              a.append(i['id'])
              a.append(i['name'])
              a.append(i['description'])
              a.append(i['comics']['available'])
              a.append(i['series']["available"])
              a.append(i["stories"]["available"])
              a.append(i["events"]["available"])
              b.append(a)
              a=[]
        df = pd.DataFrame(b,columns=['id','Character_Name','Description','Comics','Series','Stories','Events'])
        print(df)
        return df
        


try:
    DF=marvel_function("aed34f7c818eef7f79d97081349c1620",Hash,'sp')
except:
    print("error of parameters!!")



def filter_marvel(DataFr,col,Cond):
    if Cond[0]=='g':
        print(DataFr[DataFr[col]>Cond[1]])
    elif Cond[0] == 'ge':
        print(DataFr[DataFr[col]>=Cond[1]])
    elif Cond[0] == 'e':
        print(DataFr[DataFr[col]==Cond[1]])
    elif Cond[0] == 'le':
        print(DataFr[DataFr[col]<=Cond[1]])
    else:
        print(DataFr[DataFr[col]<Cond[1]])
    



filter_marvel(df,"Series",['g',20])





