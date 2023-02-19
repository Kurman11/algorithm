word = input()
word_dict = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}
stack = []
for i in word: 
    if i == '(':  # i 값에 (이 들어오면
        stack.append(i) # 스택에 ( append
    elif i == ')': # i 값에 )이 들어오면
        check = 0 # check = 0 이면서 while문 동작

        while 1:
            target = stack.pop() # 스택에 있는 제일 마지막 을 pop하고 그 값을 target에 저장
            if target == '(': # stact의 제일 마지막이 ( 이라면
                break # while문 종료
            check += target # check에 target값을 더해준다
        stack.append(check) # stack에 더한 check값을 append한다

    elif i in word_dict: # 해당 문자가 dict에 들어있다면
        stack.append(word_dict[i]) # 해당 딕셔너리의 value값을 stack로 append
    else:
        stack[-1] *= int(i) # 만약 숫자가 들어온다면 스택의 가장 마지막 수와 숫자와 곱해준다
print(sum(stack)) # 스택에 저장된 숫자를 다 더해준다