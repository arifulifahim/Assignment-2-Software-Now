#Decryption function to decrypt the 'encrypted code' back to the original code
def decrypt(text, key):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key  # Shift character back by the key value
            
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around if before 'a'
                elif shifted > ord('z'):
                    shifted -= 26  # Wrap around if past 'z'
            
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around if before 'A'
                elif shifted > ord('Z'):
                    shifted -= 26  # Wrap around if past 'Z'
            
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    
    return decrypted_text



