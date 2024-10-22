def caesar_decrypt(message, key):
    decrypted_message = ""

    for char in message:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_message += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted_message += char

    return decrypted_message

key = int(input("Enter key: "))
message = input("Enter message: ")

result = caesar_decrypt(message, key)

print("\nResult:", result)