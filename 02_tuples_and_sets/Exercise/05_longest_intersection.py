lines = int(input())
longest_intersection = set()

for _ in range(lines):
    first_range, second_range = input().split('-')

    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    current = first.intersection(second)
    if len(current) > len(longest_intersection):
        longest_intersection = current

print(f'Longest intersection is {[el for el in longest_intersection]} with length {len(longest_intersection)}')
