#5.11 (Summarizing Letters in a String) Write a function
#summarize_letters that receives a string and returns a list of tuples
#containing the unique letters and their frequencies in the string. Test your
#function and display each letter with its frequency. Your function should
#ignore case sensitivity (that is, 'a' and 'A' are the same) and ignore
#spaces and punctuation. When done, write a statement that says whether
#the string has all the letters of the alphabet.

def alphabetchecker(string):   
    alphabet = []
    alphabet += 'abcdefghijklmnopqrstuvwxyz'
    letter = []
    letter += string
    letter = [str(i).lower() for i in letter]
    letteronly = []
    for i in range(len(letter)):
        if letter[i] in alphabet:
            letteronly += letter[i]
    sorted_letter = sorted(letteronly)  
    store = {}
    for i in range(len(sorted_letter)):
        key = sorted_letter[i]
        store[key] = 0     
    for lett in sorted_letter: 
        if lett in sorted_letter: 
            store[lett] += 1
        else:
            store[lett] = 1       
    if store:
        print('Your input has the following alphabet: \n')
        for key, value in store.items():
            print(f' {key: <10}{value}')
        if len(store) == 26:
            print('The input has all the alphabet!')      
    else:                
        print('too bad, there is no alphabet in your input')
                 
 
alphabetchecker(input('Please enter your input here: '))
