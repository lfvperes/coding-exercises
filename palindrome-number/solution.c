bool isPalindrome(int x) {
    if (x < 0)
        return false;
    
    int n = 0;
    int xCopy = x;

    while (xCopy > 0) {
        xCopy /= 10;
        n++;
    }
    
    for (int i = 0; i < n/2; i++) {
        int left = (x / (int)pow(10,n-i-1)) % 10;
        int right = (x % (int)pow(10,i+1)) / (int)pow(10,i);
        if (left != right)
            return false;
    }

    return true;
}