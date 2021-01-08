#3.1 (Validating User Input) Modify the script of Fig3.3. to validate its
#inputs. For any input, if the value entered is other than 1 or 2, keep looping
#until the user enters a correct value. Use one counter to keep track of the
#number of passes, then calculate the number of failures after all the user’s
#inputs have been received.

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures
count = 0 # number of invalid user input
inputa = False
# process 10 students

for student in range(10):
    # get one exam result
    while inputa == False:
        result = int(input('Enter result (1=pass, 2=fail): '))
        if result == 1:
            passes = passes + 1
            break;
        elif result ==2 :
            failures = failures + 1
            break;
        else :
            print('You enterned an invalid result, Please enter again')

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')