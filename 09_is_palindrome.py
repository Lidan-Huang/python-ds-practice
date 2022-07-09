def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    if len(phrase) <= 1:
        return True

    phrase = phrase.lower()
    if ' ' in phrase:
        # phrase = "".join(phrase.split(" "))
        phrase = phrase.replace(" ", "")
    
    # phrase_list = list(phrase)

    # while len(phrase_list) > 1:
    #     if phrase_list.pop(0) != phrase_list.pop():
    #         return False
    
    # return True

    # .replace() to remove the space
    reversed = phrase[::-1]
    return reversed == phrase