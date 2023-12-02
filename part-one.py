#!/usr/bin/env python3

import os

max_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_game_value(data):
    parts = data.split(':')
    game_number = int(parts[0][5:])
    hands = parts[1].split(';')
    for hand in hands:
        colors = hand.strip().split(',')
        colors = [color.strip().split(' ') for color in colors]
        colors = {color[1].strip(): int(color[0].strip()) for color in colors }
        for color, count in colors.items():
            if count > max_values.get(color, 0):
                return 0
    return game_number

def answer(input_file):
    with open(input_file, "r") as input:
        data = input.read().split('\n')

    answer = sum([get_game_value(game) for game in data])

    print(f'The answer is: {answer}')

input_file = os.path.join(os.path.dirname(__file__), "input")
answer(input_file)
