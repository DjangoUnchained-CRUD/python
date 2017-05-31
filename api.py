import requests
import math
import random

print('#################################')
print('######### MOVIE TRIVIA ##########')
print('#################################')
print('\n')

class MyGame:
    score = 0

# end of MyGame

def get_popular_actors(strict):
    if strict:
        random_page = int(math.ceil((MyGame.score + 1) / 3.0))
    else:
        random_page = random.randint(1, 10)

    api_key = '11938d3660b328fb2c7a3a87e50fa540'
    url = 'https://api.themoviedb.org/3/person/popular?language=en-US&page='+str(random_page)+'&api_key='+api_key

    response = requests.get(url)
    return response.json()

# end get_popular_actors

def get_random_actor(popular):
    return popular['results'][random.randint(0, (len(popular['results']) - 1))]['name']

# end get_random_actor

def get_answer_actors(correct_actor):
    actors = []

    actors.append(correct_actor)

    popular = get_popular_actors(False)

    actors.append(get_random_actor(popular))
    actors.append(get_random_actor(popular))

    random.shuffle(actors)

    return actors

# end get_answer_actors

def game_logic():
    popular = get_popular_actors(True)

    random_result = random.randint(0, (len(popular['results']) - 1))

    known_for = popular['results'][random_result]['known_for']

    correct_actor = popular['results'][random_result]['name']

    actors = get_answer_actors(correct_actor)

    for movie in known_for:
        try:
            print(movie['title'])
        except KeyError:
            continue

    print('\n')
    print("Who acted in all these movies?")
    print('\n')

    count = 1

    for actor in actors:
        str_actor = str(count) + ') ' + actor
        print(str_actor)
        count += 1

    selected = int(input("Please select 1, 2, or 3"))

    while selected > 3 or selected < 1:
        selected = int(input('I said please select 1, 2, or 3!  '))

    # add error handling for non-ints

    if actors[(selected - 1)] == correct_actor:
        print('Woot woot!  You know your movies! The correct answer is ' + correct_actor)
        return True
    else:
        print('Suck it nerd! The correct answer was: ' + correct_actor)
        return False

# end game_logic()

def main():
    count = 0
    while game_logic() == True:
        MyGame.score += 1
        score_message = 'Your score: ' + str(MyGame.score) + '\n'
        print(score_message)
        print('Onto the next one \n')

# end main()

main()
