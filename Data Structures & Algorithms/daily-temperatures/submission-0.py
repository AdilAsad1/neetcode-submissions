class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        

        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            
            while stack and current_temp > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                output[stack_idx] = i - stack_idx
                
            stack.append(i)


        return output
