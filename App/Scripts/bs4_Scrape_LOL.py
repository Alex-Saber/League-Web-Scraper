from selenium import webdriver
import bs4 as bs
import urllib.request
import pandas as pd
import pymongo
import sys

def grab_data():
    #Declaring variables
    num_champs = 0
    driver = webdriver.Chrome()
    driver.get('http://www.op.gg/statistics/champion/')
    #def grab_data():
    sauce = driver.page_source
    soup = bs.BeautifulSoup(sauce, 'lxml')
    champ_Stats = soup.find_all('td', class_=["ChampionName"])

    champ_names = list()
    champ_win_rate = list()
    champ_games_played = list()
    champ_KDA_ratio = list()
    champ_CS_earned = list()
    champ_gold_earned = list()
    for data in champ_Stats:
        champ_names.append(data.text.strip())
        data = data.find_next_sibling('td')
        champ_win_rate.append(data.text.strip())
        data = data.find_next_sibling('td')
        champ_games_played.append(data.text.strip())
        data = data.find_next_sibling('td')
        champ_KDA_ratio.append(data.text.strip())
        data = data.find_next_sibling('td')
        champ_CS_earned.append(data.text.strip())
        data = data.find_next_sibling('td')
        champ_gold_earned.append(data.text.strip())
        num_champs += 1
        print (data.text.strip())


    client = pymongo.MongoClient("mongodb://localhost")
    db = client.test
    db.champs.drop()
    db.create_collection('champs')
    champs = db.champs
    for i in range(0, num_champs): 
        champs.insert_one({'name': champ_names[i],
                            'win_rate': champ_win_rate[i],
                            'games_played': champ_games_played[i],
                            'KDA_ratio': champ_KDA_ratio[i],
                            'CS_earned': champ_CS_earned[i],
                            'gold_earned': champ_gold_earned[i]})

    return {'names': champ_names, 
            'win_rates': champ_win_rate, 
            'games_played': champ_games_played, 
            'KDA': champ_KDA_ratio, 
            'CS': champ_CS_earned, 
            'gold': champ_gold_earned }   
