__author__ = 'lee'
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        point_set = set()
        point_sum = 0
        min_x = rectangles[0][0]
        max_x = rectangles[0][2]
        min_y = rectangles[0][1]
        max_y = rectangles[0][3]

        for list in rectangles:
            points = self.getAllPointList((list[0], list[1]), (list[2], list[3]))
            point_sum += points.__len__()
            point_set.update(points)
            if point_set.__len__() != point_sum:
                return False
            min_x = min(min_x, list[0])
            min_y = min(min_y, list[1])
            max_x = max(max_x, list[2])
            max_y = max(max_y, list[3])

        if (max_x - min_x) * (max_y - min_y) == point_sum:
            return True

        return False


    def getAllPointList(self, blp, trp):
        points = []
        for x in range(blp[0], trp[0]):
            for y in range(blp[1], trp[1]):
                points.append((x, y))

        return points

if __name__ == '__main__':
    sol = Solution()
    print sol.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])