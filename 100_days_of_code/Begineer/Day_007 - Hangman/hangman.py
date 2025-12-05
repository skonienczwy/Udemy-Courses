import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list).lower()

placeholder = ""

for i in range(len(chosen_word)):
    placeholder += "_"
  
game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"*******************YOU HAVE {lives} LIVES LEFT*******************")
    print(chosen_word)
    guess = input("Guess the letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed the letter '{guess.upper()}' previously.")
      

    display = "" 

    for letter in chosen_word:
        if guess == letter:
            display += letter 
            correct_letters.append(guess)     
        elif letter in correct_letters:
            display +=  letter             
        else:
            display += "_"            
                        
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess.upper()}', that's not in the word. You lose a life.")
    if lives == 0:
        game_over = True
        print("*******************YOU LOSE*******************")
            
    if "_" not in display:
        game_over = True
        print("*******************YOU WIN*******************")

    print(hangman_art.hangman_art[lives])




