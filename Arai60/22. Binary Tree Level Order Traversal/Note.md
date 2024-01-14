1:✖ 14.Oct.2023


1. Quiz popleftではなく、popを使うとどのような出力になるか。
**深さ優先探索になる。**
最後に使った値をfor文で見ていくので、
親ノードから、ひたすら右の子ノードを見て、終わったら左の子ノードを処理する
という順番になる。
[[3],[20,7],[15,9]]

2. popの復習
```
list = [10, 20, 30, 40, 50]
item = lst.pop()      # item は 50, lst は [10, 20, 30, 40]
item2 = lst.pop(1)   # item2 は 20, lst は [10, 30, 40]
```

3. if level: と if level is not None:の違い
Choosing between these two depends on the specific condition you need to check in your code. If you only want to check against None, use if level is not None:. If you want to check for any value that is not falsy (which includes None), use if level:.

if level:
This statement checks if level is "truthy", which means it checks for a value that is not considered "falsy" in Python.
In Python, ***various values are considered falsy, such as None, False, numeric zeros (0, 0.0), empty sequences ('', [], {}), and other similar default instances which are implicitly evaluated as False.***
So, if level: will be False if level is any of these falsy values.

if level is not None:
This statement explicitly checks whether level is not equal to None.
***This is a strict check solely for the None value.*** It does not consider whether level might be another falsy value like 0, False, or an empty sequence.
It will be True for any value other than None, including other falsy values like 0, False, etc.
Example:
            