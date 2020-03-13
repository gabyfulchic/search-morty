from routes import get_all_characters
from ramapi import *

# No message because PyTest return only boolean.

def should_return_all_character():
    assert get_all_characters() == ramapi.Character.get_all().get("results", "")

def should_return_all_episode():
    assert get_all_episodes() = ramapi.Episode.get_all().get("results", "")

def should_return_true_if_character_is_in_this_episodes(character):
    assert get_all_episodes_where_character_is(character) = ramapi.Episode.get(character).get("results", "")

def should_return_true_if_name_match():
    assert getPerson(name) == "Annie")