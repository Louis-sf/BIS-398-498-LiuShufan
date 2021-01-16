import random

print('Battle Ground is here:\n ')
print('  A B C D E F G H I J ')
for x in range(1,11):
    print(x,'x x x x x x x x x x ')
    
ROW =[]
ROW += 'ABCDEFGHIJ'

def generator():
    Horizontal = ROW[random.randrange(0,10,1)]
    Vertical = str(random.randrange(1,11,1))
    Coordinate = Vertical + Horizontal
    return Coordinate

print('\nshot!! ' + generator())
while True: 
    U = (input("Please type N or H: ")).upper()
    if U != 'N' and U != 'H':
        print('Please type ONLY N OR H:')
        continue
    if U == 'N':
        print('\nwhat about this time! \nshot!! ' + generator())
        continue
    if U=='H':
        print("You sank their battleship!")
        break
    