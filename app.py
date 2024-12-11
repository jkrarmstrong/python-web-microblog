import datetime # for working with dates and times
import os # for interacting with operative system
from flask import Flask, render_template, request, url_for
from pymongo import MongoClient # for interaction with MongoDB
from dotenv import load_dotenv # for loading enviroment variables from a .env file
import calendar

load_dotenv() # loads variables from .env into enviroment

def create_app():
    app = Flask(__name__) # instance of Flask class
    client = MongoClient(os.getenv("MONGODB_URI")) # connect to db with URI from enviroment variable
    app.db = client.microblog # access "microblog" db and assign it to app.db


    @app.route("/", methods=["GET", "POST"]) # define route and methods accepted
    def home():

        if request.method == "POST": # if request is POST
            entry_content = request.form.get("content") # get content field from form
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d") # format date as YYYY-MM-DD
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date}) # insert new entry to db

        # list of entries with formatted date
        entries_with_date = [
            (
                entry["content"], # entry content
                entry["date"], # entry date
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d") # display date (e.g. Oct 21)
            )
            
            for entry in app.db.entries.find({}) # iterate collection of entries
        ]
        return render_template("home.html", entries=entries_with_date) # display html file with the entries

    

    # function will render a calender the user can choose a date from
    @app.route("/calendar/")
    def display_calender():
        return render_template("calendar.html")
    

    # function will render the actual blog posts from the desired date
    @app.route("/get_date", methods=["POST"])
    def get_date():
        selected_date = request.form["selected_date"]
        selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d")
            
        entries = [
            (
                entry["content"], # entry content
                entry["date"], # entry date
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d") # display date (e.g. Oct 21)
            )
            
            for entry in app.db.entries.find({}) # iterate collection of entries
        ]
        return render_template("date_entries.html", entries=entries)



    # function will render all recent blog posts
    @app.route("/recent/")
    def recent():
        return "Her kommer det tidligere poster"


    
    
    
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)    