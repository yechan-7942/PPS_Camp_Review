def solution(skill, skill_trees):
    
    answer = 0
    
    for skill_tree in skill_trees:
        index = 0
        a = skill[index]
        for n in skill_tree:
            if (n in skill and n != a):
                break
                
            if (n == a):
                if (len(skill) - 1 != index):
                    index += 1
                    a = skill[index]
            
        
        else:
            answer += 1
            
        
        
    return answer