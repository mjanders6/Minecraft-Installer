import inquirer
from inquirer.themes import GreenPassion
import subprocess


# q = [
#     inquirer.Text("name", message="Whats your name?", default="No one"),
#     inquirer.List("jon", message="Does Jon Snow know?", choices=["yes", "no"], default="no"),
#     inquirer.Checkbox(
#         "kill_list", message="Who you want to kill?", choices=["Cersei", "Littlefinger", "The Mountain"]
#     ),
# ]

# inquirer.prompt(q, theme=GreenPassion())


text = inquirer.text(message="Enter your username")
print(text)

password = inquirer.password(message='Please enter your password')


choice = inquirer.list_input("Public or private?",
                              choices=['public', 'private'])
correct = inquirer.confirm("This will delete all your current labels and "
                        "create a new ones. Continue?", default=False)
						
						