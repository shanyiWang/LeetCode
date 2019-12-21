class Solution:
    def combinationSum(self, candidates, target):
        def combinationSum_helper(candidates, target, index, result, cur):
            if target == 0:
                result.append(list(cur))
            elif target > 0:
                for i in range(index, len(candidates)):
                    cur.append(candidates[i])
                    combinationSum_helper(candidates, target-candidates[i], i, result, cur)
                    cur.pop()

        candidates = sorted(candidates)
        result, cur = [], []
        index = 0
        combinationSum_helper(candidates, target, index, result, cur)
        print(result)

s = Solution()
candidates = [2,3,6,7]
target = 7
s.combinationSum(candidates, target)