class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_track = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_track:
                count += prefix_track[prefix_sum - k]
            prefix_track[prefix_sum] = prefix_track.get(prefix_sum, 0) + 1
        return count        



