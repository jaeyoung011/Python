

num_eng_dict = {'zero' : '0', 'one':'1', 'two':'2',  'three':'3', 'four':'4', 'five':'5', 'six':'6',
                'seven':'7','eight':'8','nine':'9'}

inv_map = {v: k for k, v in num_eng_dict.items()}

def num_change(s): # My_solution

    s = list(s)

    for i in range(len(s)):
        if s[i].isnumeric():
            s[i] = inv_map[s[i]]

    temp = ''.join(s)

    result_temp = []
    result = []
    j = 0
    for i in range(len(temp)+1):
        if temp[j:i] in num_eng_dict.keys():
            result_temp.append(temp[:i])
            j = i

    for i in range(len(result_temp)):
        if i == 0:
            result.append(result_temp[i])
        else:
            result.append(result_temp[i][len(result_temp[i-1]):])

    num_result = []
    for i in result:
        num_result.append(num_eng_dict[i])

    answer = int(''.join(num_result))

    return answer

print(num_change("one4seveneight"))



# 다른 사람 풀이 참조 from 프로그래머스

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

def solution(s):
    nums = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    for key, value in nums.items():
        s = s.replace(key,value)

    return int(s)
