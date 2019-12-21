class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        l = 0
        r = len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            print(l, r)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return area

    def maxArea_2(self, height):
        def area(ind1, ind2):
            return abs(ind1 - ind2) * min(height[ind1], height[ind2])

        i, j = 0, len(height) - 1
        max_area = 0
        while i != j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            max_area = max(area(i,j), max_area)
        return max_area
height = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(height))