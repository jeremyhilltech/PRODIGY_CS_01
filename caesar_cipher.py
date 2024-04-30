FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shifter(user_input, shift_value):
# Result Placeholder
    result = ""

    # Go through each of the characters in the message given by user input. 
    for char in user_input.upper():
        if char .isalpha():
        # Convert character into ASCII Code
            char_code = ord(char)
            new_char_code = char_code + shift_value

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    print(result)

user_message = input("Secret message to encrypt/decrypt?:")
user_shift = int(input("Shift by how many values?"))
caesar_shifter(user_message, user_shift)