class Solution_1():
    def twoSum(self, nums, target):
        """
        type nums: List[int]
        type target: int
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in num_dict:
                return [num_dict[complement], i]
            else:
                num_dict[num] = i
                
        return None
    
nums = [2,7,11,15]
target = 9
result = Solution_1()
if result.twoSum(nums, target):
    print(f"İki sayının toplamı {target} hedefine ulaşmak için kullanılan sayıların indeksleri: {result.twoSum(nums, target)}")
else:
    print("Çözüm bulunamadı.")
