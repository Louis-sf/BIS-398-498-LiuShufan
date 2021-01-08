# 4.12 (Simulation: The Tortoise and the Hare) In this problem, you’ll 
#recreate the classic race of the tortoise and the hare. You’ll use 
#randomnumber generation to develop a simulation of this memorable event.
import random
print("ON YOUR MARK, GET SET \nBANG !!!!! \nAND THEY'RE OFF !!!!!")

length = 70
Tposition = 0
Hposition = 0
def Hare():
   i = random.randrange(1,10,1)
   if i<=2:
       H = 0
   if i <= 4 and i>2:
       H = 9
   if i == 5:
       H = -12
   if i>5 and i<=8:
       H = 1
   if i>8:
       H = -2
   return H

def Tortoise():
   i = random.randrange(1,10,1)
   if i<=5:
       T = 3
   if i <= 7 and i>5:
       T = -6
   if i >7:
       T = 1
   return T



while Hposition<=70 and Tposition<=70:    
    for s in range(71):
        Tposition = Tposition + Tortoise()
        Hposition = Hposition + Hare()
        if Tposition<0:
            Tposition=0
        if Hposition<0:
            Hposition = 0
        if Tposition > Hposition:
            print(" "*Tposition, 'T' , " "*(Hposition-1), 'H' )
        if Tposition < Hposition:
            print(" "*Hposition, 'H' , " "*(Tposition-1), 'T' )
        if Tposition == Hposition:
            print('OUCH')
        if Tposition >= 70 or Hposition>=70:
            break
    if Tposition >= 70 and Hposition<70:
        print('Tortoise won!!')
        break
    if Hposition >= 70 and Tposition<70:
        print('Hare won!')
        break
    if Hposition>=70 and Tposition >= 70:
        print("Although it's a tie, let Tortoise win for encouragement")
        break

