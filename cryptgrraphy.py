small_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
capital_letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

def Cryptography():
    """
    An interactive Caesar Cipher-based encryption and decryption program.

    This function continuously prompts the user to choose between encryption or decryption
    using a Caesar Cipher technique with a user-defined shift key. It works for both
    uppercase and lowercase English letters, while keeping non-alphabet characters unchanged.

    Features:
    - Encrypt: Shifts each letter forward in the alphabet by the key value.
    - Decrypt: Shifts each letter backward in the alphabet by the key value.
    - Handles both uppercase and lowercase letters.
    - Leaves symbols, digits, and spaces unchanged.
    - Asks the user whether to continue or exit after each operation.

    Example:
    >>> Enter 'encrypt' for encryption and 'decrypt' for decryption: encrypt
    >>> Enter the word to encrypt or decrypt: Hello
    >>> Enter the shift key: 2
    >>> Encrypted form is Jgnnq

    Note:
    This uses the Caesar cipher logic and is meant for educational or simple text transformation purposes.

    """
    # function code continues...

    while True:
        text = input("Enter 'encrypt' for encryption and 'decrypt' for decryption: ").lower()
        if text in ('encrypt', 'decrypt'):
            norm_text = input("Enter the word to encrypt or decrypt: ")
            key = int(input('Enter the shift key: '))
            encrypt_key = key if text == 'encrypt' else -key

            modified_text = ""
            for char in norm_text:
                if char in small_letters:
                    i = (small_letters.index(char) + encrypt_key) % 26
                    modified_text += small_letters[i]
                elif char in capital_letters:
                    j = (capital_letters.index(char) + encrypt_key) % 26
                    modified_text += capital_letters[j]
                else:
                    modified_text += char
            print(f'Encrypted form is {modified_text}' if text == 'encrypt' else f'Decrypted form is {modified_text}')
        else:
            print("Enter correct string!")

        while True:
            resume = input("Wanna continue (yes/no): ").strip().lower()
            if resume == 'no':
                print("Goodbye")
                return
            elif resume == 'yes':
                break
            else:
                print("Please enter 'yes' to continue or 'no' to exit.")

Cryptography()
# print(Cryptography.__doc__)
