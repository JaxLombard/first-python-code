message = input("Enter a message to encode or decode: ")
message = message.upper()   #Makes the message UPPERCASE
output = ""                 #Creates an empty string to hold the output
for letter in message:
    if letter.isupper:
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.isupper():
            value-= 26
            letter = chr(value)
    output += letter
print("Outside message: ", output)
