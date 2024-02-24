letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W','X','Y','Z']

class encryption():
    def encrypt_vigenere(self,key,word,mode):
        encrypted = []
        key_len = len(key)
        
        #turn the key and word into upper case
        word = word.upper()
        key = key.upper()
        
        #checking if there is a punctuation character / number
        for i in key: 
            if i not in letters: 
                raise ValueError("The key can only contain letters")
        iterate = 0
        
        for letter in word: 
            if letter not in letters:
                encrypted.append(letter)
                continue

            letter = letter.upper()
            if mode == "1":
                encrypt = (letters.index(letter) + letters.index(key[iterate % key_len])) % 26
            elif mode == "2":
                encrypt = (letters.index(letter) - letters.index(key[iterate % key_len])) % 26
            else:
                raise ValueError("Invalid mode option")
            encrypt = letters[encrypt]
            encrypted.append(encrypt)
            iterate += 1
            
        return "".join(encrypted)
        
encrypt = encryption()

print("please note that this code only take text for the key and cannot contain any number")
input_key = input("please enter the key: ")
input_word = input("please enter the word you want to encrypt: ")
input_mode = input("please enter the mode of encryption 1[encrypt] or 2[decrypt]: ")

result = encrypt.encrypt_vigenere(input_key,input_word,input_mode)
print(result)