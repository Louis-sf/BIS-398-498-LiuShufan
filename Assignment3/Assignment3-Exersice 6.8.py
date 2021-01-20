#  6.8 (Challenge: Writing the Word Equivalent of a Check Amount) In
#check-writing systems, it’s crucial to prevent alteration of check amounts.
#One common security method requires that the amount be written in
#numbers and spelled out in words as well. Even if someone can alter the
#numerical amount of the check, it’s tough to change the amount in words.
#Create a dictionary that maps numbers to their corresponding word
#equivalents. Write a script that inputs a numeric check amount that’s less
#than 1000 and uses the dictionary to write the word equivalent of the
#amount. For example, the amount 112.43 should be written as

# ONE HUNDRED TWELVE AND 43/100

import math
  
single_digits =['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
 'EIGHT', 'NINE']

ten_two_digits = ['', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN', 'FOURTEEN',
 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']

tenth_digits = ['', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY', 'SIXTY', 'SEVENTY',
 'EIGHTY', 'NINETY']

tens_power =['HUNDRED']
def check_write(number):
    if number>0:
        digits = int(math.log10(number))+1
    elif number == 0:
        digits = 1
    else:
        digits = -1
    if digits == 0:
        print('Empty input')
        return
    if digits>=4:
        print('Our prgram cannot process such a big nmumber')
        return
    if digits ==-1:
        print('Monetary value cannot be negative')
    printnumber = int(number)
    #For Single digit number
    if digits ==1:
        printnumber = int(number)
        print(single_digits[printnumber],end =' ')
    #For numbers between 10 and 20
    if digits ==2 and number < 20:
        print(ten_two_digits[printnumber-9],end =' ')
    #For numbers between 20 and 99
    if number<100 and number >=20:
        tenth = int(printnumber/10)
        unit = printnumber-tenth*10
        print(tenth_digits[tenth-1], end = ' ')
        if unit!= 0:
            print(single_digits[unit])        
    #For numbers between 100 and 1000
    if number>=100 and number<1000:
        hundredth = int(printnumber/100)
        tenth = int((printnumber-hundredth*100)/10)
        unit = printnumber-hundredth*100-tenth*10
        print(single_digits[hundredth],tens_power[0], end = ' ')
        if tenth != 1:            
            if tenth == 0 and unit != 0:
                print('AND', single_digits[unit],end=' ')
            if tenth!= 0 and unit ==0:
                print(tenth_digits[tenth-1],end=' ')
            if tenth!=0 and unit!=0:
                print(tenth_digits[tenth-1],single_digits[unit],end=' ')
        if tenth == 1:
            if unit == 0:
                print(ten_two_digits[1],end=' ')
            if unit != 0:
                print('AND', ten_two_digits[unit+1],end=' ')
    if number !=printnumber:
        print('AND', int(100*(number-printnumber)), end ='')
        print('/100')

inputs = float(input('Enter a number smaller than 1000: '))        
check_write(inputs)










        