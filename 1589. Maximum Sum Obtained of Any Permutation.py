class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        idx_freq = [0] * len(nums)
        for l, r in requests:
            idx_freq[l] += 1
            if r + 1 < len(nums):
                idx_freq[r+1] -= 1
        for i in range(1, len(nums)):
            idx_freq[i] += idx_freq[i-1]       
        for i, num in zip(sorted(range(len(idx_freq)), key=lambda i:idx_freq[i]), sorted(nums)):
            nums[i] = num
        for j in range(1, len(nums)):
            nums[j] += nums[j-1]
        ans = 0
        for left, right in requests:
            cur = nums[right] - nums[left - 1] if left - 1 > -1 else nums[right]
            print(cur)
            ans += cur
        return ans % (10 ** 9 + 7)  

