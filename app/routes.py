import os

from ramapi import *
from flask import Flask, request, render_template

app = Flask(__name__)

def create_first_page():
    app = Flask(__name__)
    Bootstrap(app)

    return app

def get_all_characters():
    return ramapi.Character.get_all().get("results", "")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def my_form_post():
    find = 0
    character_to_search = request.form['character']

    if (character_to_search == ""):
        return "Merci de saisir un personnage."
    else:
        all_characters = get_all_characters()
        for c in all_characters:
            if (character_to_search == c.get("name", "")):
                find = 1
                break
        if (find == 1):
            return "Nous avons trouvé votre personnage : " + character_to_search
        
    return "Désolé, nous n'avons pas trouvé votre personnage."