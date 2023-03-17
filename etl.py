import requests
import pandas as pd
import os

def extract():
    df1 = pd.read_csv('https://www.football-data.co.uk/mmz4281/1920/E0.csv')
    df1.to_csv('raw/E0_raw.csv',index=False)
    df2 = pd.read_csv('https://www.football-data.co.uk/mmz4281/1920/E2.csv')
    df2.to_csv('raw/E2_raw.csv',index=False)
    df3 = pd.read_csv('https://www.football-data.co.uk/mmz4281/1920/E1.csv')
    df3.to_csv('raw/E1_raw.csv',index= False)

def transform():
    df1_transform = pd.read_csv("raw/E0_raw.csv")
    df1_transform = df1_transform[["Div","Date","Time","HomeTeam","AwayTeam","FTHG","FTAG"]]
    df1_transform.to_csv("transform/E0_transform.csv",index=False)
    
    df2_transform = pd.read_csv("raw/E2_raw.csv")
    df2_transform = df1_transform[["Div","Date","Time","HomeTeam","AwayTeam","FTHG","FTAG"]]
    df2_transform.to_csv("transform/E2_transform.csv",index=False)
    
    df3_transform = pd.read_csv("raw/E1_raw.csv")
    df3_transform = df1_transform[["Div","Date","Time","HomeTeam","AwayTeam","FTHG","FTAG"]]
    df3_transform.to_csv("transform/E1_transform.csv",index=False)
    finaldFF = pd.concat([df1_transform,df2_transform,df3_transform])
    return finaldFF


