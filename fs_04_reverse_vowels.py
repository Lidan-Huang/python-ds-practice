def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    letters = list(s)
    vowels = "aeiouAEIOU"
    left = 0
    right = len(letters) - 1

    while (left < right):
        while (left < right):
            if (letters[left] not in vowels):
                left += 1
                continue
            else:
                break
        while (left < right):
            if (letters[right] not in vowels):
                right -= 1
                continue
            else: 
                break
        letters[left], letters[right] = letters[right], letters[left]
        left += 1
        right -= 1
    return "".join(letters)
            