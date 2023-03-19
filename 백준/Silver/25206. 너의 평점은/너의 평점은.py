a = []
b = []
for i in range(20):
    Grades = list(map(str,input().split()))
    if Grades[2] == 'A+':
        Grades[2] = 4.5
    elif Grades[2] == 'A0':
        Grades[2] = 4.0
    elif Grades[2] == 'B+':
        Grades[2] = 3.5
    elif Grades[2] == 'B0':
        Grades[2] = 3.0
    elif Grades[2] == 'C+':
        Grades[2] = 2.5
    elif Grades[2] == 'C0':
        Grades[2] = 2.0
    elif Grades[2] == 'D+':
        Grades[2] = 1.5
    elif Grades[2] == 'D0':
        Grades[2] = 1.0
    elif Grades[2] == 'F':
        Grades[2] = 0
    
    try:
        a.append(int(float(Grades[1]))* float(Grades[2]))
        b.append(int(float(Grades[1])))
    except:
        pass
print(sum(a)/sum(b))