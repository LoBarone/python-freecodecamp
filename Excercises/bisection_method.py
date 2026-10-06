def square_root_bisection(number, tolerance=0.1, max_iterations=50):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    top = max(1.0, number)
    low = 0
    for _ in range(max_iterations):
        mid = (low + top) / 2
        if abs(top - low) <= tolerance:
            print(f'The square root of {number} is approximately {mid}')
            return mid
        elif mid ** 2 > number:
            top = mid
        else:
            low = mid
    print (f'Failed to converge within {max_iterations} iterations')
    return None
