from flask import Flask, request, render_template
import bs4_Scrape_LOL
import get_Stats

app = Flask("Scrape")
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Home Page
@app.route('/')
# These parameters call store_data() to scrape and store the champion stats
# and get_data() to access the champion stats for display
def home():
    bs4_Scrape_LOL.store_data() 
    data = get_Stats.get_data()
    return render_template("home.html", data=data)
