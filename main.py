import random
import requests
import csv

def random_manga():
    number = random.randint(1, 151) #generates random number from 1-150
    url = 'https://api.jikan.moe/v3/manga/{}'.format(number)
    request = requests.get(url)
    response_body = request.json()
    return {
        'title': response_body["title"],
        'id': response_body["mal_id"],
        'rank': response_body["rank"],
        'popularity': response_body["popularity"]}

def run():
    # Ask players their names
    name1 = input('Player 1, what is your name?')
    name2 = input('Player 2, what is your name?')
    #Randomly assign two characters for player 1
    player1_character = random_manga()
    player1_character2 = random_manga()
    print('{}, you were given {} and {}'.format(name1, player1_character['title'], player1_character2['title']))
    char_choice = input('Which character do you want to choose?')
    if char_choice == player1_character['title']:
        choice = input('Which stat do you want to use? (id, rank, popularity) ')
        player1_stat = player1_character[choice]
    elif char_choice == player1_character2['title']:
        choice = input('Which stat do you want to use? (id, rank, popularity) ')
        player1_stat = player1_character2[choice]
    player2_character = random_manga()
    print('{}, you were given {}'.format(name2, player2_character['title']))
    player2_choice = input('{}, which stat do you want to use? (id, rank, popularity) '.format(name2))
    player2_stat = player2_character[player2_choice]
    #Compares the stats chosen by each player
    if player1_stat > player2_stat:
        print('Player 1 Wins!')
    elif player1_stat < player2_stat:
        print('Player 2 Wins!')
    else:
        print('Draw!')
    score1 = 0
    score2 = 0
    if player1_stat > player2_stat:
        score1=score1+1
    elif player1_stat < player2_stat:
        score2=score2+1
    else:
        score1=score1+0
    field_names=['name','score']
    data = [{'name':name1,'score':score1},{'name':name2, 'score':score2}]
    with open ('scores.csv','w+') as csv_file:
        spreadsheet =csv.DictWriter(csv_file, fieldnames=field_names)
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    return


run()


