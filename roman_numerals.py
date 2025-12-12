
roman = "IVXLCDM"
def decimal_to_roman(N: int) -> str:
    answer: str = ""
    if N < 40:
        count_tens = N // 10
        count_fives = (N - count_tens * 10) // 5
        count_ones = N % 5
        tens = count_tens*"X"
        fives = count_fives*"V"
        if count_ones == 4:
            if count_fives == 0:
                answer += f"{tens}IV"
            elif count_fives == 1:
                answer += f"{tens}IX"
        else:
            ones = count_ones*"I"
            answer += f"{tens}{fives}{ones}"
    else:
        answer = "".join([roman[roman.find(r)+2] for r in decimal_to_roman(N//10)]) + decimal_to_roman(N%10)
    
    return answer

for i in range(2995,3005):
    answer = decimal_to_roman(i)
    print(f"{i}={answer}")
