'''
cube = [
    [
        ['R', 'R', 'R'],
        ['R', 'R', 'R'],
        ['R', 'R', 'R']
    ],
    [
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G']
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
            ['G', 'G', 'G'],
            ['G', 'G', 'G'],
            ['G', 'G', 'G']
        ],
        [
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y'],
            ['Y', 'Y', 'Y']
        ]
    ]
    return cube;

def print_pretty_cube(cube):
    print(cube[0])
    print(cube[1])
    print(cube[2])

def remove_piece(cube, num_pieces):
    i = 0
    while(i < num_pieces):
        x = random.randrange(0,3)
        y = random.randrange(0,3)
        z = random.randrange(0,3)
        if cube[x][y][z] != ' ':
            temp = [x,y,z]
            removed_block_list.append(temp)
            cube[x][y][z] = ' '
            i += 1

def generate_choices(cube, removed_blocks):
    choices = []  # List to store all choices

    correct_choice = removed_blocks[:] # copy of the list of removed blocks
    choices.append(correct_choice)

    while len(choices) < 4:
        distractor = []
        for _ in range(len(removed_blocks)):
            random_pos = [random.randrange(0, 3), random.randrange(0, 3), random.randrange(0, 3)]

            if random_pos not in distractor and (random_pos) not in correct_choice:
                distractor.append(random_pos)

        if distractor not in choices:
            choices.append(distractor)

    random.shuffle(choices)
    return choices

cube = generate_cube()
removed_block_list = [];
num_piece_to_remove = random.randrange(1,6)
print('\nnum_piece_to_remove: ' + str(num_piece_to_remove) + '\n')
remove_piece(cube, num_piece_to_remove)
print('removed_block_list: ')
print(removed_block_list)
print()
print_pretty_cube(cube)
print('\nMultiple Choices: ')
final_choices = generate_choices(cube, removed_block_list)
for i, choice in enumerate(final_choices):
    print(f"Option {i + 1}: {choice}")