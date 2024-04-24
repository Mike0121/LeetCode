import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Hint1: nums1 and 2 are in non-decreasing order.
        
        #リストとして定義したデータから、heapとして値を出し入れできるheap便利過ぎないか？
        heap = []
        #回答を格納する用のlist
        result = []

        #heapに、
        #nums1の各値と、nums2の最初の要素の和を、position:0として入れる。
        for x in nums1:
            heapq.heappush(heap, [x + nums2[0], 0])

        while k > 0 and heap:
            #ヒープから値とpositionを取り出す。
            #Pythonのheapは最小ヒープのため、常に最小の値が取り出される。
            #ちなみに、ヒープの中身がリスト形式の場合、リストやタプルの最初の要素に基づいて行われる。
            h = heapq.heappop(heap)
            val, pos = h[0], h[1]

            #resultに、ヒープから値を取り出された最小値の
            #nums1の値 = s - nums2[position]
            #nums2の値 = nums[position] を記録する。
            result.append([val - nums2[pos], nums2[pos]])

            #もし、現在見ているposition+1がnums2の値より小さい場合、
            #⇔nums2にまだ値がある場合
            #heapに次の最小となりうる値を追加
            if pos + 1 < len(nums2):
                #下記が1番トリッキー
                heapq.heappush(heap, [val - nums2[pos] + nums2[pos+1], pos+1])
            k -= 1

        return result