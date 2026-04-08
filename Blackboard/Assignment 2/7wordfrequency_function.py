'''The following program takes user input of a sentence and
calculates the number of times a word is repeated and
prints the total number of times each word in a sentence is repeated'''

# Function to calculate word frequency in a sentence
def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Asking user for a sentence
print("Enter a sentence:")
user_sentence = input()

# Calling the function
result = word_frequency(user_sentence)

# Print the frequency dictionary as output
print("Word frequency:")
for word, count in result.items():
    print(word, ":", count)

# By Biplab Prasad Gajurel 25024641