def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # second_idx = None

    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == goal:
    #             if second_idx is None or j <= second_idx:
    #                 second_idx = j
    #                 break
                
    # return ((goal - nums[second_idx]), nums[second_idx]) if second_idx else ()

    visited = set()

    for num in nums:
        diff = goal - num
        if diff in visited:
            return (diff, num)
        visited.add(num)

    return ()