number_of_guests = int(input())
regular = set()
vip = set()

for x in range(number_of_guests):
    guest = input()
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

while True:
    guest = input()
    if guest == 'END':
        break
    if guest in regular:
        regular.remove(guest)
    elif guest in vip:
        vip.remove(guest)

total = len(regular) + len(vip)
print(total)
for x in sorted(vip):
    print(x)
for x in sorted(regular):
    print(x)