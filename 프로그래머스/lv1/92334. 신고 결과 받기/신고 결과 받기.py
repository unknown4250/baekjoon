def solution(id_list, report, k):
    answer = []
    # 한 유저가 같은 유저를 여러번 신고해도 1회로 간주되므로 중복 제거
    report = set(report)

    # 각 유저들의 신고한 목록
    info = {id:[] for id in id_list}

    # 유저가 신고해서 정지당한 유저 수 저장
    cnt = {id:0 for id in id_list}

    # 유저들의 신고 내역 저장
    for r in report:
        # key: 신고 당한 유저, value: 신고한 유저
        info[r.split()[1]].append(r.split()[0])
    
    # 각 유저가 신고한 유저 중 정지된 유저 찾기
    for id in id_list:
        for key, val in info.items():
            # 신고한 유저가 신고 목록에 있으면서 k 이상이면, key(=id)는 정지된 유저
            if id in val and len(info[key]) >= k:
                cnt[id] += 1
        answer.append(cnt[id])

    return answer