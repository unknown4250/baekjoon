from collections import defaultdict

def solution(tickets):
    answer = []

    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)
    
    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop())
        answer.append(start)

    dfs("ICN")
    return answer[::-1]
