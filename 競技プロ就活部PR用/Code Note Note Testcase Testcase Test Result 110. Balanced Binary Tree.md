
# 1回目
5分考え方がわからず、解けず。
1つ1つ上からノードをチェックしていって、あるノードが止まった段階を記録しておいて、
反対側が2回以上進んだ場合にFalseをreturnするのかと考えたが、正直どうやってそれぞれの段階を記録・判断するのかを具体的に思い浮かばず。

答えを見た後に考えると、再帰的に行う、ボトムアップ(下の人に電話をかけるを繰り返し、反応を上に伝播させていく)考えが思い浮かべばよかったが、正直コードに落とし込むにはもう少し練習が必要そう。

2回目は、他参加者のコードを参考に写すのではなく、理解できたと思ったら
何も見ずに自分で書いてみて、再現できました。

#### 時間計算量の理解に不安があるので、もし間違えていたらご指摘いただきたいです。

- 時間計算量: O(2N) (行き + 帰りで全てのノードを1度ずつ通る) (?)
- 空間計算量: O(N) (各ノード分)
- N:ノード数

# 2回目
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_subtree_gap(root) >= 0
    
    def get_subtree_gap(self, root):
        if not root:
            return 0

        left_height, right_height = self.get_subtree_gap(root.left), self.get_subtree_gap(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) >= 2:
            return -1
        
        return max(left_height, right_height) + 1
```

# 3回目
上記のコードをベースに、Odaさんのアドバイスを参照に、
isBalanced, get_subtree_gapを同時に行いました。

- 時間計算量: O(N) (?)
- 空間計算量: O(N) (各ノード分)
- N:ノード数

# 3回目
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedAuxiliary(root):
            if not root:
                return 0, True

            height_left, is_balanced_left = isBalancedAuxiliary(root.left)
            height_right, is_balanced_right = isBalancedAuxiliary(root.right)

            node_height = max(height_left, height_right) + 1
            balanced_flag = is_balanced_left and is_balanced_right and abs(height_left - height_right) < 2

            return node_height, balanced_flag

        _, result = isBalancedAuxiliary(root)
        return result
```

# 3周解き後
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedAuxiliary(root):
            if not root:
                return 0, True

            height_left, is_balanced_left = isBalancedAuxiliary(root.left)
            height_right, is_balanced_right = isBalancedAuxiliary(root.right)
            
            node_height = max(height_left, height_right) + 1
            is_balanced = is_balanced_left and is_balanced_right and abs(height_left - height_right) < 2

            return node_height, is_balanced

        _, result = isBalancedAuxiliary(root)
        return result
```
