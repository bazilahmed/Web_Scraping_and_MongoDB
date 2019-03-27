
# program to load mars data to MongoDB 
import pymongo
import json
from pprint import pprint
import os
from flask import Flask, jsonify, render_template, redirect

# import the mars scraping script
import scrape_mars

# create a connection
conn = "mongodb://localhost:27017"

# pass connnection to the pymongo instance
client = pymongo.MongoClient(conn)

# connect to a database. It will create one if not already exists
db = client.mars

# drop collections if exists 
db.mars_data.drop()


########################################################
# Flask app

app = Flask(__name__)

@app.route('/scrape')
def scrape():
    mars_scraped_data = scrape_mars.scrape()
    # upsert data to mars_data collection
    db.mars_data.update({}, mars_scraped_data, upsert=True)
    # Redirect back to home page
    return redirect("/")

@app.route('/')
def index():
    mars_data_from_mongo = db.mars_data.find_one()
    return render_template("index.html", mars_d=mars_data_from_mongo)





if __name__ == "__main__":
    app.run(debug=True)

