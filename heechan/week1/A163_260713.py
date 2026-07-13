def to_days(date):
    y, m, d = map(int, date.split('.'))
    return (y * 12 + m) * 28 + d

def solution(today, terms, privacies):
    term_map = {}
    for t in terms:
        name, month = t.split()
        term_map[name] = int(month)

    today_d = to_days(today)
    answer = []

    for i, p in enumerate(privacies, start=1):
        date, name = p.split()
        if today_d >= to_days(date) + term_map[name] * 28:
            answer.append(i)

    return answer