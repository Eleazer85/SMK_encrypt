letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
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
            if i not in letter: 
                encrypted.append(i)
                continue
            if mode == "1":
                encrypt = (letter.index(i) + key) % 26
            elif mode == "2":
                encrypt = (letter.index(i) - key) % 26
            encrypted.append(letter[encrypt])
            
        return ''.join(encrypted)

encrypt = Encryption()
key = input("enter the key: ")
word = input("enter the word you want to encrypt / decrypt: ")
option = input("enter 1 for encrypt and 2 for decrypt: ")

result = encrypt.encrypt_caesar_cipher(key,word,option)
print(result)