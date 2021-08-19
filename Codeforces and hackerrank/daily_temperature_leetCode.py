class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        ans = [-1 for x in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            if temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))

            else:
                while len(stack) != 0 and temperatures[i] > stack[-1][0]:
                    element = stack.pop(-1)
                    ans[element[1]] = (i - element[1])
                stack.append((temperatures[i], i))
        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = 0
        return ans
