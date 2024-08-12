n = 1260
coin_type = [500, 100, 50, 10]

count = 0

for coin in coin_type: # 총 4번의 for문 순회
    count += n // coin  # 1260을 500, 100, 50, 10 순서로 나눔
    n %= coin 
    # 1260을 500으로 나눈 나머지 값으로 업데이트하여 n을 1260원에서 260원으로 업데이트. 
    # 2번째 for문을 순회하면, 
    # 260원을 200원으로 나누어 n을 60원으로 업데이트 
    # 60원을 50원으로 나누어 n을 10원으로 업데이트
    # 10원을 10원으로 나누어 업데이트 종료
print(count)


# 함수 만들기
def min_coin(n, coin_type):
    count = 0
    for coin in coin_type:
        count += n // coin
        n %= coin
    return count
coin_type = [500, 100, 50, 10]

print(min_coin(1260, coin_type))