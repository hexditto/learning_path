"""
Exercise
Create a function that finds the first duplicate,
considering the second number of the duplication.
Return the named duplication.

Requisites:
    The order of the duplicated number is considered from
    the second ocurrence of the number, in other words, the 
    duplicated number itself.
Example:
    [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 are duplicates (return 3)
    [1, 2, 3, 4, 5, 6] -> Return -1 (there arent duplicates)
    [1, 4, 9, 8, ->9<-, 4, 8] (return 9)
    If a duplicate is not found, return -1
"""

integer_list_number = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 19, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

def find_first_duplicate(list_integers):
    check_numbers = set()
    first_duplicate = -1

    for number in list_integers:
        if number in check_numbers:
            first_duplicate = number
            break

        check_numbers.add(number)
    return first_duplicate


for array in integer_list_number:
    print(
        array,
        find_first_duplicate(array)
    )