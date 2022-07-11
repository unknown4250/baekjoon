num1, num2, num3 = map(int, input().split())

if num1 == num2 and num2 == num3 and num3 == num1:
    print(10000 + num1 * 1000)

elif num1 != num2 and num2 != num3 and num3 != num1:
    max_num = max(num1, num2, num3)
    print(max_num * 100)

else:
    if num1 == num2:
        print(1000 + num1 * 100)
    elif num2 == num3:
        print(1000 + num2 * 100)
    else:
        print(1000 + num3 * 100)