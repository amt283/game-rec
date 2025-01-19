# Asks for input on type of game looking for (liked, never played, unfinished, missing achievements)
# Asks for game length (??)
# Searches dict of games (two dicts? One for type, second for length?)
# (maybe asks how many games to suggest?)
# Outputs suggestion 
# Have the ability to refresh list based on previous choices
# Have ability to go back to previous steps and change settings
# Have ability to go back to main menu and start over at any time

def main():
    games = {
        "A Vicious Circle": 26.5,
        "Actually": 8.5,
        "Age of the Dragon 2": 30.5,
        "Alan Walker": 7,
        "Alan Walker 2": 164,
        "American Delusion by Alan Walker": 1.5,
        "Bring a Plate": 143,
        "Central Pacific": 52.5,
        "Coral Boat": 48,
        "Deep Sea Galaxy Game": 37.5,
        "Deep Sea Voyages": 53.5,
        "Double Royal Palace": 5,
        "Electric Washing Machine": 10.5,
        "Emergency Hi-Fi": 5,
        "Empty Door 3": 6,
        "Evil Is Inside": 12,
        "Evil Is Inside 2": 2,
        "Experience Dragons": 12.5,
        "Final Administrative Body": 95,
        "Final Estimate of X": 56.5,
        "Folding and Inking Machine": 38,
        "From The Subway": 60.5,
        "From The Subway Extended Edition": 61,
        "Golden Man 4": 41,
        "Haunted Corridor": 3,
        "Hell 2": 104,
        "His Name is Porto": 33,
        "History of Cords": 33.5,
        "In Principle": 29,
        "In The Desert": 9,
        "Killer Company": 94,
        "My Environment Is Friendly": 39.5,
        "Path of the Gods": 27.5,
        "Photo By Stanley": 45,
        "Pizza Box": 141,
        "Rain Disease 2": 5,
        "Results of the Andromeda Conference": 27.5,
        "Second and a Dark Forest: A Critical Edition": 142,
        "Second, The Dark Forest": 66.5,
        "Sub-Zero War: Sub-Zero": 4,
        "Supermarket Style": 9,
        "The Last Dream VII": 103,
        "The Lost Dream IX": 2.5,
        "The Result: New Vegas": 201,
        "Train 2033 Redux": 9,
        "Valley Of The Stars": 129,
        "Will This Game Kill Me?": 6,
    }

    print(games)

main()