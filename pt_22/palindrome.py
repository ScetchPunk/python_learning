def palindrome(str_for_check):
    word = str_for_check.lower()
    return word[::-1] == word
print (palindrome("мама"))
print (palindrome("мам"))