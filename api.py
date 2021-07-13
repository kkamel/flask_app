
import csv
import sqlite3
import time

from datetime import datetime
from dask import dataframe as dd
from markupsafe import escape

from flask import Flask, current_app, g, render_template
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from .models import db, Player


app = Flask(__name__)
api = Api(app)

data_file = "People.csv"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
# Intialize DB
#db = SQLAlchemy(app)

# Data files
fields = []
row_table = {}
players = {}

cache = {}
CACHE_SIZE = 1000

@app.before_first_request
def create_tables():
    #read_verylarge_csv(data_file)
    db.init_app(app)
    db.create_all()
    read_csv(data_file)

parser = reqparse.RequestParser()

@app.route('/')
def index():
    return 'Players API'

@app.route('/players', methods=["GET"])
def list_players():
    players = {}
    not_cached = []

    if len(cache) == 0:
        result = Player.query.order_by(Player.playerID).all()
        print("loading into cache", len(result))
        for player in result:
            #print(type(player))
            if len(cache) < CACHE_SIZE:
                cache[player.playerID] = str(player)
            else:
                not_cached = player.id
            players[player.playerID] = str(player)
            
        if result:
            print("success", len(result))
        else:
            print("failure")

    else:

        #result = Player.query.order_by(Player.playerID).all()
        

        for player_id, attrs in cache.items():
            players[player_id] = str(attrs)

        for id, player in not_cached.items():
            player = Player.query.get(id)
            players[player_id] = str(player)

        print ("retruning from cache")
    
    return players, 200
   
@app.route('/players/<player_id>', methods=["GET"])
def retrieve_player(player_id):
    result = Player.query.filter_by(playerID=player_id).first()
    print(result)
    if not result:
        return "Player Not found", 404    
    return str(result), 200


@app.route('/players/<player_id>/weight', methods=["PUT"])
def increment_weight(player_id):
    player = Player.query.filter_by(playerID=player_id).first()
    if not player:
        return "Player Not found", 404
    print("found player")
    player.weight += 1
    print("incremented weight")
    db.session.commit()
    print("commited to DB")
    return str(player)


@app.route('/players/<player_id>/height', methods=["PUT"])
def increment_height(player_id):
    player = Player.query.filter_by(playerID=player_id).first()
    if not player:
        return "Player Not found", 404
    player.height += 1
    db.session.commit()
    return str(player)


def read_csv(filepath):
    print("read csv")
    # reading csv file
    with open(filepath, 'r') as csvfile:
        # create a csv reader object
        csvreader = csv.reader(csvfile)
          
        # extract fields from first line
        fields = next(csvreader)
      
        # extract each line
        for row in csvreader:

            populate_DB(row)
            #print (row)

            players[row[0]] = row
      
        # get total number of rows
        print("Total no. of rows: %d"%(csvreader.line_num))
    
    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

''' Dask utilizes multiple CPU cores by internally chunking dataframe and process in parallel.
 It can be parallelized on a single machine or distributed processing system. Dask uses
lazy computation by creating a graph of tasks and then invokes a compute() function when invoked.
'''  
def read_verylarge_csv(filepath):
    start = time.time()
    dask_df = dd.read_csv(filepath)
    end = time.time()
    print("Read csv with dask: ",(end-start),"sec")


def populate_DB(row):
    if row[16] != '':
        row[16] = int(row[16])
    if row[17] != '':
        row[17] = int(row[17])

    player = Player(playerID=row[0], birthYear=row[1], birthMonth=row[2], birthDay=row[3], \
        birthCountry=row[4], birthState=row[5], birthCity=row[6], deathYear=row[7],\
        deathMonth=row[8], deathDay=row[9], deathCountry=row[10], deathState=row[11],\
        deathCity=row[12], nameFirst=row[13], nameLast=row[14], nameGiven=row[15], \
        weight=row[16], height=row[17], bats=row[18], throws=row[19], debut=row[20],\
        finalGame=row[21], retroID=row[22], bbrefID=row[23])
    
    db.session.add(player)
    db.session.commit()

'''
api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')
'''
if __name__ == "__main__":
    create_tables()
    app.run(host='localhost', port=5000, debug=True)

