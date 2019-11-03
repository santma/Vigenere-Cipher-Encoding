# Vigenere-Cipher-Encoding:
A cryptography exercise in python for a data security course.

##  What is Vigenere Cipher Encoding?
Vigenere cipher is basic a way to encrypt alphabetical text. Here is a step-by-step in plain English: 
1. Take your text and give each letter a number.
                  a = 0, b = 1, c = 2, ... , z = 25
                  
      So this: 
      
                  THISISREALLYEASY
                  
      Becomes:
      
                  19 7 8 18 8 18 17 4 0 11 11 24 4 0 18 24 
                  
2. Split the digits up into groupings. For example groups of four:
                  
                  19 7 8 18 | 8 18 17 4 | 0 11 11 24 | 4 0 18 24

3. Create your KEY with the same length as your groupings. Let's make the key:

                  5 , 2 , 8 , 10

4. Then, apply some formula using each key number to the corresponding number in the groups. Let's use arithmetic.

                  19+5 7+2 8+8 18+10 | 8+5 18+2 17+8 4+14 | ......
                  
      But, we must do our calculations in modulo 26, which is means that when you surpass 26 or multiples of 26, you just go back to 0. The modulo is that fun % symbol in programming.
      For the example above, 18 + 10 = 28 % 26 = 2. (In our case it is 2, since our index starts at A = 0). 

      So now we have this:
      
                  24 9 16 2 | 13 20 25 16 | 5 13 19 8 | 9 2 0 8
                  
5. Finally, we change the numbers back to letters again:
        
        THISISREALLYEASY --> YJQCNUZQFNTIJCAI
        
6. To decrypt, you do the exact same thing but with the reverse function. This assumes that you know what the key is. If you do not know what the key is, then you need some more analysis of the ecrypted text dealing with distributions of the letters and probabilities of letter combinations. Some methods for this to Google are "Kasiski" test to find the "Index of Coincidence". I'll keep it basic for now, since this is mostly a Python exercise. So for the time being, the key is known.

## How the code works

1. Encryption:

      We create a variable 'alphabet', which will come into play later:
                
                alphabet = 'abcdefghijklmnopqrstuvwxyz'

      When you run the code, the user is prompted to enter a message. The message is converted from a string type to a list which we call 'plaintext' (essentially splitting up the letters).
      
                message = input('enter message:')
                plaintext = list(message)
                
      The user also enters a numerical key. The code splits this up into an array called 'K'.
      
                    key = input('enter Key:')
                    K = [int(i) for i in key.split(',')]
      
       We also need to take the length of the key 'K' and set it to a variable 'm'. This will be the number for our groupings in step 4 above.
      
                    m = len(K)
                    
       Now, we need to create a list object (a list of arrays) out of the plaintext list of letters which we call 'ek'. This will group our letters in to groups of size 'm'.
       
                    ek = [plaintext[i:i+m] for i in range(0,len(plaintext),m)]
                    
       Then, we iterate through each letter in the groupings 'ek' and add the corresponding 'K'values. We add the values according to their position in the 'alphabet' string. When we add to the position, we use the magical '%' symbol for the modulo, so that the position sticks to the number of letters in the alphabet. We put all these values in the 'encrypt' variable.
       
                        encrypt = []
                        for i in ek:
                            position = [alphabet.find(letter) for letter in i]
                            for i in range(0,len(position)):
                            encrypt.append((position[i] + K[i])%26)
        
        Now we have a list of numbers that correspond to the encrypted message. Now we convert this into a list of letters called 'ciphertext', which we convert back to a string called 'encrypted_message'. Note: I cannot remember why I put 'c + 97', but I'll edit when it comes to me.
        
                           ciphertext = []
                           for i in encrypt:
                               c = i + 97
                               cipher = chr(c)
                               ciphertext.append(cipher)
        
                            encrypted_message = ''.join(str(e) for e in ciphertext)
                            
2. Decryption:

        For decription, the user enters an encrypted message and the key. This is not very realistic since usually you would not have the key. Anyway, the code is exactly the same except the K values are subtracted from the position rather than added.
        
                            encrypt.append((position[i] - K[i])%26) 
                            
                            
Conclusion: this is primarily a python exercise. It gives us some insight into encryption, but in this case the key is known.
       
                     
                
