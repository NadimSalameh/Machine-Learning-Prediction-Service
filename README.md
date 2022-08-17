# Machine-Learning-Prediction-Service
Train a RandomForestClassifier for prediction making, save the model in a Binary file then create a REST API using Flask in a Docker container. When there is a prediction made, the Flask app responds to the prediction request with JSON, and store the timestamp, input values and prediction result in MongoDB.

## Authors

- [@NadimSalameh](https://github.com/NadimSalameh)

## Technologies and Tools

* python 3.9.7
* Jupyter Notebook
* Flask
* Docker
* REST API
* MongoDB
* JSON
* seaborn
* Matplotlib
* Sklearn

## Documentation

My  flaskapp folder contains eight files:
* Templates: contains design.html and history.html (used for the design of the app)
* App.py: contains the code for the application
* docker-compose file
* Docker file
* Model: jupyter notebook for analysis, visualization and model training
* RandomForest.pkl: contains the model used for the app
* Requirements: requirements needed for the app
* SkyData_pro: contains the dataset


## How to run the application

* Download the files
* In your Command line (cmd,GitBash..) type *python app.py* 
* *docker-compose build* build your images(mongoDB and flaskapp)
* *docker-compose run* run the images in the DOCKER containers
* After building the image and running docker containers, you can see the app running on you localhost:5000 in your browser.

* On the main page you see a form that you have to fill in to make a prediction. After filling it in, click on predict to see your result.

* If you want to see the prediction history, click on history that will show you a database table saving your input, timestamp and the result of the prediction (bottom left of the page).

## mongoDB in Docker

* *docker ps*: show running container
* *docker exec –it mongo-image-ID /bin/bash* 

* *Show dbs*: show databases
* *use flaskappDB*
* *Show collections*: show collections
* *db.data.find()*: show vlaues inside the collection (data)


## Future Work

I will try to work more the design of the application