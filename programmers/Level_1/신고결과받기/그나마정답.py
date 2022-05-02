
# 프로그래머스에서 가져옴

def solution(id_list, report, k):
    ids = []
    reports = []
    for message in set(report):
        ids.append(message.split(" ")[0])
        reports.append(message.split(" ")[1])

    set_report = set(reports)

    restrained = counting_report(set_report, reports, k)

    messaged = counting_message(restrained, ids, reports, id_list)

    answer=[]
    for ID in id_list:
        answer.append(messaged[ID])

    return answer

def counting_report(set_report, reports, k):
    result = []
    for reported in set_report:
        if reports.count(reported)>=k:
            result.append(reported)

    return result

def counting_message(restrained, ids, reports, id_list):
    result = {}
    for ID in id_list:
        result[ID] =0
    for res in restrained:
        for ID, reported in zip(ids, reports):
            if reported == res:
                result[ID]+=1
    return result


# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3 ))

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
