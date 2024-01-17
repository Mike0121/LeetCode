class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        zigzag = [[] for _ in range(numRows)]
        i = 0

        while i < len(s):
            #行き
            for n in range(numRows):
                if i >= len(s): break
                zigzag[n].append(s[i])
                i += 1

            #帰り
            for n in range(numRows-2, 0, -1):
                if i >= len(s): break
                zigzag[n].append(s[i])
                i += 1

        for i in range(1, numRows):
            zigzag[0].extend(zigzag[i])

        return "".join(zigzag[0])