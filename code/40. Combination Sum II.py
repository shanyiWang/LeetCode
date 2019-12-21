class Solution:
    def combinationSum2(self, candidates, target):
        def combinationSum2_helper(candidates, target, index, result, cur):
            if target == 0:
                result.append(list(cur))
            elif target > 0:
                for i in range(index, len(candidates)):
                    if i != index and candidates[i] == candidates[i-1]:
                        continue
                    cur.append(candidates[i])
                    combinationSum2_helper(candidates, target-candidates[i], i+1, result, cur)
                    cur.pop()

        candidates = sorted(candidates)
        index = 0
        result, cur = [], []
        combinationSum2_helper(candidates, target, index, result, cur)
        print(result)

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
s.combinationSum2(candidates, target)