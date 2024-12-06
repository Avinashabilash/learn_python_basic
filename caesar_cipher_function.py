alpha = list('abcdefghijklmnopqrstuvwxyz')

def encryption(plain_text, shift_key):
    cipher_text = ""
    plain_text = plain_text.lower()  # Convert input text to lowercase
    for char in plain_text:
        if char in alpha:  # Check if the character is alphabetic
            position = alpha.index(char)
            new_position = (position + shift_key) % 26  # Apply shift
            cipher_text += alpha[new_position]  # Append shifted character
        else:
            cipher_text += char  # Preserve non-alphabetic characters
    print(f"Here we have the text after encryption: {cipher_text}")

def decryption(plain_text, shift_key):
    cipher_text = ""
    plain_text = plain_text.lower()  # Convert input text to lowercase
    for char in plain_text:
        if char in alpha:  # Check if the character is alphabetic
            position = alpha.index(char)
            new_position = (position - shift_key) % 26  # Apply shift
            cipher_text += alpha[new_position]  # Append shifted character
        else:
            cipher_text += char  # Preserve non-alphabetic characters
    print(f"Here we have the text after decryption: {cipher_text}")

wanna_end=False

while not wanna_end:
   Type = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
   text = input("Type your message:\n")
   shift = int(input("Enter shift key:\n"))
   if Type == "encrypt" or Type == "enc":
       encryption(plain_text=text, shift_key=shift)
   elif Type == "decrypt" or Type == "dec":
       decryption(plain_text=text, shift_key=shift)
   paly_again=input("Type 'yes' to continues,type 'no' to exit:\n")
   if paly_again =='N'.lower() :
      wanna_end=True
      print("try until u wanna cark it ..")

