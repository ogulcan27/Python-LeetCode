#String'e dönüştürerek yapılan çözüm
class Solution_2():
    def isPalindrome(self, x):
        """
        type x: int
        """
        if x < 0:
            return False
        else:
            reversed_x = int(str(x)[::-1])
        
        return reversed_x == x

x = 121 
result = Solution_2()
print(result.isPalindrome(x))
