class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = 0
        for num in nums:
            if num % 2 == 0:
                sum_even += num
        result = []
        for quer in queries:
            val, ind = quer
            if nums[ind] % 2 == 0:
                if (nums[ind] + val) % 2 == 0:
                    nums[ind] += val
                    sum_even += val
                    result.append(sum_even)
                else:
                    sum_even -= nums[ind]
                    nums[ind] += val
                    result.append(sum_even)
            elif (nums[ind] + val) % 2 == 0:
                nums[ind] += val
                sum_even += nums[ind]
                result.append(sum_even)
            else:
                nums[ind] += val 
                result.append(sum_even)   
        return result


            
            



        