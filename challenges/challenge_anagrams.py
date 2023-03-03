def join_sort(arr_word):

    if len(arr_word) <= 1:
        return arr_word

    middle = len(arr_word) // 2

    left = join_sort(arr_word[:middle])
    right = join_sort(arr_word[middle:])

    return join_merge(left, right)


def join_merge(left, right):

    arr = []
    counterA = 0
    counterB = 0

    while counterA < len(left) and counterB < len(right):

        if left[counterA] < right[counterB]:
            arr.append(left[counterA])
            counterA += 1
        else:
            arr.append(right[counterB])
            counterB += 1

    arr += left[counterA:]
    arr += right[counterB:]

    return "".join(arr)

def is_anagram(first_string, second_string):

    first_Lower = first_string.lower()
    second_Lower = second_string.lower()

    first = join_sort(first_Lower)
    second = join_sort(second_Lower)

    isTrue = (first != "" and second != "" and first == second)

    return (first, second, isTrue)
