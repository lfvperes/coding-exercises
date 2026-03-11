int romanCharToInt(char c) {
    switch (c) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
    }
}

int romanToInt(char* s) {
    int converted = romanCharToInt(s[strlen(s)-1]);
    
    for (int i = 0; i < strlen(s)-1; i++) {
        if (romanCharToInt(s[i]) >= romanCharToInt(s[i+1]))
            converted += romanCharToInt(s[i]);
        else
            converted -= romanCharToInt(s[i]);
    }
    
    return converted;
}