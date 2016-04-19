"""SecTalks CTF101 - 02 - Cryptoanalysis
Create Caesar cipher for every possible keys
"""

message = 'SecTalks meetups are about participating in IT security discussions, learning from others, and improving problem-solving skills.'
message = 'SecTalks meetups are about participating in IT security discussions, learning from others, and improving problem-solving skills. SecTalks offers an avenue where you can team-up with likeminded people to participate in solving technical IT security challenges'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    cipher = ''

    for symbol in message.upper():  # Loop through each character of message
        if symbol in LETTERS:
            position = LETTERS.index(symbol)  # Find symbol in alphabet
            position = position + key  # Replaced letter with key+position

            # If position is negative, add 26, length of alphabet
            if position > 25:
                position = position - len(LETTERS)

            # Encryption
            cipher = cipher + LETTERS[position]

        else:
            # Symbol not find, just add character with no encryption
            cipher = cipher + symbol

    print('Key #{0}: {1}'.format(key, cipher))
