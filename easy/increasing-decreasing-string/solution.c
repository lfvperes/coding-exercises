char* sortString(char* s) {
    int freq[26] = {0};
    int n = strlen(s);
    char* result = malloc(sizeof(char) * (n+1));
    bool increasing = true;
    for (int i = 0; i < n; i++)
        freq[s[i]-'a']++;
    
    int i = 0, j = 0;
    while (i < n) {
        if (freq[j] > 0) {
            result[i] = 'a' + j;
            freq[j]--;
            i++;
        }
        if (increasing) {
            if (j == 25)
                increasing = false;
            else
                j++;
        } else {
            if (j == 0)
                increasing = true;
            else
                j--;
        }   
    }
    result[n] = '\0';
    return result;
}