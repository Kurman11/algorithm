from math import ceil

def time2price(t, defaulttime, defaultprice, unittime, unitprice):
    # 기본시간 이하이면 기본요금 청구
    if t <= defaulttime:
        return defaultprice
    # 초과한 시간에 대해서 단위 시간마다 단위 요금을 청구
    excesstime_unit = ceil( (t - defaulttime) / unittime )
    return defaultprice + excesstime_unit * unitprice

def h2m(t):
    # 시간 문자열을 분 단위 정수 값으로 바꿉니다.
    return 60 * int(t.split(':')[0]) + int(t.split(':')[1])

def solution(fees, records):
    # 주차장에 들어와있는 차들의 상태를 관리하는 state 딕셔너리를 만듭니다.
    # 각 차별로 누적 시간을 나타내는 car2time 딕셔너리를 만듭니다.
    state, car2time = {}, {}
    
    for record in records:
        time, car, type = record.split(); time = h2m(time)
        if type == 'IN':
            # 입차 시간을 기록합니다.
            state[car] = time
        else:
            # 현재 해당 차의 누적 주차 시간에
            # 입차 시간과 출차 시간의 차이를 더해줍니다.
            car2time[car] = car2time.get(car, 0) + (time - state[car])
            state.pop(car)
            
    # 아직 주차되어 있는 차는 23:59에 출차된 것으로 간주합니다
    for car, time in state.items():
        car2time[car] = car2time.get(car, 0) + (h2m('23:59') - time)
    
    car2price = {car:time2price(time, *fees) for car, time in car2time.items()}
    
    answer = [car2price[car] for car in sorted(car2price.keys())]
    return answer