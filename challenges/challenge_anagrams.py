def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return first_string, second_string, False

    first_split = [caracter.lower() for caracter in list(first_string)]
    second_split = [caracter.lower() for caracter in list(second_string)]

    merge_sort(first_split, 0, len(first_split))
    merge_sort(second_split, 0, len(second_split))

    first_sort = first_split
    second_sort = second_split

    first_joined = "".join(first_sort)
    second_joined = "".join(second_sort)

    if first_joined == second_joined:
        return first_joined, second_joined, True
    else:
        return first_joined, second_joined, False


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0
    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
