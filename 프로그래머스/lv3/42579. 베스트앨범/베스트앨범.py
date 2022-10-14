def solution(genres, plays):

    ## 1. 가장 많이 재생된 장르
    ## 2. 장르별 가장 많이 재생된 곡

    answer = []
    total = {} # 장르별 총 재생 횟수
    genres_plays = {} # 동일한 장르의 곡별 재생 횟수

    for i in range(len(genres)):
        # 장르가 같으면 재생횟수 누적
        # total.get(genres[i], 0): 해시에 장르가 없으면 0으로 초기화
        total[genres[i]] = total.get(genres[i], 0) + plays[i]

        # 각 장르에 속하는 곡의 고유번호, 재생횟수 추가
        if genres[i] in genres_plays:
            genres_plays[genres[i]].append((i, plays[i]))
        else:
            genres_plays[genres[i]] = [(i, plays[i])]
    
    # 총 재생횟수를 기준으로 장르 순위 결정
    genre_rank = sorted(total, key=total.get, reverse=True)


    for rank in genre_rank:
        # 재생횟수(내림차순), 고유번호(오름차순) 기준으로 정렬
        play_rank = sorted(genres_plays[rank], key=lambda x:(-x[1], x[0]))
        print(play_rank)

        # 장르별 2곡 선택, 단 장르에 1곡만 있다면 1곡만 선택
        if len(play_rank) == 1:
            answer.append(play_rank[0][0])
        else:
            answer.append(play_rank[0][0])
            answer.append(play_rank[1][0])

    return answer
    