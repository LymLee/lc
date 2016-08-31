__author__ = 'lee'
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def addCorner(x, y):
            if (x, y) in dict:
                dict[(x, y)] += 1
            else:
                dict[(x, y)] = 1

        dict = {}
        min_x = rectangles[0][0]
        max_x = rectangles[0][2]
        min_y = rectangles[0][1]
        max_y = rectangles[0][3]
        area_sum = 0

        for list in rectangles:
            addCorner(list[0], list[1])
            addCorner(list[2], list[1])
            addCorner(list[0], list[3])
            addCorner(list[2], list[3])

            area_sum += (list[3] - list[1]) * (list[2] - list[0])

            min_x = min(min_x, list[0])
            min_y = min(min_y, list[1])
            max_x = max(max_x, list[2])
            max_y = max(max_y, list[3])

        if (max_x - min_x) * (max_y - min_y) != area_sum:
            return False

        if ((min_x, min_y) in dict) and ((min_x, max_y) in dict) and ((max_x, min_y) in dict) and ((max_x, max_y) in dict):
            if (dict[(min_x, min_y)] != 1) or (dict[(min_x, max_y)] != 1) or (dict[(max_x, min_y)] != 1) or (dict[(max_x, max_y)] != 1):
                return False
        else:
            return False

        del dict[(min_x, min_y)]
        del dict[(min_x, max_y)]
        del dict[(max_x, min_y)]
        del dict[(max_x, max_y)]

        for p in dict:
            if dict[p] != 2 and dict[p] != 4:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print sol.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])
    #print sol.isRectangleCover([[0,0,1,1],[0,0,1,1],[1,1,2,2],[1,1,2,2]])