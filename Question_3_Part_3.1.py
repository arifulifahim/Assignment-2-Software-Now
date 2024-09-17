def encrypt(text, key):
    # Initialize an empty string to store the encrypted result
    encrypted_text = ""
    # Iterate through each character in the text
    for char in text:
        # Check if the character is an alphabet letter (ignores numbers, punctuation, etc.)
        if char.isalpha():
            shifted = ord(char) + key  # Get the ASCII value and shift it by 'key'
            # For lowercase letters
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26  # Wrap around if it goes past 'z'
                elif shifted < ord('a'):
                    shifted += 26  # Wrap around if it goes before 'a'
            # For uppercase letters
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26  # Wrap around if it goes past 'Z'
                elif shifted < ord('A'):
                    shifted += 26  # Wrap around if it goes before 'A'
            # Add the encrypted (shifted) character to the result
            encrypted_text += chr(shifted)
        else:
            # If the character is not an alphabet letter, keep it unchanged
            encrypted_text += char
    
    # Return the fully encrypted text
    return encrypted_text
#Corrected Decryption Function (with Comments):
def decrypt(text, key):
    # Initialize an empty string to store the decrypted result
    decrypted_text = ""
    # Iterate through each character in the text
    for char in text:
        # Check if the character is an alphabet letter (ignores numbers, punctuation, etc.)
        if char.isalpha():
            shifted = ord(char) - key  # Get the ASCII value and shift it back by 'key'
            # For lowercase letters
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around if it goes before 'a'
                elif shifted > ord('z'):
                    shifted -= 26  # Wrap around if it goes past 'z'
            # For uppercase letters
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around if it goes before 'A'
                elif shifted > ord('Z'):
                    shifted -= 26  # Wrap around if it goes past 'Z'
            # Add the decrypted (shifted) character to the result
            decrypted_text += chr(shifted)
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += char
    
    # Return the fully decrypted text
    return decrypted_text

