"""SecTalks CTF101 - 02 - Cryptoanalysis
Brute-force Caesar cipher
"""

cipher = 'FVBJHUIYLHRJVKLHUKFVBHYLWYVBKVMPA'
#cipher = 'FRPGNYXFZRRGHCFNERNOBHGCNEGVPVCNGVATVAVGFRPHEVGLQVFPHFFVBAFYRNEAVATSEBZBGUREFNAQVZCEBIVATCEBOYRZFBYIVATFXVYYF'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    plaintext = ''

    for symbol in cipher:  # Loop through each character of cipher
        if symbol in LETTERS:
            position = LETTERS.index(symbol)  # Find symbol in alphabet
            position = position - key  # Replaced with key previous letter

            # If position is negative, add 26, length of alphabet
            if position < 0:
                position = position + len(LETTERS)

            # Decryption: added the letter than the key position to plaintext
            plaintext = plaintext + LETTERS[position]

        else:
            # Symbol not find, just add cipher character with no decription
            plaintext = plaintext + symbol

    print('Key #{0}: {1}'.format(key, plaintext))
