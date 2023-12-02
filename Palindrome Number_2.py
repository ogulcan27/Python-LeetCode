#String'e dönüştürmeden yapılan çözüm
class Solution_2a():
    def isPalindrome(self, x):
        """
        type x: int
        """
        if x < 0:
            return False
        else:
            original_x = x
            reversed_x = 0
            while x > 0:
                reversed_x = reversed_x*10 + x % 10
                x = x//10
                
        return original_x == reversed_x
    
x = 233
result = Solution_2a()
print(result.isPalindrome(x))
