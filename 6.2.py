#ARYAN SHARMA 16015025070

from text_utils import is_palindrome, count_vowels, word_frequency, most_common_word

paragraph = input("Enter a paragraph: ")

print("\n--- Text Analytics Report ---")

print("Palindrome:", is_palindrome(paragraph))

print("Number of vowels:", count_vowels(paragraph))

frequency = word_frequency(paragraph)
print("Word frequency:", frequency)

common = most_common_word(paragraph)

if common:
    print("Most common word(s):", common)
else:
    print("Most common word(s): None")