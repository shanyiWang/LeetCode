class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def helper(state, total):
            key = ''.join(state)
            if key in self.memory:
                return self.memory[key]
            for i in range(1, len(state)):
                if state[i] == '0':
                    state[i] = '1'
                    if (total - i <= 0) or not helper(state, total - i):
                        self.memory[key] = True
                        state[i] = '0'
                        return True
                    state[i] = '0'
            self.memory[key] = False
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memory = {}
        state = ['0'] * (1 + maxChoosableInteger)
        return helper(state, desiredTotal)

s = Solution()
res = s.canIWin(10, 0)
print(res)