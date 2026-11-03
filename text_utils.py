#ARYAN SHARMA 16015025070
def is_palindrome(s):
    text = ''.join(s.lower().split())
    return text == text[::-1]


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count


def word_frequency(s):
    words = s.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:'\"")
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


def most_common_word(s):
    frequency = word_frequency(s)

    if not frequency:
        return None

    max_count = max(frequency.values())
    common_words = []

    for word, count in frequency.items():
        if count == max_count:
            common_words.append(word)

    return common_words

if __name__ == "__main__":
    assert is_palindrome("Madam") == True
    assert count_vowels("Hello") == 2
    assert word_frequency("apple apple mango") == {
        "apple": 2,
        "mango": 1
    }
    assert most_common_word("cat dog cat") == ["cat"]

    print("All self-tests passed!")