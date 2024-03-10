import math
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()

    a=[]
    b=[]
    for i in range(len(str1)-1):
        if (str1[i:i+2]).isalpha():
            a.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if (str2[i:i+2]).isalpha():
            b.append(str2[i:i+2])

    gyo=0 #다중집합에서 교집합을 구하는 방법
    b1=b.copy()
    for i in a:
        if i in b1:
            gyo+=1
            b1.remove(i)
            
    hap=[] #다중집합에서 합집합을 구하는 방법
    a1=a.copy() 
    for i in b:
        hap.append(i)
        if i in a1:
            a1.remove(i)
    hap=a1+hap
    
    if gyo==0 and len(hap)==0:
        return 65536
    else: return math.floor(gyo/len(hap)*65536)