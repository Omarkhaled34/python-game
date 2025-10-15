#python game : rock  paper  scissor#python game : rock  paper  scissor
import sys
import random
from enum import Enum
choice=int(input('Enter....,1 for rock ,2 for paper, or 3 for scissor:\n  '))
class RPS(Enum):
    rock = 1
    paper = 2
    scissor=3
while True:
    if choice<1 | choice>3:
        sys.exit('you must enter a valid choice')
    python_choice=random.randint(1,3)
    print(f'you chose {RPS(choice).name}')
    print(f'python chose {RPS(python_choice).name}')
    if (choice == 1 and python_choice == 3) or \
       (choice == 2 and python_choice == 1) or \
       (choice == 3 and python_choice == 2):
        print('You won!')
    elif choice==python_choice:
        print('tie game')
    else:
        print("python won")
    playagain=input('play again? (y/n)')
    if playagain=='y':
        continue
    else:
        sys.exit(" you quit the game")

