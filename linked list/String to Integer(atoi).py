class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        symbols = ['+', '-']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        dot = '.'

        def is_num_symbol_begin(str):
            if str[0] in symbols:
                return 'symbol'
            elif str[0] in numbers:
                return 'number'
            else:
                return 'other'

        def process_num(str):
            for i in range(len(str)):
                if str[i] not in numbers:
                    return str[:i]
            return str

        def process_float(str):
            if dot in str:
                index = str.index('.')
                str = str[:index]
            return str

        str = str.strip()
        minus = 1
        if len(str) == 0:
            return 0

        str = str.split(' ')[0]
        if is_num_symbol_begin(str) == 'other':
            return 0
        if is_num_symbol_begin(str) == 'symbol':
            if len(str) <= 1:
                return 0
            if str[0] == '-':
                minus = -1
            str = str[1:]
        str = process_num(str)
        str = process_float(str)
        if len(str) == 0:
            return 0
        print(str)
        res = int(str)
        print(res)
        if res > pow(2, 31) - 1:
            if minus == 1:
                return pow(2, 31) - 1
            else:
                return -1 * pow(2, 31)
        return minus * res