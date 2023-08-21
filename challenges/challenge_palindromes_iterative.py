def is_palindrome_iterative(word):
    if not word:
        return False

    word_to_lower = word.lower()
    reversed_word = word_to_lower[::-1]

    if word_to_lower == reversed_word:
        return True

    return False
