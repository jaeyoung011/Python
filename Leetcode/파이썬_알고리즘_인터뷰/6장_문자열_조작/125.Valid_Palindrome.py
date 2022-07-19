
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True



if __name__ == '__main__':
    Solution = Solution() # 클래스를 먼저 선어을 해주어야한다. 선언이 없을시 사용이 불가능하다.
    s = "A man, a plan, a canal: Panama"
    print(Solution.isPalindrome(s))