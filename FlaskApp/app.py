import json
import time
from flask import Flask, request, render_template
from pymongo import MongoClient
import pandas
import joblib
import datetime

app = Flask(__name__) # Create Flask app

client = MongoClient(host='db',port = 27017) # Create mongo client 
db = client.flaskappDB # Create Database
data=db.data


@app.route('/', methods=['GET', 'POST'])

def main():
    
    if request.method == "POST":
         
    # Load Random Forest model that we created
         rf = joblib.load('randomForest.pkl')
    # Create a new document inside the Database , Take user input 
         user={
        'ra':request.form.get("ra"),
        'dec':request.form.get("dec"),
        'u':request.form.get("u"),
        'g':request.form.get("g"),
        'r':request.form.get("r"),
        'i':request.form.get("i"),
        'z':request.form.get("z"),
        'redshift' : request.form.get('redshift'),
        'plate':request.form.get("plate"),
        'mjd': request.form.get("mjd"),
        
             }
        # Create dataframe for the user input
         X = pandas.DataFrame(user,index = [0, 1, 2, 3, 4, 5, 6 ,7, 8,9 ],columns = ['ra','dec','u','g','r','i','z','redshift','plate','mjd'])
        # Make prediction using the dataframe
         prediction ={'prediction':rf.predict(X)[0]}
        # upload prediction and timestamp 
         user.update(prediction)

         user.update({'timestamp':datetime.datetime.now()})
         #Insert the input to the database
         data.insert_one(user)
    else:
        prediction = ""

    return  render_template("design.html", output = json.dumps(prediction)) # render design 

@app.route('/history',methods=['GET','POST']) # Create API for the database
def get_history():
        
         _items = db.data.find()
         items = [item for item in _items ]
         return  render_template('history.html',items=items) # render history
 


if __name__ == '__main__':
    app.run(host='0.0.0',debug = True)