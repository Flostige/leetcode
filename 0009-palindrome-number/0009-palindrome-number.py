class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        temp = 0
        while x > temp:
            temp = temp * 10 + x % 10
            x //= 10
        
        return temp == x or temp // 10 == x