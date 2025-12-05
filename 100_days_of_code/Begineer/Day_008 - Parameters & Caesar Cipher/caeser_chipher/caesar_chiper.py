import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(encode_or_decode, word, shift_amount):
     
     if encode_or_decode == 'encode' :             
        encrypted_word = ""
        for letter in word.lower():
            if letter not in alphabet:
               encrypted_word += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                '''This row prevents the out of range index. Keeping the range between 0-25 of alphabet.
                  shifted_position = index of alphabet + shift_amoun. Taking this result and calulating with
                  the number of elements in alphabet, it will always keep inside the range.'''                 
                shifted_position %= len(alphabet)
                encrypted_word += alphabet[shifted_position]           
  
        print(f"Here is the encoded result: {encrypted_word}") 

     elif encode_or_decode == 'decode' :
        decrypted_word = ""
        for letter in word.lower():
          if letter not in alphabet:
            decrypted_word += letter
          else:       
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            decrypted_word += alphabet[shifted_position]


        print(f"Here is the decoded result: {decrypted_word}") 

looping = True

while looping:

   direction = input(("Type 'encode' to encrypt , type 'decode' to decrypt: \n").lower())

   if direction == 'encode' or direction == 'decode':
      text = input("Type the message you want to encrypt: \n").lower()
      shift = int(input("Type the shift number: \n"))
      caesar(encode_or_decode=direction, word=text, shift_amount=shift)


   choose = input("Type 'Yes' if you want to go again. Otherwise type 'No'. \n")
   if choose.lower() == 'no':
      looping = False
      print("Bye Bye!")
   elif choose.lower() != 'no' or choose.lower() != 'yes' :      
      print("Invalid Option.")





    
      
       