# challenge_flask_api
to create an API in python with the Flask module

### Objectives

* Create a flask app  
* Add a route that show hello world  
* Add a route with GET method  
* Add a route with POST method  
* Get data from a GET request, transorm it and return it 
* Get data from a POST request, transorm it and return it  
* Deploy your API on Heroku  - https://kaiyung-flask-api.herokuapp.com/


### Steps

- [X] Create a virtual environment called flask_api 
- [X] pip install flask / numpy etc
- [X] pip freeze --local > requirement.txt to create list of libraries installed on flask_api environment
- [X] Create a flask app -- named hello.py
- [X] Add a route that show hello world
- [X] Create a flask app -- named main.py
- [X] Add a route /home that show Home Page
- [X] Add a route /status to get status Alive!
- [X] Add boostrap by creating a layout template
- [X] Create home page & status template
- [X] Add navigation bar on layout template
- [X] Add css file in static folder
- [X] pip install flask-wtf on terminal to create form
- [X] create forms.py and import FlaskForm
- [X] create class Loginform
- [X] create secret key by using pyton secrets library to create a token_hex key
- [X] import LoginFrom to main.py  
- [X] Add a route /login to login
- [X] create login.html
- [X] update route /login to include flash message and redirct after login to home
- [X] update layout.html to get flash message (line43-51)
- [X] install flask-sqlalchemy on flask_api env
- [X] import SQLAlchemy on main.py
- [X] create app.config['SQLALCHEMY_DATA_URI'] = 'sqlite:///site.db'
- [X] create database instance db = SQLAlchemy(app)
- [X] create class Image for image file
- [X] turn application to package
- [X] moved files to main folder and created __init__.py 
- [X] create run.py to run the app
- [X] install heruko
- [X] create Procfile -- web: gunicorn main:app
- [X] pip install gunicorn and update requirements.txt
- [X] To deploy heruko:

	* heroku create
	* git push heroku HEAD:master
	* heroku ps:scale web=1
	* heroku open

- [X] Deployment successful.  
- [X] Add github link on Home Page.
- [X] Renamed heroku link - https://kaiyung-flask-api.herokuapp.com/


### The Mission

You are intern in a company to provide AI models to their customer. Unfortunatly the machine learning engineers that work with you are not very goods... They spend more time drinking coffee and play video games than doing their job. After few weeks their the project manager come to you and tell you that they have a client that is really upset to not have his model yet. He ask you to already create the API to get the data and return a random prediction. It will give him more time to beg the ML to finish the project.
You decide to use Flask as it's the best tool to boostrap and API in python. You receive a mail from the client:
Dear lazy company,
WE NEED OUR MODEL TO BE READY BY TOMOROW OR YOU WILL BE IN TROUBLE!!!
OUR LAWYERS ARE READDY TO SUE YOU!

We will test your API in 48h.
You will find in attamchment the routes that should be working (AND I HOPE FOR YOU IT WILL):

Warms regards,
You lovely client,
MadCompany
Attachments:

### Route to check if the server runs
GET /status -> "Alive!"

###  Route that to login
POST /login -> "Login success for user {USER_NAME_HERE} with password from length: {PASSWORD_LENGTH_HERE}!"
body: {
    username: <USER_NAME_HERE>
    password: <PASSWORD_HERE>
}

### Route that return the prediction
GET /predict/<seller_avaible:int>/<month:str>/<customer_visiting_website:int> -> Prediction (int between 2000 and 5000)

### Must-have features
* A GET route at /status that return the string "alive"
* A POST route at /login that return a string containing "Login success for user USER_NAME_HERE with password from length: PASSWORD_LENGTH_HERE!".
* a GET route at /predict that take 3 arguments (month, customer_visiting_website, seller_avaible) and return an int between 2000 and 5000.

### Nice-to-have features
* Folow pep8 rules.
* Add a docstring for each route.
* Type all you functions.
* Use Black to format your code. - Done
* Add a route that take an image and save it on the server. Return the image's server path. - Under construction
* Add unittest for at least one route.






