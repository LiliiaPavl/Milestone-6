def caesar_encrypt(message, key):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char

    return encrypted_message

key = int(input("Enter key: "))
message = input("Enter message: ")

result = caesar_encrypt(message, key)

print("\nResult:", result)