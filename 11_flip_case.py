def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ''
    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            if to_swap.lower() == to_swap:
                result += (ltr.lower() if ltr != to_swap else ltr.upper())
            else:
                result += (ltr.upper() if ltr != to_swap else ltr.lower())
        else:
            result += ltr
    return result