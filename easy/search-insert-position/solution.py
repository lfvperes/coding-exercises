class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return my_search(nums, target, 0, len(nums)-1)
        
        
def my_search(nums: List[int], target: int, left_idx, right_idx) -> int:
    size = len(nums)
    middle = (right_idx + left_idx) // 2
    if left_idx > right_idx:
        return left_idx
    
    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return my_search(nums, target, middle+1, right_idx)
    elif nums[middle] > target:
        return my_search(nums, target, left_idx, middle-1)