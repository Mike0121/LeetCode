1:✖(brute-forth) 29.Oct.2023
2:✖(DP) 19.Nov.2023 


if dp[n]:
	  break　をなくすとどうなるか？
不正解になる。
s の i 番目から始まる部分文字列が wordDict の単語で終了し、その後の部分も wordDict の単語で構成できることが確定した場合、他の単語を検討する必要はなくなる。

s = "abcdef"
2番目の文字(b)にアクセス: s[1] (1=2-1)
2番目から5番目の文字(bcde)のアクセス:s[1:5]

1. 文字列sから該当する文字列を消す
s = s.replace(target, "")
最悪計算量: O(m)
なぜなら、sの全ての文字を調べる必要があるから。

2. 疑問メモ (要するに何もわかってない。 @19.Nov.2023)
-なぜdpテーブルの長さは、len(s)ではなく、len(s)+1分必要なのか？
⇒文字列 s の各部分文字列が wordDict の単語によって形成できるかどうかを判断するためです。dp[len(s)] = True は空の文字列を表し、これは常に有効な部分文字列と見なされます。

-if dp[i]:を通るのはどのような状況か？
あるi番目までの文字列を調べていて、それがwordとヒットしたとき、そのwordはパスして
次に進んでよい。例えば s = "applepie" で wordDict = ["apple", "pie"] とします。dp 配列を逆順で処理していくと、i = 5（s[5] は 'p'）のときに s[5: 5 + len("pie")] が "pie" と一致します。そのため、dp[5] = True となります。この時点で if dp[i]: が True と評価され、ループは早期に終了します。

-なぜdp[i] = dp[i+len(word)]の文で成立するのか？
i = 0（s[0] は 'a'）のとき、s[0: 0 + len("apple")] は "apple" と一致し、dp[0 + len("apple")] = dp[5] はすでに True に設定されています。したがって、dp[0] = dp[5] は True になります。これは、s の最初の部分 "apple" が wordDict に一致し、残りの部分 "pie" も wordDict に一致するため、全体が wordDict で形成可能であることを意味します。


-for i in range(len(s)-1, -1, -1):, s[i : i+len(word)]の挙動を英語で説明できるか？
for i in range(len(s)-1, -1, -1):
This line of code is used to iterate over a string s in reverse order.
len(s)-1: This is the starting point of the loop. It represents the index of the last character in the string s. For example, if s is "hello", len(s)-1 would be 4, which is the index of 'o'.
-1: This is the end point of the range, exclusive. In Python, ranges go up to, but do not include, the end value. Here, -1 is used to ensure the loop includes the first character of s (index 0).
-1: This is the step value. It means the loop will decrement the index by 1 in each iteration, effectively moving backward through the string.
Overall, this loop is used to access the elements of s starting from the last one and moving backwards to the first one.

s[i : i+len(word)]
This line of code is used to get a substring from s starting at index i and extending up to i+len(word), but not including the character at i+len(word).
i: This is the starting index of the substring.
i+len(word): This is the ending index of the substring, exclusive. The length of the substring will be equal to the length of word.
For example, if s is "hello" and word is "ell", and i is 1, then s[i : i+len(word)] would be "ell" (substring from index 1 to 3).

This code snippet is typically used when you need to iterate through a string in reverse order and extract substrings of a specific length.
