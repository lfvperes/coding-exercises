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

roman_examples = []
for i in range(2994,3005):
    answer = decimal_to_roman(i)
    roman_examples.append(answer)
    print(f"{i}={answer}")

def roman_to_decimal(R: str) -> int:
    answer: int = 0
    size: int = len(R)
    if size == 1:
        index: int = roman.find(R)
        multiplier: int = 5 ** (index % 2)
        zeros: int = index // 2
        answer += multiplier * 10 ** zeros
    else:
        cur = R[0]
        nxt = R[1]
        if roman.find(cur) < roman.find(nxt):
            answer += roman_to_decimal(nxt) - roman_to_decimal(cur)
            if size > 2:
                answer += roman_to_decimal(R[2:])
        else:
            answer += roman_to_decimal(cur) + roman_to_decimal(R[1:])

    return answer

for r in roman_examples:
    print(f"{r}={roman_to_decimal(r)}")