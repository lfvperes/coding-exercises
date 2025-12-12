roman = "IVXLCDM"
def decimal_to_roman(N: int) -> str:
    count_tens = N // 10
    if count_tens < 4:
        count_fives = (N % 10) // 5
        count_ones = N % 5
        tens = count_tens*"X"
        fives = count_fives*"V"
        ones = count_ones*"I"
        answer = f"{tens}"
        if count_ones == 4:
            if count_fives == 0:
                answer += "IV"
            elif count_fives == 1:
                answer += "IX"
        else:
            answer += f"{fives}{ones}"
    else:
        answer = "".join([roman[roman.find(r)+2] for r in decimal_to_roman(count_tens)]) + decimal_to_roman(N%10)
    
    return answer

for i in range(2995,3005):
    answer = decimal_to_roman(i)
    print(f"{i}={answer}")
