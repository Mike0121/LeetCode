class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        #dictを"valueの値"で"降順"にソートし、
        #"k番目まで"の"keyの値"を取得する。
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_d[:k]]