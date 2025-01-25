# row takes column??
# [key] takes value???

import csv

game_len = {}

with open("games.csv", mode="r") as file_input:
    reader = csv.reader(file_input)
    game_len = {rows[0]: float(rows[1]) for rows in reader}

game_played = {}

with open("games.csv", mode="r") as file_input:
    reader = csv.reader(file_input)
    game_played = {rows[0]: rows[2] for rows in reader}

game_done = {}

with open("games.csv", mode="r") as file_input:
    reader = csv.reader(file_input)
    game_done = {rows[0]: rows[3] for rows in reader}

game_ach = {}

with open("games.csv", mode="r") as file_input:
    reader = csv.reader(file_input)
    game_ach = {rows[0]: rows[4] for rows in reader}

game_dislike = {}

with open("games.csv", mode="r") as file_input:
    reader = csv.reader(file_input)
    game_dislike = {rows[0]: rows[5] for rows in reader}

# print(game_len)

#print(f"Played \n: {game_played}")

# print(game_dislike)

# def create_game_len():
#     ...

# def create_game_played():
#     ...

# def create_game_done():
#     ...

# def create_game_ach():
#     ...

# def create_game_dislike():
#    ...