class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            x = abs(nums[num])
            nums[x-1] = -1 * nums[x-1]
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

