/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int carry = 1;
    *returnSize = 0;
    
    for (int i = digitsSize-1; i >= 0; i--) {
        if (digits[i] + carry > 9) {
            digits[i] = 0;
            carry = 1;
        } else {
            digits[i] += carry;
            carry = 0;
        }
        (*returnSize)++;
    }
    
    if (carry == 1) {
        (*returnSize)++;
        int* output = (int*)malloc((digitsSize+1) * sizeof(int));
        memset(output+1, 0, digitsSize * sizeof(int));
        output[0] = carry;
        return output;
    } else {
        return digits;
    }
}