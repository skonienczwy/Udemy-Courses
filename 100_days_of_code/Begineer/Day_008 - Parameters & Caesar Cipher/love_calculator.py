'''You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.  
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. '''



def calculate_love_score(name1, name2):
    true_word = 'true'
    love_word = 'love'

    letter_count1 = 0
    letter_count2 = 0

    for i in range(len(name1)):    
        for n in range(len(true_word)):
            if name1[i] == true_word[n]:               
                letter_count1 += 1
        
    for i in range(len(name2)):    
        for n in range(len(true_word)):
            if name2[i] == true_word[n]:   
                letter_count1 += 1       

    for i in range(len(name1)):    
        for n in range(len(love_word)):
            if name1[i] == love_word[n]:               
                letter_count2 += 1
        
    for i in range(len(name2)):    
        for n in range(len(love_word)):
            if name2[i] == love_word[n]:   
                letter_count2 += 1 
    print(str(letter_count1) + str(letter_count2))


calculate_love_score(name1="Kanye West", name2="Kim Kardashian")




    


  


# print(test)    