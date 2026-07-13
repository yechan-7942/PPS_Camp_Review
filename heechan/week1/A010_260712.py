def compress(s, unit):
    tokens = [s[i:i+unit] for i in range(0, len(s), unit)]

    result = 0
    prev = tokens[0]
    count = 1

    for cur in tokens[1:]:
        if cur == prev:
            count += 1
        else:
            result += len(prev) + (len(str(count)) if count > 1 else 0)
            prev = cur
            count = 1

    result += len(prev) + (len(str(count)) if count > 1 else 0)
    return result


def solution(s):
    return min(compress(s, unit) for unit in range(1, len(s) // 2 + 1)) if len(s) > 1 else 1