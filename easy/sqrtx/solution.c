int mySqrt(int x) {
    for (int i = 1; i <= x/2+1; i++) {
        if (x/i < i)
            return i-1;
        else if (x/i == i)
            return i;
    }
    return x/2;
}