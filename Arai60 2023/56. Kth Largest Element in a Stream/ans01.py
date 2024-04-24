class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums[:k]

        #ヒープを作成する。
        heapify(self.nums)

        #rangeで利用する長さは、元々のnumsの長さのため、
        #selfはつけない。
        for n in range(k, len(nums)):
            #ヒープの最小値より大きい値があった場合、
            #ヒープの値を更新
            if nums[n] > self.nums[0]:
                heappushpop(self.nums, nums[n])

    
    def add(self, val: int) -> int:
        self.val = val
        #長さkに達していない場合は問答無用で値を追加
        if len(self.nums) < self.k:
            heappush(self.nums, self.val)

        elif self.nums[0] < self.val:
            heappushpop(self.nums, self.val)
        
        return self.nums[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)