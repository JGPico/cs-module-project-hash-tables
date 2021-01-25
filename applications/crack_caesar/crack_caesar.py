# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    words = f.read()

string_list = words.split()

giant_string = ''.join(string_list)

wanted_characters = "abcdefghijklmnopqrstuvwxyz"

letter_count = {}
total_letters = 0

english_percentages = {
    "e": 11.53,
    "t": 9.75,
    "a": 8.46,
    "o": 8.08,
    "h": 7.71,
    "n": 6.73,
    "r": 6.29,
    "i": 5.84,
    "s": 5.56,
    "d": 4.74,
    "l": 3.92,
    "w": 3.08,
    "u": 2.59,
    "g": 2.48,
    "f": 2.42,
    "b": 2.19,
    "m": 2.18,
    "y": 2.02,
    "c": 1.58,
    "p": 1.08,
    "k": 0.84,
    "v": 0.59,
    "q": 0.17,
    "j": 0.07,
    "x": 0.07,
    "z": 0.03
}
given_percentages = {}
cypher = {}

# Get letter count
for letter in giant_string:
    letter = letter.lower()

    if letter in letter_count and letter in wanted_characters:
        letter_count[letter] += 1
        total_letters += 1

    elif letter in wanted_characters:
        letter_count[letter] = 1
        total_letters += 1

# Sort letters
sorted_letter_count = sorted(
    letter_count.items(), key=lambda pair: pair[1], reverse=True)

# Get percentage of letters being used
for pair in sorted_letter_count:
    percentage = round((100 * float(pair[1])/float(total_letters)), 2)
    given_percentages[pair[0]] = percentage

# Build cypher based on percentages
for letter in english_percentages:
    for given_letter in given_percentages:
        if english_percentages[letter] == given_percentages[given_letter]:
            cypher[given_letter] = letter


# Translate
translated = ''

for letter in words:
    if letter.lower() in cypher:
        letter = cypher[letter.lower()]

    translated += str(letter)


print(translated)
