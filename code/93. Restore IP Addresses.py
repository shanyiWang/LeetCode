class Solution:
    def restoreIpAddresses(self, s: str):
        def valid(s):
            if len(s) == 0:
                return False
            if len(s) >= 2 and s[0] == '0':
                return False
            else:
                if 0 <= int(s) <= 255:
                    return True
                else:
                    return False

        def helper(s, res):
            if len(s) <= 3 and len(res) == 3:
                res.append(s)
                is_valid = True
                for r in res:
                    is_valid = is_valid and valid(r)
                if is_valid:
                    self.record.append(".".join(res))
                res.pop()
                return
            else:
                if len(res) >= 3:
                    return
                for step in range(1, 4):
                    res.append(s[:step])
                    helper(s[step:], res)
                    res.pop()



        if len(s) < 4 or len(s) > 12:
            return []
        self.record = []
        res = []
        helper(s, res)
        print(self.record)
        return self.record

s = Solution()
s1 = "25525511135"
s.restoreIpAddresses(s1)