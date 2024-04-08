def solution(skill, skill_trees):
    # 투 포인터로 해결합니다.
    skillset = set(skill)
    answer = 0
    
    for skill_tree in skill_trees:
        i, j = 0, 0
        valid = True
        while i < len(skill) and j < len(skill_tree):
            # 스킬트리 상의 스킬이 skillset에 포함되어 있지만, 
            # 현재 배워야 하는 skill[i]가 아닌 경우는 불가능한 스킬트리입니다.
            if skill_tree[j] in skillset:
                if skill_tree[j] != skill[i]:
                    valid = False
                    break
                else:
                    # 배워야 하는 스킬이 맞다면, i, j를 하나씩 증가시킵니다.
                    i += 1
                    j += 1
            # 제약조건이 없는 스킬이라면, 그냥 j만 증가시킵니다.
            else:
                j += 1
                
        if valid:
            answer += 1

    return answer