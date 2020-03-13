import os
import wtforms as wt
import json

from wtforms import TextField, Form
from ramapi import *
from flask import Flask, Response, render_template, request

app = Flask(__name__)
NAMES = ["abc","abcd","abcde","abcdef"]

class SearchForm(Form):
    autocomp = TextField('autocomp', id = 'autocomplete')

def create_first_page():
    app = Flask(__name__)
    Bootstrap(app)
    return app


def get_all_characters():
    return ramapi.Character.get_all().get("results", "")


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('term')

    app.logger.debug(search)
    return Response(json.dumps(NAMES), mimetype='application/json')


@app.route("/", methods=['GET', 'POST'])
def index():
    find = 0
    form = SearchForm(request.form)

    if (request.method == "POST" and form.validate()):
        all_characters = get_all_characters()
        for c in all_characters:
            if (form == c.get("name", "")):
                find = 1
                break
        if (find == 1):
            return "Nous avons trouvé votre personnage : " + character_to_search
        else:
            return "Désolé, nous n'avons pas trouvé votre personnage."
    else:
        return render_template("index.html", form = SearchForm(request.form))

    return render_template("index.html", form = character_to_search)

if __name__ == '__main__':
    app.run(debug=True)