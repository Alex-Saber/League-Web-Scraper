from selenium import webdriver
import bs4 as bs
import urllib.request
import pymongo
import sys

# This method stores the League of Legend Champion Statistics into the MongoDB Database
def store_data():

    # Creating chrome instance in order to connect to the desired webpage.
    driver = webdriver.Chrome()
    driver.get('http://www.op.gg/statistics/champion/')

    # Transfering webpage HTML into a BeautifulSoup4 object to parse it for data.
    sauce = driver.page_source
    soup = bs.BeautifulSoup(sauce, 'lxml')

    
    # Creating lists to store text data from OP.GG
    champ_names = list()
    champ_win_rate = list()
    champ_games_played = list()
    champ_KDA_ratio = list()
    champ_CS_earned = list()
    champ_gold_earned = list()
    
    # This gives us the table data tag for the League of Legends champion name entry 
    champ_Stats = soup.find_all('td', class_=["ChampionName"])

    # Inserting text data from the websites html into different lists
    # These lists will then be used to transfer the data into a MongoDB Database
    for data in champ_Stats:

        # Start by adding the name text into the champ_names list. 
        # Once the text is appended to the list iterate to the next table data tag.
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
    
    # Connecting to MongoDB Database in order to store scraped champion data
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.test
    db.champs.drop()
    db.create_collection('champs')
    champs = db.champs
    
    # For each champion create a new dictionary with all of its 
    # corresponding statistics and insert it into the MongoDB Database
    for i in range(0, 140): 
        champs.insert_one({'name': champ_names[i],
                            'win_rate': champ_win_rate[i],
                            'games_played': champ_games_played[i],
                            'KDA_ratio': champ_KDA_ratio[i],
                            'CS_earned': champ_CS_earned[i],
                            'gold_earned': champ_gold_earned[i]})

    return
