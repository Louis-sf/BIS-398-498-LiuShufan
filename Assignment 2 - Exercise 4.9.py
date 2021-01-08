#4.9 (Temperature Conversion) Implement a fahrenheit function that
#returns the Fahrenheit equivalent of a Celsius temperature. Use the
#following formula:
    
def Change(C):
    F = (9 / 5) * C + 32
    return F
print('Celsius \t Fahrenheit')
for i in range (101):
    print(i,'\t',Change(i))