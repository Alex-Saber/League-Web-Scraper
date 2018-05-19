import bs4 as bs
import urllib.request
import pandas as pd
import pymongo
import sys

def grab_data():
    #Getting Html from OP.GG for league data
    sauce = urllib.request.urlopen('http://www.op.gg/statistics/champion/').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    n = soup.find('div', id='ChampionStatsTable')

    client = pymongo.MongoClient("mongodb://localhost")
    db = client.test
    champs = db.champs
    champs.insert({'name':"Vayne",'win_rate':"60%"})
    
    return champs.find({'name':'Vayne'})[0]['name'] 
    #n = soup.find_all('tr')
    #for i in n:
        #print (i.prettify())

#print (soup.find_all('td'))
#champion_Stats = soup.find('div', id='ChampionStatsTable') #, class_='Row Top')
#for n in champion_Stats.find_children('td', class_="ChampionName"):
#    print (n)
#stats = champion_Stats.find_all('tr', class_="Row")

#for n in stats:
 #   print (n.name)
#champ_Name = stats.children[4]
#print (champ_Name)
#for stats in champion_Stats.children:
#    print (stats)

#for tr in champion_Stats.children:
#    print (tr.get_text())
#for tr in table_rows:
#    td = tr.find_all('td', class_='Cell ChampionName')
#    name = td.find('a')
#    print (name.text)
    
