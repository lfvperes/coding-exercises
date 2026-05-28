bool checkRecord(char* s) {
    int absences = 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] == 'A')
            absences++;
        if (absences >= 2)
            return false;
        if (i >= 1 && i < n) {
            if (s[i] == 'L') {
                if (s[i-1] == 'L' && s[i+1] == 'L')
                    return false;
            }
        }
    }
    return true;
}