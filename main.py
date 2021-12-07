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
        'popularity': response_body["popularity"],
    }

def run():
    my_character = random_manga()
    print('You were given {}'.format(my_character['title']))
    choice = input('Which stat do you want to use? id, rank, popularity')
    opponent_character = random_manga()
    print('The opponent chose {}'.format(opponent_character['title']))
    my_stat = my_character[choice]
    opponent_stat = opponent_character[choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')
run()
