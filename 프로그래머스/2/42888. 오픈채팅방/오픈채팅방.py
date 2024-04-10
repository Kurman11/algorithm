def solution(record):
    answer = []
    id_dict = dict()  # id에 해당하는 이름 정보
    commands = [list(r.split()) for r in record]  # record의 데이터들을 공백 기준으로 분리

    for command in commands:
        if command[0] == 'Enter' or command[0] == 'Change':  # id에 해당하는 닉네임 정보 생성 혹은 업데이트
            id_dict[command[1]] = command[2]

    for command in commands:
        if command[0] == 'Enter':
            answer.append(id_dict[command[1]] + "님이 들어왔습니다.")
        elif command[0] == 'Leave':
            answer.append(id_dict[command[1]] + "님이 나갔습니다.")
    return answer