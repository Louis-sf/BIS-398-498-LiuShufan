#  Create a string called alphabet
# containing 'abcdefghijklmnopqrstuvwxyz', then perform the
# following separate slice operations to obtain:
    
alphabet = []
alphabet += 'abcdefghijklmnopqrstuvwxyz'

#1.  The first half of the string using starting and ending indices
alphabet[0 : 13]

#2. The first half of the string using only the ending index
alphabet[ : 13]

#3. The second half of the string using starting and ending indices.
alphabet[13 : 26]

#4. The second half of the string using only the starting index.
alphabet[13 : ]

#5. Every second letter in the string starting with 'a'.
alphabet[ :: 2 ]

#6. The entire string in reverse.
alphabet[ :: -1 ]

#7. Every third letter of the string in reverse starting with 'z'.
alphabet[ :: -3 ]
