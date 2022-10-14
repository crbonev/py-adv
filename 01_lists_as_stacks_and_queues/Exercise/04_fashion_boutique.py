clothes = list(map(int, input().split()))
capacity = int(input())
racks = 0
current_clothes = 0

while clothes:
    while current_clothes <= capacity:
        index = len(clothes) - 1
        current_clothes += clothes[index]

        if current_clothes <= capacity:
            clothes.pop()
            if index == 0:
                racks += 1
                break
            if current_clothes == capacity:
                racks += 1
                current_clothes = 0

        else:
            current_clothes = 0
            racks += 1
            if index == 0:
                racks += 1
                clothes.pop()
                break

print(racks)