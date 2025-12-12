
roman = "IVXLCDM"

def convert_to_roman(N: int) -> str:
    answer: str = ""
    if N < 40:
        count_tens = N // 10
        count_fives = (N - count_tens * 10) // 5
        count_ones = N % 5
        tens = count_tens*"2"
        fives = count_fives*"1"
        if count_ones == 4:
            ones = "0"
            if count_fives == 0:
                answer += f"{tens}01"
            elif count_fives == 1:
                answer += f"{tens}02"
        else:
            ones = count_ones*"0"
            answer += f"{tens}{fives}{ones}"
    else:
        answer = "".join([str(int(r)+2) for r in convert_to_roman(N//10)]) + convert_to_roman(N%10)
    
    return answer
# "".join([roman[int(r)] for r in answer])
def decode_to_roman(encoded: str):
    return "".join([roman[int(r)] for r in encoded])

def decimal_to_roman(N: int):
    r = convert_to_roman(N)
    return decode_to_roman(r)
for i in range(2995,3005):
    answer = decimal_to_roman(i)
    print(f"{i}={answer}")
# print(f"{5}={roman[int(convert_to_roman(5))]}")
# print(f"{50}={roman[int(convert_to_roman(50))]}")
