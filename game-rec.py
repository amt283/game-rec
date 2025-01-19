# TO-DO:
    # Ask for input on type of game looking for (liked, never played, unfinished, missing achievements, etc.)
    # Have ability to go back to previous steps and change settings (maybe?)
    # Have ability to restart program at any time (if incorrect choice picked?)
    # NEEDS REFACTORING!!!
        # Move dicts into separate files
        # Separate blocks of code in main() into separate functions (aka: clean it up)
        # Comments explaining what each block does

import random
import sys

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

    len_prompt = '''Game length (select number):
    [1] < 10 hours
    [2] 10-19 hours
    [3] 20-29 hours
    [4] 30-39 hours
    [5] 40+ Hours
    \n'''
    
    new_dict = {}

    while True:
        try:
            len_picked = int(input(len_prompt))
            #print(f"\nYou picked: {len_picked}\n")
            if len_picked == 1:
                for key, val in games.items():
                    if val < 10:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 2:
                for key, val in games.items():
                    if val >= 10 and val < 19:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 3:
                for key, val in games.items():
                    if val >= 20 and val < 29:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 4:
                for key, val in games.items():
                    if val >= 30 and val < 39:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 5:
                for key, val in games.items():
                    if val >= 40:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            else:
                print("\nNot a valid selection, please try again.\n")
                continue
        except ValueError:
            continue
    
    list_of_pairs = list(new_dict.items())
    question_order = list_of_pairs[:] # make a copy of the input list
    random.shuffle (question_order)
    print("\nTitle:", "\nLength: ".join(map(str,random.choice(question_order))), "hours\n")

    while True:
        rec_again = input("\nDo you want another recommendation? [Y/N]: ").lower()
        if rec_again == "y":
            try:
                random.shuffle (question_order)
                print("\nTitle:", "\nLength: ".join(map(str,random.choice(question_order))), "hours\n")
                question_order.pop()
                print(question_order)
            except IndexError:
                print("\nNo new games to recommend. If you'd like to loop through previously suggested games, enter Y below.\n ")
                question_order = list_of_pairs[:] # make a copy of the input list
                continue
        elif rec_again == "n":
            print("\nGoodbye!\n")
            sys.exit(0)
        else:
            print("\nInvalid entry, try again.")
            continue

main()