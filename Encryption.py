letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W','X','Y','Z']

class Encryption():
    def encrypt_caesar_cipher(self,key,word,mode):
        #check if the key is a number
        try:
            key = int(key)
        except ValueError:
            raise ValueError("The key should can only be an integer") 
        
        encrypted = []
        word = word.upper()
        
        #check if there is some symbol or number in the word
        for i in word: 
            if i not in letters: 
                encrypted.append(i)
                continue
            if mode == "1":
                encrypt = (letters.index(i) + key) % 26
            elif mode == "2":
                encrypt = (letters.index(i) - key) % 26
            encrypted.append(letters[encrypt])
            
        return ''.join(encrypted)
    
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

encrypt = Encryption()
encryption_method = input("enter the encryption method (Caesar or vigenere)").lower()
key = input("enter the key: ")
word = input("enter the word you want to encrypt / decrypt: ")
option = input("enter 1 for encrypt and 2 for decrypt: ")

if encryption_method == "caesar": 
    result = encrypt.encrypt_caesar_cipher(key,word,option)
elif encryption_method == "vigenere":
    result = encrypt.encrypt_vigenere(key,word,option)
else: 
    raise ValueError("Invalid encryption method option")

print(result)