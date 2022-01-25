def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    word_list = list(phrase)
    word_list.reverse()

    print(''.join(word_list))