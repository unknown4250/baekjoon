h, m = map(int, input().split(' '))

if m >= 45:
    m -= 45
elif m < 45 and h >= 1:
    m = m + 60 - 45
    h -= 1
else:
    m = m + 60 - 45
    h = 23

print("%d %d" % (h, m))