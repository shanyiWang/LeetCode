class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return res
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                k = i + 1
                t = len(nums) - 1
                while k < t:
                    if nums[i] + nums[k] + nums[t] == 0:
                        res.append([nums[i], nums[k], nums[t]])
                        while nums[t-1] == nums[t] and t > k:
                            t -= 1
                        while nums[k] == nums[k+1] and t > k:
                            k += 1
                        t -= 1
                        k += 1
                    elif nums[i] + nums[k] + nums[t] > 0:
                        t -= 1
                    else:
                        k += 1
        return res

nums = [-2,0,0,2,2]
s = Solution()
res = s.threeSum(nums)
print(res)