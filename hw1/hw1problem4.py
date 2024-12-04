# Vincent Yang
# 116579508
# viyyang
#
# IAE 101 (Fall 2024)
# HW 1, Problem 4

def temp_converter(temperature, new_unit):
    return (temperature - 32) * 5/9 if new_unit == "C" else temperature * 9/5 + 32


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("temp_converter(100,'C') is", temp_converter(100, 'C'))
    print()
    print("temp_converter(0,'F') is", temp_converter(0, 'F'))
    print()
    print("temp_converter(212,'C') is", temp_converter(212, 'C'))
    print()
    print("temp_converter(32,'C') is", temp_converter(32, 'C'))
    print()
    print("temp_converter(50,'F') is", temp_converter(50, 'F'))
    print()
