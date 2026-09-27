def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]
    return (range_of_numbers(start_num, end_num - 1)) + [end_num]
