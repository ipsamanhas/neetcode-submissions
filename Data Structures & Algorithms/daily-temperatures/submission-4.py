class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # i bascially return the num of days after which the
        # temp will be higher than the current temperature

        result = [0] * len(temperatures) #the final array, also the default value will be 0
        stack = [] # will store [temp, index]
        # the stack will be monotonically decreasing


        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (index - stackInd)
            stack.append([temp, index])
        return result

        