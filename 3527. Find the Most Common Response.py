class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        n = len(responses)
        max_freq = float(-inf)
        result = ""
        res_dict = {}
        for i in range(n):
            response = set(responses[i])
            for res in response:
                res_dict[res] = res_dict.get(res, 0) + 1
                if res_dict[res] > max_freq:
                    max_freq = res_dict[res]
                    result = res
                elif res_dict[res] == max_freq:
                    if res < result:
                        result = res    
        return result 
