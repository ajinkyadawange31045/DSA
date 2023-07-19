# class Solution(object):
#     def singleNumber(self, nums):
#         ones = 0
#         twos = 0

#         for num in nums:
#             ones = (ones ^ num) & ~twos
#             twos = (twos ^ num) & ~ones

#         return ones

class Solution:
    def singleNumber(self, nums):
        
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                temp = n >> i
                temp = temp & 1
                count += temp
            rem = count % 3
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i
        return res