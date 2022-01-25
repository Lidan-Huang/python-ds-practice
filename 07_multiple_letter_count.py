def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    key_to_value = {} 
    for letter in phrase:
        if letter not in key_to_value.keys():
            key_to_value[letter] = 1
        else:
            key_to_value[letter] += 1
    return key_to_value

    # .get()
    # dictionary comprehension