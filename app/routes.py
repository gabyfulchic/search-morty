
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


def get_all_episodes():
    return ramapi.Episode.get_all().get("results", "")


@app.route("/")
def home():
    return render_template('index.jinja')

@app.route("/", methods=['POST'])
def index():
    all_episodes_list = []
    character_to_search = request.form['character']

    if (character_to_search == ""):
        return "Merci de saisir un personnage."
    else:
        for c in get_all_characters():
            if (character_to_search == c.get("name", "")):
                for e in get_all_episodes():
                    all_episodes_list.append(e.get("name", ""))
                return render_template('all_episode.jinja', character = character_to_search, all_episodes = all_episodes_list)

    return "Désolé, nous n'avons pas trouvé votre personnage."