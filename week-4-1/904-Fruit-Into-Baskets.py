class Solution:
    def totalFruit(self, tree):
        l = 0
        nums = collections.Counter()
        rtn = 0
        
        for index, val in enumerate(tree):
            nums[val] += 1
            while len(nums) > 2:
                nums[tree[l]] -= 1
                if not nums[tree[l]]:
                    nums.pop(tree[l])
                l += 1
            rtn = max(rtn, index - l + 1)
        
        return rtn
        
