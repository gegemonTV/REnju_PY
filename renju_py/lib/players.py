import random
import site
site.addsitedir('/home/linuxxx0id/renju_py/lib')
from helpful import *

def ai_step(steps_of_game, field_for_now, weight_of_steps, rand_chance, let):
    b_steps = {}
    ch = ''
    max_step = '' 
    st = some_steps(field_for_now=field_for_now, let=let)
    g = restring(steps_of_game)
    for i in range(len(st)):
        ch = f'{g}{st[i]}'
        if weight_of_steps.get(ch) == None:
            weight_of_steps[ch] = 1
            
        b_steps[ch] = weight_of_steps[ch]
    if b_steps:
        max_step = max(b_steps, key=b_steps.get)
    if random.randint(1,100)> rand_chance:
        try:
            step = int(key_getter(max_step))
        except ValueError:
            mass = []
            for i in range(1,170):
                if field_for_now[i] == 'x' or field_for_now[i] == 'o':
                    continue
                else:
                    mass.append(int(field_for_now[i]))
            step = mass[random.randint(0,len(mass)-1)]

    else:
        mass = []
        for i in range(1,170):
            if field_for_now[i] == 'x' or field_for_now[i] == 'o':
                continue
            else:
                mass.append(int(field_for_now[i]))
        step = mass[random.randint(0,len(mass)-1)]
    field_for_now[step] = let
    steps_of_game.append(f'{step}{let}')
    print(weight_of_steps)

def pc_step(steps_of_game, field_for_now, let):
    step = random.randint(1,169)
    while field_for_now[step] == 'o' or field_for_now[step] == 'x':
        step = random.randint(1,169)
    field_for_now[step] = let
    steps_of_game.append(f'{step}{let}')

def human_step(steps_of_game, field_for_now, let):
    step = int(input('input your step[1-169]: '))
    while True:
        if field_for_now[step] == 'x' or field_for_now[step] == 'o':
            step = int(input('input another number[1-169]: '))
        else:
            break
    field_for_now[step] == let
    steps_of_game.append(f'{step}{let}')

