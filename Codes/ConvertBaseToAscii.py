# Binary
def ConvertBinaryToAscii(Binary):
    Int = 0
    for i in range(8):
        Int += int(Binary[i]) * (2**(7-i))
    return chr(Int)

Input = "01100011 01101111 01101100 01101111 01110010 01100001 01100100 01101111".split(" ")
print("Input:", Input)
Plaintext = "".join([ConvertBinaryToAscii(Binary) for Binary in Input])
print("Plaintext:", Plaintext)


# Octal
def ConvertOctalToAscii(Octal):
    Int = int(Octal[0]) * 64 + int(Octal[1]) * 8 + int(Octal[2]) * 1
    return chr(Int)

Input = "157 166 145 156".split(" ")
print("Input:", Input)
Plaintext = "".join([ConvertOctalToAscii(Octal) for Octal in Input])
print("Plaintext:", Plaintext)


# Hexadecimal
def ConvertHexadecimalToAscii(Hex):
    Int = int(Hex[0]) * 16 + int(Hex[1])
    return chr(Int)

Input = "73 74 72 65 65 74".split(" ")
print("Input:", Input)
Plaintext = "".join([ConvertHexadecimalToAscii(Hex) for Hex in Input])
print("Plaintext:", Plaintext)
