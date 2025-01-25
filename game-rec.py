# TO-DO:
    # Have ability to go back to previous steps and change settings (maybe?)
    # Have ability to restart program at any time (maybe?)
    # Comment explaining what each block does
    # Have option to exit program at any time
    # filter any disliked/ignored games

import random
import sys
import gameData

def main():
    
    len_choice_dict = game_len_filter()

    filtered_dict = addl_filters(len_choice_dict)
    
    # If final, filtered dict isn't empty, make suggestion. Otherwise prompts for another category to be chosen
    # Assumes csv files has other games to choose from
    while True:
        if bool(filtered_dict) == True:
            list_of_pairs = list(filtered_dict.items())
            suggestions = list_of_pairs[:] # make a copy of the input list
            random.shuffle(suggestions)
            choice = random.choice(suggestions)
            print("\nTitle:", "\nLength: ".join(map(str,choice)), "hours\n")
            suggestions.remove(choice)

            reprompt(list_of_pairs, suggestions)
        else:
            print("\nNo Valid entries. Pick another category.\n")
            filtered_dict = addl_filters(len_choice_dict)

def game_len_filter():
    games = gameData.game_len

    len_prompt = '''Game length preferred? Choose one:
    [1] < 10 hours
    [2] 10-19 hours
    [3] 20-29 hours
    [4] 30-39 hours
    [5] 40+ Hours
    [6] Surprise me (Random pick)
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
            elif len_picked == 6:
                for key, val in games.items():
                    new_dict.setdefault(key, val)
                break
            else:
                print("\nNot a valid selection, please try again.\n")
                continue
        except ValueError:
            print("\nInvalid entry, please choose a number.\n")
            continue
        except IndexError:
            print("No games to recommend, please pick another category.")
            continue
    return new_dict

def addl_filters(len_choice_dict):
        
    prompt = '''Game status?:
    [1] Never played
    [2] Unfinished
    [3] Missing Achievements
    [4] Surprise me (Random pick)
    \n'''

    user_input = int(input(prompt))

    while True:
        try:
            if user_input == 1:
                played_dict = gameData.game_played
                new_dict = {k: v for k, v in played_dict.items() if v == 'False'} # creates new dict with key/val pairs where val meets condition in 2nd dict (played_dict)
                break
            elif user_input == 2:
                played_dict = gameData.game_done
                new_dict = {k: v for k, v in played_dict.items() if v == 'True'}
                break
            elif user_input == 3:
                played_dict = gameData.game_ach
                new_dict = {k: v for k, v in played_dict.items() if v == 'False'}
                break
            elif user_input == 4:
                new_dict = len_choice_dict
                break
            else:
                print("Invalid input, try again.")
                continue
        except ValueError:
            print("Invalid input, enter a number")
            continue
    

    matched = {key: len_choice_dict[key] for key in len_choice_dict if key in new_dict} #  compare keys in two dictionaries and save the matching key-value pairs using a loop
    # This will create a new dictionary matched containing only the key-value pairs from len_choice_dict where the keys also exist in new_dict 
    # https://duckduckgo.com/?q=python+compare+keys+in+two+dicts+then+save+key%2Fvalue+when+keys+match&t=ftsa&ia=web&assist=true

    #print("These items are all match: ", matched)

    return matched

def reprompt(list_of_pairs, suggestions):
    while True:
        rec_again = input("\nDo you want another recommendation? [Y/N]: ").lower()
        if rec_again == "y":
            try:
                random.shuffle(suggestions)
                choice = random.choice(suggestions)
                print("\nTitle:", "\nLength: ".join(map(str,choice)), "hours\n")
                suggestions.remove(choice)
                #print(suggestions)
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

    games = gameData.game_done

    len_prompt = '''Game status preferred? Choose one:
    [1] Unfinished
    [2] Finished
    [3] Surprise me (Randomly picks)
    \n'''
    
    new_dict = {}

    while True:
        try:
            len_picked = int(input(len_prompt))
            #print(f"\nYou picked: {len_picked}\n")
            if len_picked == 1:
                for key, val in set(games.items()) & set(game_done_dict.items()):
                    if key == game_done_dict[key] and val == False:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 2:
                for key, val in set(games.items()) & set(game_done_dict.items()):
                    if key == game_done_dict[key] and val == True:
                        new_dict.setdefault(key, val)
                    else:
                        continue
                break
            elif len_picked == 3:
                for key, val in set(games.items()) & set(game_done_dict.items()):
                    if key == game_done_dict[key]:
                        new_dict.setdefault(key, val)
                break
            else:
                print("\nNot a valid selection, please try again.\n")
                continue
        except ValueError:
            print("\nInvalid entry, please choose a number.\n")
            continue
    print(new_dict)
    return new_dict

main()