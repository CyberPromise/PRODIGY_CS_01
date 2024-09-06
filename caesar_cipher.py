# prompt: Task-01
# Implement Caesar Cipher
# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption

def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using the Caesar Cipher.

  Args:
    text: The text to be processed.
    shift: The number of positions to shift the characters.
    mode: 'encrypt' to encrypt, 'decrypt' to decrypt.

  Returns:
    The processed text.
  """
  result = ''
  for char in text:
    if char.isalpha():
      start = ord('a') if char.islower() else ord('A')
      shifted_char = chr(((ord(char) - start + shift) % 26) + start)
    elif char.isdigit():
      shifted_char = str((int(char) + shift) % 10)
    else:
      shifted_char = char
    result += shifted_char
  return result

if __name__ == "__main__":
  message = input("Enter the message: ")
  shift = int(input("Enter the shift value: "))
  mode = input("Encrypt or decrypt? (encrypt/decrypt): ").lower()

  if mode == 'encrypt':
    encrypted_message = caesar_cipher(message, shift, mode)
    print("Encrypted message:", encrypted_message)
  elif mode == 'decrypt':
    decrypted_message = caesar_cipher(message, -shift, mode)
    print("Decrypted message:", decrypted_message)
  else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
