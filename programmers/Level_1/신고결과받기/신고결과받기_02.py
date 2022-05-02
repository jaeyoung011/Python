# https://programmers.co.kr/learn/courses/30/lessons/92334
# 프로그래머스_level1_ testcase2 번만 맞는다...

from collections import Counter


def report_result(id_list, report, k):
    # [['muzi', 'frodo'], ['','']]기 담아주
    report_list = []
    for person in report:
        report_list.append(person.split(' '))
    # 중복 제거해주는 코드 추가
    report_tuple = [tuple(i) for i in report_list] # 바로 set 을 하면 unhashable 에러
    set_report = set(report_tuple) # 중복제거
    report_to_list = list(set_report)

    # accuser , accused 따로 담아주기
    accuser = []
    accused = []
    for i,name_to_list in enumerate(report_to_list):
        accuser.append(name_to_list[0])
        accused.append(name_to_list[1])

    # k 이상인 애들만 뽑아내기
    accused_period = []
    for count_sus in accused:
        if accused.count(count_sus) > k:
            accused_period.append(count_sus)
    accused_period = set(accused_period) # 중복제거
    accused_period = list(accused_period)



    # accused_period = Counter(accused).most_common(k) # 하나만 있으면 k가 3이라도 나타나게된다..

    # k 번이상 신고당한 사람들
    suspect_done = []
    for i in range(len(accused_period)):
        suspect_done.append(accused_period[i][0])

    # 이 결과를 email로 알려주기

    # accused 에 'neo' or 'frodo' 없는 인덱스 제거

    check_idx = []
    for idx, name in enumerate(accused): # idx
        if name in check_idx:
            pass
        else:
            check_idx.append(idx)

    # check_name = []
    # for idx, name in enumerate(accused):
    #     if name in check_name:
    #         pass
    #     else:
    #         check_name.append(name)

    # 제거 : 그런데 pop 을하면 하나씩 없어지기때문에 index가 맞지가 않는다...
    for del_idx in check_idx:
        accuser.pop(del_idx)
        accused.pop(del_idx)

    ## 이름으로
    # for del_name in check_name:
    #     accuser.pop(del_name)
    #     accused.pop(del_name)



    send_email = []
    for id in id_list:
        count = 0
        for ac in accuser:
            if id == ac:
                count += 1
        send_email.append(count)
    return send_email


# print(report_result(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

print(report_result(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3 ))