class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxL = 0
        n = len(s)
        tmp = [0] * n  # 标记数组
        cur = 0

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    tmp[i], tmp[j] = 1, 1  # 匹配成功时标记

        for num in tmp:  # 计算连续1出现的最大次数
            if num:
                cur += 1
            else:  # 遇到0时中断，进行对比，并重置
                maxL = max(cur, maxL)
                cur = 0
        maxL = max(cur, maxL)  # 最后一次统计可能未终断，多做一次对比

        return maxL
