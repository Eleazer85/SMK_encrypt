letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W','X','Y','Z']
punctuation_pattern = ["?","!",",","."," ","1","2","3","4","5","6","7","8","9","0"]

class Encryption():
    def encrypt_caesar_cipher(self,key,word):
        try:
            key = int(key)
        except ValueError:
            raise ValueError("The key should can only be an integer") 
        
        encrypted = []
        for i in word: 
            if i in punctuation_pattern: 
                encrypted.append(i)
            else: 
                i = i.upper()
                encrypt = (letter.index(i) + key) % 26
                encrypted.append(letter[encrypt])
        return ''.join(encrypted)
    
    def decrypt_caesar_cipher(self,key,word):
        try:
            key = int(key)
        except ValueError:
            raise ValueError("The key should can only be an integer") 
        
        decrypted = []
        for i in word: 
            if i in punctuation_pattern: 
                decrypted.append(i)
            else: 
                i = i.upper()
                decrypt = (letter.index(i) - key) % 26
                decrypted.append(letter[decrypt])
            
        return ''.join(decrypted)

encrypt = Encryption()
key = input("enter the key: ")
word = input("enter the word you want to encrypt / decrypt: ")
option = input("enter 1 for encrypt and 2 for decrypt: ")

if option == "1":
    print(encrypt.encrypt_caesar_cipher(key,word))
elif option == "2":
    print(encrypt.decrypt_caesar_cipher(key,word))
else: 
    print("invalid input")