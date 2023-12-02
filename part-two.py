#!/usr/bin/env python3

import os
from functools import reduce

def get_game_power(data):
    parts = data.split(':')
    game_number = int(parts[0][5:])
    hands = parts[1].split(';')
    min_colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for hand in hands:
        colors = hand.strip().split(',')
        colors = [color.strip().split(' ') for color in colors]
        colors = {color[1].strip(): int(color[0].strip()) for color in colors }
        for color, count in colors.items():
            if count > min_colors.get(color, 0):
                min_colors[color] = count
    return reduce(lambda x, y: x*y, min_colors.values())

def answer(input_file):
    with open(input_file, "r") as input:
        data = input.read().split('\n')

    answer = sum([get_game_power(game) for game in data])

    print(f'The answer is: {answer}')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
