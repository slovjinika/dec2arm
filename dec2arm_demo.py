import argparse

def dec2arm(input_number):
    if not 1 <= input_number <= 29999:
        raise ValueError("The number must be between 1 and 29999")

    armenian_symbols = {
        10000: "ՕՖ",
        1000: "ՌՍՎՏՐՑՒՓՔ",
        100: "ՃՄՅՆՇՈՉՊՋ",
        10: "ԺԻԼԽԾԿՀՁՂ",
        1: "ԱԲԳԴԵԶԷԸԹ"
    }

    result = ""
    for divisor in [10000, 1000, 100, 10, 1]:
        symbols = armenian_symbols[divisor]
        quotient, input_number = divmod(input_number, divisor)
        if quotient > 0:
            if divisor == 10000:
                result += symbols[quotient - 1] + "\u0305"  # Use overline for 10000 multiplier
            else:
                result += symbols[quotient - 1]

    if input_number > 0:
        result += armenian_symbols[1][input_number - 1]

    return result

for i in range(1, 10000):
    print(f"{i}; {dec2arm(i)}")
