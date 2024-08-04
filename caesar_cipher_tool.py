def caesar_encrypt(plain_text, shift):
    # Initialize the encrypted text as an empty string
    encrypted_text = ""
    # Iterate over each character in the plain text
    for char in plain_text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the base ASCII value depending on if the character is uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            # Encrypt the character and add it to the encrypted text
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # If the character is not an alphabet letter, add it to the encrypted text as is
            encrypted_text += char
    # Return the complete encrypted text
    return encrypted_text

def caesar_decrypt(cipher_text, shift):
    # Initialize the decrypted text as an empty string
    decrypted_text = ""
    # Iterate over each character in the cipher text
    for char in cipher_text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the base ASCII value depending on if the character is uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            # Decrypt the character and add it to the decrypted text
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # If the character is not an alphabet letter, add it to the decrypted text as is
            decrypted_text += char
    # Return the complete decrypted text
    return decrypted_text

def auto_decrypt(cipher_text, grep_word):
    # Try each possible shift value from 0 to 25
    for shift in range(26):
        # Decrypt the text using the current shift value
        decrypted_text = caesar_decrypt(cipher_text, shift)
        # Check if the specified word is in the decrypted text
        if grep_word in decrypted_text:
            # If the word is found, return the decrypted text and the shift value
            return decrypted_text, shift
    # If the word is not found, return None for both values
    return None, None

def main():
    # Display the welcome message and options
    print("Welcome to the Caesar Cipher Tool")
    print("="*32)
    print("Select an option below:")
    print("1) Encrypt")
    print("2) Decrypt")
    print("="*32)
    
    # Get the user's choice
    option = input("Enter your choice (1 or 2): ").strip()
    
    if option == '1':
        # If the user chose encryption, get the plain text and shift value
        plain_text = input("Provide the plain text: ").strip()
        shift = int(input("Provide the number of shifts: ").strip())
        # Encrypt the plain text
        encrypted_text = caesar_encrypt(plain_text, shift)
        # Display the encrypted text
        print(f"\nEncrypted Text with a shift of {shift}:")
        print("-"*32)
        print(encrypted_text)
        print("-"*32)
        
    elif option == '2':
        # If the user chose decryption, get the cipher text and the word to search for
        cipher_text = input("Provide the cipher text: ").strip()
        grep_word = input("Provide the word to search for in the decoded text: ").strip()
        # Attempt to auto-decrypt the text
        decrypted_text, shift = auto_decrypt(cipher_text, grep_word)
        
        if decrypted_text:
            # If the word was found, display the decrypted text and shift value
            print("\nFound the specified word!")
            print(f"Decoded Text using a shift of {shift}:")
            print("-"*32)
            print(decrypted_text)
            print("-"*32)
        else:
            # If the word was not found, display a message indicating so
            print("\nThe specified word was not found in any shift.")
            
    else:
        # If the user entered an invalid option, display an error message
        print("Invalid option. Please select either 1 or 2.")

if __name__ == "__main__":
    # Call the main function to run the program
    main()
