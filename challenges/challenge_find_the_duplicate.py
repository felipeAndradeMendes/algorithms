def find_duplicate(nums):
    has_string = any(type(num) == str for num in nums)
    if has_string:
        return False

    has_negative = any(num < 0 for num in nums)
    is_empty = len(nums) == 0
    has_single_num = len(nums) == 1

    if has_negative or is_empty or has_single_num:
        return False

    #    nums_sorted = sorted(nums)
    #     current_num = sorted[0]

    num_organizer = []
    for num in nums:
        if num in num_organizer:
            return num
        num_organizer.append(num)

    return False

    # raise NotImplementedError


# nums = [1, 3, 4, 3, -2]
# nums = ['a', 'b']
# print(find_duplicate(nums))
