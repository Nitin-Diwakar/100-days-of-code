import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def english_word(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "delhi" this will check for "Delhi" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        check = input(f"Did you mean {get_close_matches(w,data.keys())[0]} instead ? (Y)es or (N)o:" )
        check = check.upper()
        if check == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif check == 'N':
            return f"Word doesn't exist.Please double check it."
        else:
            return f"We didn't understand your entry."
    else:
        return f"Word doesn't exist.Please double check it."


word = input('Enter your word: ')
result = english_word(word)

if type(result) == list:
    for meaning in result:
        print(meaning)
else:
    print(result)
