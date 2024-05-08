import re

def solution(new_id):
    # 1단게. 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    
    # 3단계. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = re.sub(r'^\.|\.$', '', new_id)
    
    # 5단계. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    # 6단계. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
        
    return new_id