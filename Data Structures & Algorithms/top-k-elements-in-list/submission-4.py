class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1

        result = []

        sorted_dict = dict(sorted(freq.items(), key = lambda kv: kv[1], reverse=True))

        result = list(sorted_dict.keys())
        return result[0:k]