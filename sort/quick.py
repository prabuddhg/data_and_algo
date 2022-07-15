'''
unsorted list = 54 26 93 17 77 31 44 55 20
Pivot is at 54 (0)
LM is at 26 (Pivot+1 = 1), RM is at 8 (len of list - 1)

LM has to be incremented and RM has to be decremented. The junction is splitting point (SP)

iteration #1
54 26 93 17 77 31 44 55 20
Pivot=0 (54), LM=26 (1), RM=20 (8)

    iteration #1.1 (is LM>RM?) no

    # LM increments
    26 (LM) < 54 (Pivot), yes, LM = LM + 1 which is 93
    93 (LM) < 54 (Pivot), no,  stop LM increments

    # RM increments
    20 (RM) < 54 (Pivot), yes, stop RM increments, exchange = true

    # Do exchange
    Swap places with LM and RM (93 with 20)
    new list is 54 26 20 17 77 31 44 55 93

    iteration #1.2 (is LM>RM?) no
    # LM increments
    20 (LM) < 54 (Pivot), yes, LM = LM + 1 which is 17
    17 (LM) < 54 (Pivot), yes, LM = LM + 1 which is 77
    77 (LM) < 54 (Pivot), no,  stop LM increments

    # RM increments
    93 (RM) < 54 (Pivot), no,  RM = RM - 1 which is 55
    55 (RM) < 54 (Pivot), no,  RM = RM - 1 which is 44
    44 (RM) < 54 (Pivot), yes, stop RM increments, exchange = true

    # Do exchange
    Swap places with LM and RM (77 with 44)
    new list is 54 26 20 17 44 31 77 55 93

    iteration #1.3 (is LM>RM?) no
    # LM increments
    44 (LM) < 54 (Pivot), yes, LM = LM + 1 which is 31
    31 (LM) < 54 (Pivot), yes, LM = LM + 1 which is 77
    77 (LM) < 54 (Pivot), no, stop LM increments

    # RM increments
    77 (RM) < 54 (Pivot), no, RM = RM - 1 which is 31
    31 (RM) < 54 (Pivot), yes, stop RM increments, exchange = true

    # Check is LM > RM, yes, exchange LM with Pivot
    new list 31 26 20 17 44 54 77 55 93
    left side of list(31 26 20 17 44)
    right side of list(77 55 93)

    # Do exchange
    Swap places with LM and RM (77 with 31)
    new list


'''