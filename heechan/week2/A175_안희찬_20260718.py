import re

def solution(babbling):
    answer = 0
    for word in babbling:
        tokens = re.findall(r'aya|ye|woo|ma', word)

        if ''.join(tokens) != word:
            continue

        if any(tokens[i] == tokens[i+1] for i in range(len(tokens) - 1)):
            continue
        
        answer += 1
    
    return answer