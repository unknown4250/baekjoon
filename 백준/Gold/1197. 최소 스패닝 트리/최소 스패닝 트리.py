"""
Kruskal 알고리즘
1. root(=부모노드)를 저장하는 v_root 배열을 생성한다. 
(여기서 root는 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장)
2. 간선들(e_list)을 가중치 기준으로 정렬한다.
3. 간선들이 이은 두 정점을 find함수를 통해 두 root(s_root, e_root)를 찾는다.
4. 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
5. 가중치를 더한다.
"""

import sys
read = sys.stdin.readline

v, e = map(int, read().split())
v_root = [i for i in range(v+1)]

e_list = []
for _ in range(e):
    e_list.append(list(map(int, read().split())))

e_list.sort(key=lambda x: x[2]) # x[2]: 각 간선의 가중치


def find(x):
    if x != v_root[x]:
        v_root[x] = find(v_root[x])
    return v_root[x]


answer = 0
for s, e, w in e_list:
    s_root = find(s)
    e_root = find(e)

    # union 연산
    # 두 노드의 부모 노드가 서로 다르다면 => 사이클이 발생하지 않는다면 mst에 포함
    if s_root != e_root:
        # 번호가 작은 노드를 부모 노드로 변경
        if s_root > e_root:
            v_root[s_root] = e_root
        else:
            v_root[e_root] = s_root
        answer += w

print(answer)