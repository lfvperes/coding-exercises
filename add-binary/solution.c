char* addBinary(char* a, char* b) {
    char* c;
    int carry = 0;
    int nA = strlen(a);
    int nB = strlen(b);
    int n = nA;
    int s, bit;

    if (nA < nB)
        n = nB;

    char* buffA = (char*)malloc((n + 1) * sizeof(char));
    memset(buffA, '0', n);
    strcpy(buffA + (n - nA), a);
    
    char* buffB = (char*)malloc((n + 1) * sizeof(char));
    memset(buffB, '0', n);
    strcpy(buffB + (n - nB), b);

    char* buffC = (char*)malloc((n + 2) * sizeof(char));
    memset(buffC, '0', n + 1);

    for (int i = n-1; i >=0 ; i--) {
        s = (buffA[i] - '0') + (buffB[i] - '0') + carry;
        bit = s % 2;
        carry = s / 2;
        
        buffC[i+1] = bit + '0';
    }
    
    buffC[0] = carry + '0';

    buffC[n+1] = '\0';

    if (buffC[0] == '1') {
        return buffC;
    } else {
        return buffC+1;
    }
    
}