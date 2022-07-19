
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 2개의 키를 람다 표현식으로 정렬 : 이부분 labmda 식 표현이 이해가 가질 않는다.
        # letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        sorted(letters, key=lambda x: (x.split()[1:], x.split()[0])) # art own art 기준으로 하는데 같을시에는 let1, let2, let3 기준으로 한다

        return letters+digits # letters 후에 digits


if __name__ == '__main__':
    Solution = Solution()
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    result = Solution.reorderLogFiles(logs)

    print(result)


