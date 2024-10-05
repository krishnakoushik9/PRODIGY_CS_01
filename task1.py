# I did not use object oriented coding for these tasks
# I will make sure to learn POOP and then work on these in the future

while True:
    choice = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit: ").lower()

    if choice == 'q':
        break

    elif choice in ['e', 'd']:
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (1-25): "))

        result = ""
        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                if choice == 'e':
                    shifted = (ord(char) - ascii_offset + shift) % 26
                else:
                    shifted = (ord(char) - ascii_offset - shift) % 26
                result += chr(shifted + ascii_offset)
            else:
                result += char

        if choice == 'e':
            print(f"Encrypted message: {result}")
        else:
            print(f"Decrypted message: {result}")

    else:
        print("Invalid input. Please try again.")

print("Thank you for using the Caesar Cipher program!(Prodigy Cyber security)")
print("This was Task - 1")
print("All the codes are written in python in ZED IDE")
