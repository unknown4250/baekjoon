n, m = map(int, input().split())

st = []

def back_tracking():
    if len(st) == m:
        print(' '.join(map(str, st)))
        return
    
    for i in range(1, n + 1):
        if i in st:
            continue
        st.append(i)
        back_tracking()
        st.pop()

back_tracking()