# challenge_flask_api
to create an API in python with the Flask module

### Objectives

* Create a flask app - DONE
* Add a route that show hello world - DONE
* Add a route with GET method - DONE
* Add a route with POST method - DONE
* Get data from a GET request, transorm it and return it - DONE
* Get data from a POST request, transorm it and return it - DONE
* Deploy your API on Heroku - DONE


### Steps

1. Create a virtual environment called flask_api 
2. pip install flask / numpy etc
3. pip freeze --local > requirement.txt to create list of libraries installed on flask_api environment
4. Create a flask app -- named hello.py
5. Add a route that show hello world
6. Create a flask app -- named main.py
7. Add a route /home that show Home Page
8. Add a route /status to get status Alive!
9. Add boostrap by creating a layout template
10. Create home page & status template
11. Add navigation bar on layout template
12. Add css file in static folder
14. pip install flask-wtf on terminal to create form
15. create forms.py and import FlaskForm
16. create class Loginform
17. create secret key by using pyton secrets library to create a token_hex key
18. import LoginFrom to main.py  
19. Add a route /login to login
20. create login.html
21. update route /login to include flash message and redirct after login to home
22. update layout.html to get flash message (line43-51)
23. install flask-sqlalchemy on flask_api env
24. import SQLAlchemy on main.py
25. create app.config['SQLALCHEMY_DATA_URI'] = 'sqlite:///site.db'
26. create database instance db = SQLAlchemy(app)
27. create class Image for image file
28. turn application to package
29. moved files to main folder and created __init__.py 
30. create run.py to run the app
31. install heruko
32. create Profile with web: gunicorn main:app
33. pip install gunicorn and update requirements.txt
34. Follow the command below to deploy heruko

	* heroku create
	* git push heroku HEAD:master
	* heroku ps:scale web=1
	* heroku open

35. Deployment successful. (old name https://arcane-reef-89340.herokuapp.com/)
36. Add github link on Home Page.
37. Renamed link https://git.heroku.com/kaiyung-flask-api.git

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






