line = input().split('|')
sub_lists = []
for substring in line[::-1]:
    sub_lists.extend(substring.split())
print(*sub_lists)