def solution(number, limit, power):
    divisor_count = [0] * (number + 1)
    
    for d in range(1, number + 1):
        for multiple in range(d, number + 1, d):
            divisor_count[multiple] += 1
    
    answer = 0
    for n in range(1, number + 1):
        if divisor_count[n] > limit:
            answer += power
        else:
            answer += divisor_count[n]
    
    return answer