'''
cube = [
    [
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R']
    ],
    [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O']
    ],
    [
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y'],
        ['Y', 'Y', 'Y']
    ]
] 
'''


import random

def generate_cube():
    cube = [
        [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']
        ],
        [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ],
        [
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y']
        ]
    ]
    return cube;

def remove_piece(cube, num_pieces):
    return 0