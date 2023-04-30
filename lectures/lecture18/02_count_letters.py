# Challenge: 
#   1. How many unique letters are in the word supercalifragilisticexpialidocious?
#   2. How many times does each letter occur?

# Your job: loop through each letter of the word.


word = 'supercalifragilisticexpialidocious'
for letter in word:
    print(letter)

letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
    
print(str(letter_count))