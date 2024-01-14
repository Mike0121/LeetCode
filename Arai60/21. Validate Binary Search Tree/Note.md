2:✖ 28.Nov.2023


1. ヒント:
[1,1] (Flase), [2, 2, 2] (False)のパターンもある


2. dfsのreturnの書き方に関して
下記の2パターンは、"ほぼ"同じである。
が、上の書き方は、左がFalseの場合、右のサブツリーの検証は行われない。
```

return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))

if not dfs(root.left, root.val, high):
                return False
            
            if not dfs(root.right, low, root.val):
                return False
```