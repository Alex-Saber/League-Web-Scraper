import pymongo
import sys

# This method pulls data from the MongoDB to display on the Flask App
def get_data():
    
    # Creating Lists to return
    champ_names = list()
    champ_win_rate = list()
    champ_games_played = list()
    champ_KDA_ratio = list()
    champ_CS_earned = list()
    champ_gold_earned = list()


    # Connecting to MongoDB to collect statistics to display
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.test
    champs = db.champs

    # For each entry in the database collection grab the appropriate data
    # and add it to the appropriate list.
    for entry in champs.find(): 
        champ_names.append(entry['name'])
        champ_win_rate.append(entry['win_rate'])
        champ_games_played.append(entry['games_played'])
        champ_KDA_ratio.append(entry['KDA_ratio'])
        champ_CS_earned.append(entry['CS_earned'])
        champ_gold_earned.append(entry['gold_earned'])
    
    # Return a dictionary of the data that will be displayed on the Flask App
    return {'names': champ_names, 
            'win_rates': champ_win_rate, 
            'games_played': champ_games_played, 
            'KDA': champ_KDA_ratio, 
            'CS': champ_CS_earned, 
            'gold': champ_gold_earned }
