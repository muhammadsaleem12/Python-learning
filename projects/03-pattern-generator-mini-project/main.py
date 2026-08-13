# this is simple pattern generator mini project using pyhton.

def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."

    pattern_list = []

    for i in range(1, n + 1):
        pattern_list.append(str(i))

            
    return " ".join(pattern_list)

print(number_pattern(12))

# the program should return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)