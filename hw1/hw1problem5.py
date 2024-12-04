# Vincent Yang
# 116579508
# viyyang
#
# IAE 101 (Fall 2024)
# HW 1, Problem 5

def how_long(distance, fraction, scale):
    c = 186000
    return distance / c / fraction / (60 if scale == "M" else
                                      3600 if scale == "H" else
                                      86400 if scale == "D" else
                                      31536000)


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = how_long(238900, 0.01, "M")  # approximate distance to Moon
    print("how_long(238900, 0.01, 'M') is:", test1)
    print()
    test2 = how_long(45594000, 0.01, "H")  # approximate distance to Mars
    print("how_long(45594000, , 0.01, 'H') is:", test2)
    print()
    test3 = how_long(93000000, 1.0, "M")  # approximate distance to Sun
    print("how_long(93000000, 1.0, 'M') is:", test3)
    print()
    # approximate distance to edge of Solar System
    test4 = how_long(9000000000, 0.01, "D")
    print("how_long(9000000000, 0.01, 'D') is:", test4)
    print()
    # approximate distance to closest system Alpha Centauri
    test5 = how_long(25000000000000, 0.01, "Y")
    print("how_long(25000000000000, 0.01, 'Y') is:", test5)
    print()
