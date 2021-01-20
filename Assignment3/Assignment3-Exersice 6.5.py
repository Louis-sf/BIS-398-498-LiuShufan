#  (Counting Duplicate Words) Write a script that uses a dictionary to
#determine and print the number of duplicate words in a sentence. Treat
#uppercase and lowercase letters the same and assume there is no
#punctuation in the sentence. Use the techniques you learned in Section


text = ('This is sample text with several words This is a sentence that '
        'Does not have punctuation and Does Not FoLLow the General RulE of '
        'CaPiTAL LEtter and LowER CAse letteR')
text = text.lower()
word_counts = {}
# count occurrences of each unique word
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f'{"Duplicated Word": <10}Count')
for word, count in sorted(word_counts.items()):
    if count >1:
        print(f'{word: <10}{count}')
        

