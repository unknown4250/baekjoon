from collections import deque

def solution(cacheSize, cities):
    answer = 0
    n = len(cities)

    # LRU 교체 알고리즘이므로 데크를 활용
    cache = deque()
    
    # 캐시 크기가 0이면 cache miss만 발생
    if cacheSize == 0:
        return 5 * n

    for i in range(n):
        # 대소문자 구분하지 않으므로 소문자로 저장
        city = cities[i].lower()

        # cache hit인 경우
        if city in cache:
            # 실행시간 증가
            answer += 1
            
            # cache hit이 발생하면 이전의 값은 지우고 새로 업데이트 해야 함
            cache.remove(city)
            cache.append(city)

        # cache miss이거나 캐시에 여유 공간 있는 경우
        elif city not in cache or len(cache) < cacheSize:
            # 실행시간 증가
            answer += 5

            # cache miss인 경우
            if len(cache) == cacheSize:
                # 캐시에서 가장 오래된 도시 제거
                cache.popleft()
            
            # 캐시에 새로 추가
            cache.append(city)

                
    return answer
