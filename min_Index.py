from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        dict = {}
        min_index = float('inf')
        for i, str in enumerate(list1):
            if str in list2:
                dict[str] = list1.index(str) + list2.index(str)
                if dict[str] < min_index:
                    min_index = dict[str]
        for val in dict:
            if dict[val] == min_index:
                result.append(val)   
        return result         
                
                


        