import requests
import flask
from flask import Flask, request, jsonify
#declare the app
app = flask.Flask(__name__)
#declaring our routes
#any time you hit the url , it will access some code 
@app.route('/api/brew', methods=["GET", "POST"])
def apiPost():
    brewery_type = {}
    response = request.get_json()
    state = response["state"]
    url = "https://api.openbrewerydb.org/breweries?format=json&by_state=" + state
    response = requests.get(url)
    brew = response.json()
    for i in range(len(brew)):
        if brew[i]["name"] in brewery_type:
            brewery_type[brew[i]["name"]] += 1
        else:
            brewery_type.update({brew[i]["name"]: 1})
    # return "Types of breweries in " + state + ":\n" + str(brewery_type)
    return "Names of breweries in " + state + ":\n" + str(brewery_type)


    # return str(brew)
app.run()