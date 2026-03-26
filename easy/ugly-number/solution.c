bool isUgly(int n) {
    if (n <= 0)
        return false;
    if (n <= 5)
        return true;

    while (n > 1) {
        if (!(n % 2)) 
            n /= 2;
        
        if (!(n % 3)) 
            n /= 3;
        
        if (!(n % 5)) 
            n /= 5;
        
        if (n == 1)
            return true;
        if (n % 2 && n % 3 && n % 5)
            return false;
    }
    return false;
}