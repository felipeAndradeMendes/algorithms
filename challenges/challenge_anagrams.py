def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return first_string, second_string, False

    first_split = [caracter.lower() for caracter in list(first_string)]
    second_split = [caracter.lower() for caracter in list(second_string)]

    # print(first_split)
    # print(second_split)

    merge_sort(first_split, 0, len(first_split))
    merge_sort(second_split, 0, len(second_split))

    first_sort = first_split
    second_sort = second_split

    # print("FIRST SORT:", first_sort)
    # print("SECOND SORT:", second_sort)

    first_joined = "".join(first_sort)
    second_joined = "".join(second_sort)

    if first_joined == second_joined:
        return first_joined, second_joined, True
    else:
        return first_joined, second_joined, False
    # raise NotImplementedError


def insertion_sort(numbers):
    n = len(numbers)  # Quantidade de elementos na lista

    for index in range(1, n):  # Começaremos a ordenar pelo segundo elemento
        key = numbers[
            index
        ]  # Pegamos o segundo elemento e o definimos como chave

        new_position = (
            index - 1
        )  # Tomamos a posição anterior para iniciar a comparação
        while (
            new_position >= 0 and numbers[new_position] > key
        ):  # Enquanto a chave for menor, remaneja o elemento para frente
            numbers[new_position + 1] = numbers[
                new_position
            ]  # Remaneja o elemento
            new_position = new_position - 1

        numbers[new_position + 1] = key  # Insere a chave na posição correta

    return numbers


def merge_sort(numbers, start=0, end=None):
    # print("ARRAY DE STRING:", numbers)
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    # print("NUMBER:", numbers)
    # print("START:", start)
    # print("MID:", mid)
    # print("END:", end)

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


print(is_anagram("amor", "roma"))
