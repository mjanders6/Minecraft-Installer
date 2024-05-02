import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

questions = [
    inquirer.List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
    inquirer.Text("name", message="What's your name?"),
    inquirer.Text("surname", message="What's your surname, {name}?"),
    inquirer.Confirm("continue", message="Should I continue"),
    inquirer.Confirm("stop", message="Should I stop", default=True),
    
]

answers = inquirer.prompt(questions)

pprint(answers)