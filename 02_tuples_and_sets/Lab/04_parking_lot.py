lines = int(input())
parking = set()
for i in range(lines):
    command = input().split(', ')
    cmd = command[0]
    car = command[1]
    if cmd == 'IN':
        parking.add(car)
    elif cmd == 'OUT':
        parking.remove(car)
if parking:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')