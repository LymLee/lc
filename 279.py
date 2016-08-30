__author__ = 'lee'

class Solution(object):
    def numSquares(self, n):
        queue = [(n, 0, n)]

        while queue.__len__() > 0:
            val = queue.pop(0)

            if val[0] == 1 or val[0] == 4 or val[0] == 9:
                return val[1] + 1

            for i in range(val[2], 0, -1):
                i_sq = i * i
                if i_sq < val[0]:
                    queue.append((val[0] - i_sq, val[1] + 1, i))
                elif i_sq == val[0]:
                    return val[1] + 1




if __name__ == '__main__':
    sol = Solution()
    print '5 = ', sol.numSquares(5)
    print '55 = ', sol.numSquares(55)
    print '555 = ', sol.numSquares(555)
    print '7168 = ', sol.numSquares(7168)
    print '1 = ', sol.numSquares(5)