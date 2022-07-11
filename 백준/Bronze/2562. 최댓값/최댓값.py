dict = {}

for i in range(9):
    dict[int(input())] = i + 1

max_num = max(dict)

print(max_num)
print(dict[max_num])