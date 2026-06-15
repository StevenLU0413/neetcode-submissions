class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = defaultdict(list)
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for count in sorted_freq[:k]:
            res.append(count[0])
        
        return res
    