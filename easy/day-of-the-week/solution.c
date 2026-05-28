char* dayName[] = {
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
};
int monthsSize[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
char* dayOfTheWeek(int day, int month, int year) {
    int dateNumber = 4; // starting on dec 31 1970
    for (int y = 1971; y < year; y++) {
        dateNumber += 365;
        // check if leap year
        if ((y % 400 == 0) || (y % 100 != 0 && y % 4 == 0))
            dateNumber += 1;
    }
    // adding days of the month for current year
    for (int m = 1; m < month; m++) {
        if (m == 2)
            if ((year % 400 == 0) || (year % 100 != 0 && year % 4 == 0))
                dateNumber += 1;
        dateNumber += monthsSize[m-1];
    }
    // adding days for current month
    dateNumber += day;
    
    return dayName[dateNumber % 7];
}