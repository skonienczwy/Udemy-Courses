my_list = [10,20,30,40,50, -1, -20, -90]

new_list = [i**2 for i in my_list if i < 0]
print(my_list)
print(new_list)


sentence = 'My name is Vitor'

#isalpha check if the characters in a text are letters
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]

print(consonants)