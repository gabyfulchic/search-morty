import routes

from ramapi import *

def should_return_all_character():
    assert routes.get_all_characters() == ramapi.Character.get_all().get("results", "")