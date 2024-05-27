def solution(id_list, report, k):
    rep_set = set(report)
    rep_lst = []

    id_stop_lst = {}
    
    for i in rep_set:
        rep_item = i.split()
        id_stop_lst[rep_item[1]] = id_stop_lst.get(rep_item[1], []) + [rep_item[0]]
    
    id_mail_cnt = {}
    for key in id_stop_lst:
        if len(id_stop_lst[key]) >= k:
            for man in id_stop_lst[key]:
                id_mail_cnt[man] = id_mail_cnt.get(man, 0) + 1
    answer = []
    for i in range(len(id_list)):
        answer.append(id_mail_cnt.get(id_list[i], 0))

    return answer