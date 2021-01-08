#3.16 (Nested Control Statements) Use a loop to find the two largest values
#of 10 numbers entered.

m = float(input('enter a number: '))
for i in range(9):
    n=float(input('enter a number: '))
    if n>m:
        m=n
print('the largest number you entered is ', m)        
