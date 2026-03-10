/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int first, second;
    int* indices;
    for (int i = 0; i < numsSize - 1; i++) {
        first = nums[i];
        second = target - first;
        for (int j = i+1; j < numsSize; j++) {
            if (second == nums[j]) {
                indices = (int*)malloc(2 * sizeof(int));
                indices[0] = i;
                indices[1] = j;
                *returnSize = 2;
                break;
            }
        }
    }
    return indices;
}