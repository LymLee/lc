__author__ = 'lee'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        count = 1
        for i in nums:
            sum += (count - i)
            count += 1

        return sum


if __name__ == '__main__':
    sol = Solution()
    print '[1, 2, 3, 4, 5] = ', sol.missingNumber([1, 2, 3, 4, 5])
    print '[0, 1, 2, 3, 5] = ', sol.missingNumber([0, 1, 2, 3, 5])
    print '[0, 1, 3, 4, 5] = ', sol.missingNumber([0, 1, 3, 4, 5])
    print '[0, 1, 3, 4, 5, 6] = ', sol.missingNumber([0, 1, 3, 4, 5, 6])
    print '[0, 1, 2, 3, 4] = ', sol.missingNumber([0, 1, 2, 3, 4])