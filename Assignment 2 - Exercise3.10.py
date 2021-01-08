#  3.10 (7% Investment Return) Reimplement Exercise 2.12 to use a loop
#that calculates and displays the amount of money you’ll have each year at
#the ends of years 1 through 30.

p=1000
r=7
n = 1
while n<=30:
    p = p*(1+r/100)**n
    print("In year", n, "the return is: ", p)
    n=n+1