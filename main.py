import random
import requests

def random_manga():
    number = random.randint(1, 151)
    url = 'https://api.jikan.moe/v3/manga/{}'.format(number)
    request = requests.get(url)
    response_body = request.json()
    return {
        'title': response_body["title"], 
        'id': response_body["mal_id"],
        'rank': response_body["rank"],
        'popularity': response_body["popularity"]}

def run():
    my_character = random_manga()
    my_character2 = random_manga()
    print('You were given {} and {}'.format(my_character['title'], my_character2['title']))
    char_choice = input('Which character do you want to choose?')
    if char_choice == my_character['title']:
        choice = input('Which stat do you want to use? id, rank, popularity')
        my_stat = my_character[choice]
    elif char_choice == my_character2['title']:
        choice = input('Which stat do you want to use? id, rank, popularity')
        my_stat = my_character2[choice]
    opponent_character = random_manga()
    print('The opponent chose {}'.format(opponent_character['title']))
    opponent_stat = opponent_character[choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
        
run()
