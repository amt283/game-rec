# TO-DO:
    # Ask for input on type of game looking for (liked, never played, unfinished, missing achievements, etc.)
    # Have ability to go back to previous steps and change settings (maybe?)
    # Have ability to restart program at any time (if incorrect choice picked?)
    # "Surprise me" feature - picks randomly
    # NEEDS REFACTORING!!!
        # Move dicts into separate files
        # Separate blocks of code in main() into separate functions (aka: clean it up)
        # Comments explaining what each block does

import random
import sys
import game-data

def main():
    
    print(game-data.games)

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
            print("\nInvalid entry, try again.\n")
            continue
    
    list_of_pairs = list(new_dict.items())
    suggestions = list_of_pairs[:] # make a copy of the input list
    random.shuffle (suggestions)
    print("\nTitle:", "\nLength: ".join(map(str,random.choice(suggestions))), "hours\n")

    while True:
        rec_again = input("\nDo you want another recommendation? [Y/N]: ").lower()
        if rec_again == "y":
            try:
                random.shuffle (suggestions)
                print("\nTitle:", "\nLength: ".join(map(str,random.choice(suggestions))), "hours\n")
                suggestions.pop()
                print(suggestions)
            except IndexError:
                print("\nNo new games to recommend. Program will now loop through previously suggested games.\n ")
                suggestions = list_of_pairs[:] # Copy input list again to repopulate suggestions
                continue
        elif rec_again == "n":
            print("\nGoodbye!\n")
            sys.exit(0)
        else:
            print("\nInvalid entry, try again.")
            continue

main()