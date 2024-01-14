1:△ 15.Dec.2023


Note:
他の解答未確認。


1. Binary Treeに引っ張られない
×⇒self.sortedArrayToBST(nums[mid+1:r])
〇⇒self.sortedArrayToBST(nums[mid+1:r+1])