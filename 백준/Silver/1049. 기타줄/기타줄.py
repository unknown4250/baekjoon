import sys

input = sys.stdin.readline

broken_strings, brands = map(int, input().split())
package_prices, piece_prices = [], []

# 각 브랜드의 패키지 및 낱개 가격 저장
for _ in range(brands):
    package, piece = map(int, input().split())

    package_prices.append(package)
    piece_prices.append(piece)

# 패키지와 낱개 가격 중 최소값만 저장하면 됨
min_package_price = min(package_prices)
min_piece_price = min(piece_prices)

# 패키지 가격이 낱개 6개 가격보다 적으면 패키지 위주로 구매
if min_package_price < min_piece_price * 6:
    
    # 모두 패키지로 구입
    if min_package_price < (broken_strings % 6) * min_piece_price:
        print((broken_strings // 6) * min_package_price + min_package_price)

    # 패키지 + 낱개
    else:
        print((broken_strings // 6) * min_package_price + (broken_strings % 6) * min_piece_price)

# 패키지 가격이 낱개 6개 가격보다 비싸면 낱개로만 구매
else:
    print(broken_strings * min_piece_price)
