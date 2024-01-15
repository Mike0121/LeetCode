class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        
        zigzag = [[] for _ in range(numRows)]
        index = 0
        step = 1

        for i in range(len(s)):
            
            zigzag[index].append(s[i])

            if index == 0:
                step = 1
            
            if index == numRows-1:
                step = -1

            index += step

        for i in range(1, len(zigzag)):
            zigzag[0].extend(zigzag[i])
            
        return ("").join(zigzag[0])