class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for i in range(len(nums)):
            if nums[i] not in freqs:
                freqs[nums[i]] = 0
            freqs[nums[i]] += 1
        key_set = list(freqs.keys())
        kss = sorted(key_set, key=freqs.get, reverse=True)
        return kss[:k]