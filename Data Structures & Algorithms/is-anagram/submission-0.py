class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_table = dict()
        my_table_2 = dict()

        for i in s:
            if i in my_table:
                my_table[i] += 1
            else:
                my_table[i] = 1

        for i in t:
            if i in my_table_2:
                my_table_2[i] += 1
            else:
                my_table_2[i] = 1


        if my_table == my_table_2:
            return True
        else:
            return False