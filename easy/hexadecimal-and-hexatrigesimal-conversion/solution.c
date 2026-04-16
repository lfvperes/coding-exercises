#include <math.h>

void convertToBase(int n, int base, char* buf, int size);

char* concatHex36(int n) {
    int maxHexadec = 6;
    char* result16 = malloc(maxHexadec * sizeof(char));
    convertToBase((int)pow(n, 2), 16, result16, maxHexadec);

    int maxHexatri = 7;
    char* result36 = malloc(maxHexatri * sizeof(char));
    convertToBase((int)pow(n, 3), 36, result36, maxHexatri);

    char* result = malloc(maxHexadec + maxHexatri * sizeof(char));
    strcpy(result, result16);
    strcat(result, result36);
    
    return result;
}

void convertToBase(int n, int base, char* buf, int size) {
    memset(buf, '0', size);
    int temp, i = size-2;
    while (n > 0) {
        temp = n % base;
        temp += (temp < 10) ? '0' : ('A' - 10);
        buf[i--] = temp;
        n /= base;
    }

    int start = i+1;
    int j = 0;
    while (start < size - 1)
        buf[j++] = buf[start++];
    buf[j] = '\0';
    
    return;
}