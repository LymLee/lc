__author__ = 'lee'

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentances = s.split(' ')
        sentances.reverse()

        res = ''
        for sen in sentances:
            if sen != '':
                res += sen
                res += ' '

        return res[:-1]


if __name__ == '__main__':
    sol = Solution()

    print sol.reverseWords('this is a word')
    print sol.reverseWords('  ')