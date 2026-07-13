def solution(price, money, count):
    sum = 0
    sum = (count + 1) * (price * count) // 2
    
    if (sum >= money): answer = sum - money
    else:
        answer = 0

    return answer