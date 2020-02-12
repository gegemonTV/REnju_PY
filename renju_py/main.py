import random
import site
site.addsitedir('/home/linuxxx0id/renju_py/lib')
from players import *
from helpful import *

game = []
score = {}

q = 0.1

RAND_CHANCE = 5

x_player = input('Input who would play with "x"[1-for Player, 2-for AI, 3-for Stupid PC]: ')
if x_player == '1':
    score['Player'] = 0
elif x_player == '2':
    score['AI'] = 0
elif x_player == '3':
    score['Stupid PC'] = 0

o_player = input('Input who would play with "o"[1-for Player, 2-for AI, 3-for Stupid PC]: ')
if o_player == '1':
    score['oPlayer'] = 0
elif o_player == '2':
    score['oAI'] = 0
elif o_player == '3':
    score['oStupid PC'] = 0

w_steps = {}

def field_generator(x,y):
    field = {}
    for i in range(x*y):
        field[i+1] = f'{i+1}'
    return field

"""
k = 0
tryscore = {'Stupid PC': 0, 'oAI':0}
try_score = {'AI': 0, 'oStupid PC': 0}
while k<10000:
    game = []
    field = field_generator(13,13)
    game_ai = []
    print('Start')
    print()
    view_field(field)
    k+=1
    print('\n\n')
    if k<=5000:
        ai_step(game, field, w_steps,RAND_CHANCE, 'x')
        if check_win(segmentation(field),'x') == 1:
            score_editing(try_score, 'AI', 'oStupid PC', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] += q

        if check_win(segmentation(field),'o') == 1:
            score_editing(try_score, 'AI', 'oStupid PC', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] -= q
        print(try_score)
        break
        
        view_field(field)

        pc_step(game, field, 'o')
        if check_win(segmentation(field),'x') == 1:
            score_editing(try_score, 'AI', 'oStupid PC', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] += q

        if check_win(segmentation(field),'o') == 1:
            score_editing(try_score, 'AI', 'oStupid PC', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] -= q
        print(try_score)
        break
        view_field(field)
    if k>5000:
        pc_step(game, field, 'x')
        
        if check_win(segmentation(field),'x') == 1:
            score_editing(tryscore, 'Stupid PC', 'oAI', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] -= q

        if check_win(segmentation(field),'o') == 1:
            score_editing(tryscore, 'Stupid PC', 'oAI', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] += q
        print(tryscore)
        break

        view_field(field)
        
        ai_step(game, field, w_steps,RAND_CHANCE, 'o')

        if check_win(segmentation(field),'x') == 1:
            score_editing(tryscore, 'Stupid PC', 'oAI', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] -= q

        if check_win(segmentation(field),'o') == 1:
            score_editing(tryscore, 'Stupid PC', 'oAI', field)
            for i in range(0, len(game_ai)):
                print(game_ai)
                w_steps[game_ai[i]] += q
        print(tryscore)
        break

        view_field(field)
"""
while True:
    game = []
    i=1
    field = field_generator(13,13)

    game_ai = []

    print('Start')
    print()
    view_field(field)

    while i < 170:
        i+=1
        print('\n\n')
        if x_player == '1':
            human_step(game, field, 'x')
        elif x_player == '2':
            ai_step(game, field, w_steps, RAND_CHANCE, 'x')
        elif x_player =='3':
            pc_step(game, field, 'x')
        print(game)
        if i > 1:
            game_ai.append(restring(game))
        print(game_ai)
        if check_win(segmentation(field),'x') == 1:
            if x_player == '1' and o_player == '1':
                score_editing(score, 'Player', 'oPlayer', field)
            elif x_player == '1' and o_player == '2':
                score_editing(score, 'Player', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '1' and o_player == '3':
                score_editing(score, 'Player', 'oStupid PC', field)
            elif x_player == '2' and o_player == '1':
                score_editing(score, 'AI', 'oPlayer', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '2':
                score_editing(score, 'AI', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '3':
                score_editing(score, 'AI', 'oStupid PC', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '3' and o_player == '1':
                score_editing(score, 'Stupid PC', 'oPlayer', field)
            elif x_player == '3' and o_player == '2':
                score_editing(score, 'Stupid PC', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '3' and o_player == '3':
                score_editing(score, 'Stupid PC', 'oStupid PC', field)
            print(score)
            y = input('enter Enter: ')
            break

        if check_win(segmentation(field),'o') == 1:
            if x_player == '1' and o_player == '1':
                score_editing(score, 'Player', 'oPlayer', field)
            elif x_player == '1' and o_player == '2':
                score_editing(score, 'Player', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '1' and o_player == '3':
                score_editing(score, 'Player', 'oStupid PC', field)
            elif x_player == '2' and o_player == '1':
                score_editing(score, 'AI', 'oPlayer', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '2' and o_player == '2':
                score_editing(score, 'AI', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '3':
                score_editing(score, 'AI', 'oStupid PC', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '3' and o_player == '1':
                score_editing(score, 'Stupid PC', 'oPlayer', field)
            elif x_player == '3' and o_player == '2':
                score_editing(score, 'Stupid PC', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '3' and o_player == '3':
                score_editing(score, 'Stupid PC', 'oStupid PC', field)
            print(score)
            y = input('enter Enter: ')
            break

        if o_player == '1':
            human_step(game, field, 'o')
        elif o_player == '2':
            ai_step(game, field, w_steps, RAND_CHANCE, 'o')
        elif o_player =='3':
            pc_step(game, field, 'o')
        i+=1
        view_field(field)

        if check_win(segmentation(field),'x') == 1:
            if x_player == '1' and o_player == '1':
                score_editing(score, 'Player', 'oPlayer', field)
            elif x_player == '1' and o_player == '2':
                score_editing(score, 'Player', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '1' and o_player == '3':
                score_editing(score, 'Player', 'oStupid PC', field)
            elif x_player == '2' and o_player == '1':
                score_editing(score, 'AI', 'oPlayer', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '2':
                score_editing(score, 'AI', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '3':
                score_editing(score, 'AI', 'oStupid PC', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '3' and o_player == '1':
                score_editing(score, 'Stupid PC', 'oPlayer', field)
            elif x_player == '3' and o_player == '2':
                score_editing(score, 'Stupid PC', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '3' and o_player == '3':
                score_editing(score, 'Stupid PC', 'oStupid PC', field)
            print(score)
            y = input('enter Enter: ')
            break


        if check_win(segmentation(field),'o') == 1:
            if x_player == '1' and o_player == '1':
                score_editing(score, 'Player', 'oPlayer', field)
            elif x_player == '1' and o_player == '2':
                score_editing(score, 'Player', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '1' and o_player == '3':
                score_editing(score, 'Player', 'oStupid PC', field)
            elif x_player == '2' and o_player == '1':
                score_editing(score, 'AI', 'oPlayer', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '2' and o_player == '2':
                score_editing(score, 'AI', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '2' and o_player == '3':
                score_editing(score, 'AI', 'oStupid PC', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] -= q
            elif x_player == '3' and o_player == '1':
               score_editing(score, 'Stupid PC', 'oPlayer', field)
            elif x_player == '3' and o_player == '2':
                score_editing(score, 'Stupid PC', 'oAI', field)
                for i in range(0, len(game_ai)):
                    print(game_ai)
                    w_steps[game_ai[i]] += q
            elif x_player == '3' and o_player == '3':
                score_editing(score, 'Stupid PC', 'oStupid PC', field)
            print(score)
            y = input('enter Enter: ')
            break


        view_field(field)
    if i>=170:
        if check_win(segmentation(field),'o') == 0 and check_win(segmentation(field),'x') == 0:
            for i in range(0,len(game_ai)):
                w_steps[game_ai[i]] -=q
            print(w_steps)
            view_field(field)
            print('nothing happens')
            y = input('enter Enter: ')
    print(w_steps)
