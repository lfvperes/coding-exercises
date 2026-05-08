int passThePillow(int n, int time) {
    int direction = 1;
    int i = 1;
    while (time > 0) {
        if (direction > 0 && i == n)
            direction = -1;
        
        if (direction < 0 && i == 1)
            direction = 1;
        
        i += direction;
        time--;
    }
    return i;
}