def get_even_squares(num_list: list[int]) -> list[int]:
    '''
    返回 num_list 中所有偶數的平方值列表。

    Args:
        num_list: 一個整數列表。

    Returns:
        一個列表，包含 num_list 中所有偶數的平方值。
    '''
    return [num ** 2 for num in num_list if num % 2 == 0]


def get_odd_cubes(num_list: list[int]) -> list[int]:
    '''
    返回 num_list 中所有奇數的 3 次方值列表。

    Args:
        num_list: 一個整數列表。

    Returns:
        一個列表，包含 num_list 中所有奇數的 3 次方值。
    '''
    return [num ** 3 for num in num_list if num % 2 != 0]


def get_sliced_list(num_list: list[int]) -> list[int]:
    '''
    返回 num_list 從第 5 個元素開始到最後一個元素(包含最後一個)的子列表。

    Args:
        num_list: 一個整數列表。

    Returns:
        一個列表，包含 num_list 從第 5 個元素開始到最後一個元素的子列表。
    '''
    return num_list[4:]


def format_numbers(numbers: list[int]) -> str:
    '''
    返回一個新列表，其中每個數字都被格式化為 8 個字元的寬度，並靠右對齊。

    Args:
        numbers: 一個數字列表。

    Returns:
        一個字符串，包含格式化後的數字列表，每個數字都被格式化為 8 個字元的寬度，並靠右對齊，以逗號分隔。
    '''
    formatted_numbers = [str(num).rjust(8) for num in numbers]
    return ', '.join(formatted_numbers)


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(format_numbers(get_even_squares(num_list)))
print(format_numbers(get_odd_cubes(num_list)))
print(format_numbers(get_sliced_list(num_list)))
