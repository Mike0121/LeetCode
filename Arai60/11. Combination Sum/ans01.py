class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #おそらく、for文で各要素を回し、while文で値がtargetを超えないと足し続けるような形にしたい。
        #しかし、"targetを超えない"が難しく、例えば"2"を3回入れてから他のを試すことにすると、
        #"7"は絶対入らなくなる。
        #そこで、targetから値を引いていき、backtrackingを行う形にできないかを検討する。
        ans = []
        tmp = []
        def back_tracking(i, target, tmp):
            #ベースケース
            #インデックスiが最後まで到達した場合
            if i == len(candidates):
                if target== 0:
                    ans.append(tmp[:])
                return

            if target - candidates[i] >= 0:
                tmp.append(candidates[i])
                #まだ値を足すことが可能な場合は、targetの値をcandidates[i]で更新して
                #同じiでback_trackingを実行
                back_tracking(i, target-candidates[i], tmp)
                tmp.pop()
            #while文を抜けたら、tmpの値を更新して
            #次のbacktrackingに入る。
            back_tracking(i+1, target, tmp)

        back_tracking(0, target, tmp)

        return ans