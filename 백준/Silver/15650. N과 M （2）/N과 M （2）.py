n, m = map(int, input().split())

st = []

def back_tracking(start):
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(start, n + 1):
        if i in st:
            continue
        st.append(i)
        back_tracking(i + 1)
        st.pop()

back_tracking(1)