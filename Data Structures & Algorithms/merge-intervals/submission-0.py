class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        output = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(lastend, end)
            else:
                output.append([start,end])
        return output