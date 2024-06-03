def solution(book_time):

    time_rooms = []
    rooms = dict()

    for bt in book_time:
        start, end = bt
        start = int(start.split(':')[0])*60+int(start.split(':')[1])
        end = int(end.split(':')[0])*60+int(end.split(':')[1])    
        time_rooms.append((start, end))

    for time in time_rooms:
        start, end = time

        for t in range(start, end+10):
            if rooms.get(t) == None:
                rooms[t] = 1
            else:
                rooms[t] +=1

    
    return  max(rooms.values())