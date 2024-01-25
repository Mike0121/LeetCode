class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        i = 0
        zigzag = [[] for _ in range(numRows)]

        while i < len(s):
            for row in range(numRows):
                if i >= len(s): break
                zigzag[row].append(s[i])
                i += 1

            for row in range(numRows - 2, 0, -1):
                if i >= len(s): break
                zigzag[row].append(s[i])
                i += 1

        string_line_by_line = ""

        for row in range(len(zigzag)):
            string_line_by_line += ("").join(zigzag[row])

        return string_line_by_line
                

        