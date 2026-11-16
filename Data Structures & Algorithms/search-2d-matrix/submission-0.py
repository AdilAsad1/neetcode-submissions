class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = []
        for i in matrix:
            if target >= i[0] and target <= i[-1]:
                row = i
                break

        if not row:
            return False

        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False



    
