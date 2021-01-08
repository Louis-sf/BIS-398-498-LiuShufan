#Exercise 2.8
# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares
# and cubes of the numbers from 0 to 5. Print the resulting values in table
# format, as shown below. Use the tab escape sequence to achieve the threecolumn output.

print("Number\t square\t cube\t\n")
for number in range (6):
    square = number**2
    cube = number**3
    print(number, "\t", square, "\t" , cube , "\t" )