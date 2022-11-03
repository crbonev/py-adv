def sum_of_negative(num):
    result = sum([x for x in num if x < 0])
    return result


def sum_of_positive(num):
    result = sum([x for x in num if x > 0])
    return result


def check_numbers(negative, positive):
    if abs(negative) > abs(positive):
        return f'The negatives are stronger than the positives'
    else:
        return f'The positives are stronger than the negatives'


numbers = list(map(int, input().split()))


print(sum_of_negative(numbers))
print(sum_of_positive(numbers))
print(check_numbers(sum_of_negative(numbers), sum_of_positive(numbers)))

"""
1 2 -3 -4 65 -98 12 57 -84
"""