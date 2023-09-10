t = 0
h1,m1,s1 = map(int,input().split(":")) # 현재 시간
h2,m2,s2 = map(int,input().split(":")) # 임무 시작 시간
t += (h2 - h1)*3600 + (m2 - m1)*60 + s2 - s1
t %= 3600*24 # 음수일 경우 대비
print("%.2d:%.2d:%.2d" %(t//3600,t%3600//60,t%60))