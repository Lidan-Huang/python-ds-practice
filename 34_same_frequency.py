def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    lst1 = list(str(num1))
    lst1.sort()
    lst2 = list(str(num2))
    lst2.sort()

    return ''.join(lst1) == ''.join(lst2)

    # in Python, dictionaries with the same key-value pairs are equal