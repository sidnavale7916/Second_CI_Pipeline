
def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))
    return non_zeros + zeros
