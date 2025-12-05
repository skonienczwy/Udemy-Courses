import hangman_art
import hangman_words
import random


word = random.choice(hangman_words.word_list).lower()
print(hangman_art.logo)


placeholder = ""
for i in range(len(word)):
    placeholder += '_'
    
print(placeholder)

game = True
correct_letters = []
lives = 6

while game:
    print(f"You have {lives} lives")
    print(hangman_art.hangman_art[lives])
    guess = input('Guess a Letter: ').lower()
    if guess in correct_letters:
        print(f"You  already guessed the letter '{guess.upper()}' ")
   
    display = ""
    for letter in word:
        
        if letter == guess:
            display += letter        
            correct_letters.append(guess)
            

        elif letter in correct_letters:
            display += letter 
                         
        else: 
                      
            display += "_"
            
    if guess not in word:
        lives -= 1         
        print(f"The letter '{guess.upper()}' is not in the word")    
    if lives == 0:        
        game = False
        print("Game Over")
        print(hangman_art.hangman_art[lives])        
        print(f"The word was : {word}")

    if "_" not in display:
        game = False
        print("You Win")
        

    print(display)
