numbers = tuple(input().split())
unique_numbers = []
output = {}
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(float(number))

for number in unique_numbers:
    number_count = numbers.count(number)
    output[number] = str(f'{number_count} times')

for key, value in output.items():
    print(f'{key} - {value}')