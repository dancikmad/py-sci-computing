text = "Hello Zaira"
shift = 3


def caesar(message: str, offset: int) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for char in message.lower():
        if char == " ":
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print("plain text:", message)
    print("encrypted text:", encrypted_text)


# Calling the function
caesar(text, shift)
# Returns:
# plain text: Hello Zaira
# encrypted text: khoor cdlud


# Calling the function
caesar(text, 13)
# Returns:
# plain text: Hello Zaira
# encrypted text: uryyb mnven
