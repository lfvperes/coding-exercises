class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.seek(nums, 0, len(nums)-1, target)

    def seek(self, nums, start, end, target):
        n = end - start
        if n <= 1:
            if nums[start] >= target:
                return start
            elif nums[end] < target:
                return end+1
            else:
                return end
        middle = (start + end) // 2
        if nums[middle] > target:
            return self.seek(nums, start, middle-1, target)
        elif nums[middle] < target:
            return self.seek(nums, middle+1, end, target)
        else:
            return middle
