#python game : rock  paper  scissor
import sys
import random
from enum import Enum
choice=int(input('Enter....,1 for rock ,2 for paper, or 3 for scissor:\n  '))
class RPS(Enum):
    rock = 1
    paper = 2
    scissor=3

if choice<1 | choice>3:
    sys.exit('you must enter a valid choice')
python_choice=random.randint(1,3)
print('you chose',str(RPS(choice).name))
print('python chose',str(RPS(python_choice).name))
if choice==1 and python_choice==2:
    print('you won')
elif choice==2 and python_choice==1:
    print('you won')
elif choice==3 and python_choice==2:
    print('you won')
elif choice==python_choice:
    print('tie game')
else:
    print("python won")


















