text = input("Enter a text to check: ")  # e.x.: Hello World, my name is Mars and I own a racecar..
palindromes = 0


def is_palindrome(word):
    return len(word) > 1 and word[::-1] == word


for word in text.split():
    word = word.replace(',', '') \
               .replace('.', '')

    if is_palindrome(word):
        palindromes += 1

print('Palindromes found: ' + str(palindromes))
