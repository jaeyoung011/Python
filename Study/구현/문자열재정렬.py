

def get_alph_num(order_list):
    number_list = []
    char_list = []
    big_letters = map(chr, range(ord('A'), ord('Z')+1))
    bit_letters = list(big_letters)

    for i in order_list:
        if i in str([1,2,3,4,5,6,7,8,9]):
            number_list.append(i)
        elif i in bit_letters:
            char_list.append(i)

    char_list = sorted(char_list)
    number_list = map(int, number_list)
    number_list = list(number_list)
    sum_number = str(sum(number_list))
    char_str = ''.join(char_list)
    get_order = char_str + sum_number

    return get_order

print(get_alph_num('K1KA5CB7'))


# 답안 예시

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))
