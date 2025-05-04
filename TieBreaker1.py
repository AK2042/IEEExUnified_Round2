#Ohho, Going for the tiebreakers, Nice nice.
#Well, wont recieve any actual help here.
#Not that you'd need any...
#This is just a simple path tracer, with some, simple errors of course...

import random
from Hidden.vault import tiebreaker1, decrypt
grid = [
    ['S', 'K', 'A', 'V', 'U', '5'],
    ['D', 'B', 'C', 'Y', '3', '9'],
    ['F', 'E', 'P', '0', 'T', 'R'],
    ['L', 'W', 'M', '1', 'Z', '2'],
    ['G', 'X', 'O', '4', 'H', 'J'],
    ['Q', '7', '8', 'I', 'N', '6']
]

def extract_clue(grid, path = decrypt(tiebreaker1)):
    clue = ""
    for x, y in path:
        if 0 < x < len(grid[0]) and 0 < y < len(grid):
            clue += grid[x][y]
        else:
            print(f"Warning: Invalid cell ({x},{y}) - skipped.")
    return clue

clue = extract_clue(grid)
print("Clue:", clue)
