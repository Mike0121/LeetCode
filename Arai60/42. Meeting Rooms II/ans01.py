class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        #重要:startとendはそれぞれ個別にsortする必要がある。
        # ↓startのみにしかsortされないので×
        # for interval in sorted(intervals):
        #     start.append(interval[0])
        #     end.append(interval[1])

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals]) 

        count, ans = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] >= end[e]:
                e += 1
                count -= 1
            else:
                s += 1
                count += 1

            ans = max(count, ans)
        
        return ans

        