class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        t, r, minus = 0, 0, 1
        if x < 0:
            minus = -1
            x = x * -1
        while True:
            t = x % 10
            r = r * 10 + t
            x = x / 10
            if r > pow(2, 31):
                return 0
            if x == 0:
                break
        return minus * r

    def reverse(self, x):
        result = 0

        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        while x:
            result = result * 10 + x % 10
            x /= 10
        return 0 if result > pow(2, 31) else result * symbol

s = Solution()
r = s.reverse(1534236469)
print(r)