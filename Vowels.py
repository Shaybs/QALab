word = input("Enter a word: ").lower()
vowels_number = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for i in word:
    if i in vowels:
        vowels_number += 1

print('The number of vowels are: ', vowels_number)
