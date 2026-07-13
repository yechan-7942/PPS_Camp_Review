def solution(x):
    sum = 0
    temp = x
    while (x > 0):
        sum += x % 10
        x = x // 10
        
    return (temp % sum == 0)