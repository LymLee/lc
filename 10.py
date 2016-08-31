__author__ = 'lee'

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        que = [(s, p)]
        while que.__len__() > 0:
            e = que.pop(0)
            es = e[0]
            ep = e[1]
            es_len = es.__len__()
            ep_len = ep.__len__()

            if es_len == 0:
                if ep_len ==  0:
                    return True
                elif ep[ep_len-1] == '*':
                    que.append((es, ep[0:ep_len-2]))
                else:
                    continue
            elif ep_len == 0:
                continue
            elif ep[-1] == '*':
                if ep_len > 3 and ep[-3] == '*' and (ep[-2] == ep[-4] or ep[-4] == '.'):
                    que.append((es, ep[:-2]))
                elif self.isCharMatch(es[-1], ep[-2]):
                    que.append((es, ep[:-2]))
                    que.append((es[:-1], ep))
                    que.append((es[:-1], ep[:-2]))
                else:
                    que.append((es, ep[:-2]))
            elif self.isCharMatch(es[-1], ep[-1]):
                que.append((es[:-1], ep[:-1]))

        return False

    def isCharMatch(self, c1, c2):
        if c1 == '.' or c2 == '.' or c1 == c2:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch("aa","a")
    print sol.isMatch("aa","aa")
    print sol.isMatch("aaa","aa")
    print sol.isMatch("aa", "a*")
    print sol.isMatch("aa", ".*")
    print sol.isMatch("ab", ".*")
    print sol.isMatch("aab", "c*a*b")
    print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")
    print sol.isMatch("aaaabcbcbccccbac", "bc*c*a*.*a*a*c*.*c*")