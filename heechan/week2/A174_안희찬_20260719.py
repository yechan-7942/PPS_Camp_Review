import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for s in score:
        if len(heap) < k:
            heapq.heappush(heap, s)
        elif s > heap[0]:
            heapq.heapreplace(heap, s)
        
        answer.append(heap[0])
    
    return answer