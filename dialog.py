from lib2to3.pgen2 import grammar
import os
import sys
from pprint import pprint
from wsgiref import validate

import inquirer.events

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

from inquirer.themes import GreenPassion

questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
    inquirer.Text(
        "name", 
        message="What's your name?",
        
        ),
    inquirer.Text("surname", message="What's your surname, {name}?"),
    inquirer.Confirm("continue", message="Should I continue"),
    inquirer.Confirm("stop", message="Should I stop", default=True),
    inquirer.Checkbox(
        "interests",
        message="What are you interested in?",
        choices=["Computers", "Books", "Science", "Nature", "Fantasy", "History"],
        default=["Computers", "Books"],
    ),
]

questions2 = [
        inquirer.List(
        "width",
        message="What width do you need?",
        choices=["tiny", "teany tiny"],
        default = ["tiny"]
    ),
    inquirer.Text(
        "time", 
        message="What time are we meeting?",
        
        ),
]

answers = inquirer.prompt(questions, theme=GreenPassion())
answers2 = inquirer.prompt(questions2, theme=GreenPassion())


pprint(answers)
pprint(answers2)
