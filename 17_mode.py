def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    unique = set(nums)
    count = 0
    common_num = 0
    
    for num in unique:
        if nums.count(num) > count:
            count = nums.count(num)
            common_num = num
    return common_num