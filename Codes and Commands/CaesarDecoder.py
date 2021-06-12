Ciphertext = "ynkooejcpdanqxeykjrbdofgkq"
Ciphertext = Ciphertext.upper()
Ciphertext = [ord(Letter)-65 for Letter in Ciphertext]

for Shift in range(26):
    print("Shift:{}, plantext:{} or {}".format(
        Shift, "".join([chr( (Int+Shift)%26 + 65 ) for Int in Ciphertext]), "".join([chr( (Int+Shift)%26 + 97 ) for Int in Ciphertext]) 
    ))