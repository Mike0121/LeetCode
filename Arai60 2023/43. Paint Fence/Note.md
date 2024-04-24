1:✖ 24.Dec.2023
解法への発想:
参照:https://leetcode.com/problems/paint-fence/solutions/178010/the-only-solution-you-need-to-read
dpは、大学受験の確率漸化式のように、i-1, i番目とのパターンを"必ず書いて"場合分けをして考える。
おそらく、**i-2番目を考慮する場合でも、今回のように、i-1番目とiを考えてから、NGパターンとしてi-2番目を考える。**
今回は、i番目の色の塗り方(num_ways(i))について、(i)i-1と同じ色で塗る(num_ways_same(i))、(ii)i-1と異なる色で塗るnum_ways_diff(i)、の2パターンに分けて考える。
(i): num_ways_diff(i)
i-1番目の色の塗り方をnum_ways(i-1)とおくと、i-1で塗られた色以外のすべてのパターンがOKのため、
num_ways_diff(i) = num_ways(i-1) * (k-1) 
(ii):num_ways_same(i)
i-1で塗られた色と同じ色でしか濡れないため、
num_ways_same(i) = num_ways(i-1) * 1

ここで、(ii):num_ways_same(i)に関して、3色同じ色でつならってしまうパターンを除く必要があり、
num_ways_same(i) = num_ways_**diff**(i-1) * 1 である。
つまり、num_ways_same(i) = num_ways_**diff**(i-1) * 1 = num_ways(i-**2**) * (k-1) となる。
(i) + (ii)を都度計算していけばよい。