
def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, (No//2)+1, 1):
        if (No % i) == 0:
            return False
        i += 1
    return True


    # while (i * i) <= No:
    #     if (No % i) == 0:
    #         return False
    #     i += 1
    # return True