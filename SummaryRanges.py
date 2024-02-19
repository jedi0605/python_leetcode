from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        s, e = nums[0], nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] > e + 1:  # range break
                if s != e:
                    res.append(str(s) + "->" + str(e))
                else:
                    res.append(str(s))
                s, e = nums[i], nums[i]
            else:
                e = nums[i]

        # for last range
        if s != e:
            res.append(str(s) + "->" + str(e))
        else:
            res.append(str(s))
        return res
