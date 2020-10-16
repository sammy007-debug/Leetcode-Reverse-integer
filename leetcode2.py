x = -123




def reverseInteger(x):
    def divide(integer, divider):
        return int(integer * 1.0 / divider)

    def mod(integer, m):
        if integer < 0:
            return integer % -m
        return integer % m  


    


    MAXInt = 2**31 
    MAXInt = MAXInt - 1
    MINInt = 2**31
    MINInt = MINInt * - 1

    result = 0
    while x != 0:
        remainder = mod(x, 10)
        x = divide(x, 10)
        if result > divide(MAXInt, 10) or (result == divide(MAXInt, 10) and result > 7):
            return 0
        elif result < divide(MINInt, 10) or (result == divide(MINInt, 10) and result < -8):
            return 0
        result = result * 10 + remainder

    return result

print(reverseInteger(x))

  