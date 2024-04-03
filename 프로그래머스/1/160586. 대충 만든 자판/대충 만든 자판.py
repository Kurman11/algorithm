from collections import defaultdict
def solution(keymap, targets):
    answer = []
    
    dict = defaultdict(str)
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            ch = keymap[i][j]
            if ch not in dict:
                dict[ch] = j+1
            else:
                dict[ch] = min(dict[ch], j+1)
    
    for target in targets:
        sum = 0
        for t in target:
            if t in dict:
                sum += dict.get(t)
            else:
                sum = -1
                break
        
        answer.append(sum)
    
    return answer
# def solution(keymap, targets):
#     result = []
#     for i in range(len(targets)):
#         for a in range(len(keymap)):
#             b = []
#             result.append(b)
#             for j in targets[i]:
#                 cnt1 = 1
#                 cnt2 = 1
#                 for k in keymap[a]:
#                     if j == k:
#                         b.append(cnt1)
#                         break
#                     else:
#                         cnt1 += 1
#                         if cnt1 > len(keymap[a]):
#                             b.append(0)
                
                
#     for i in range(len(targets)):
#         for j in range(len(targets)):
#             for a in result[i]:
                
        
        
#     answer = []
#     return answer