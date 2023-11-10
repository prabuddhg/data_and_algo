num1 = "001"
num2 = "011"


def add_binary(num1, num2):
    num1_list = [int(i) for i in num1]
    num2_list = [int(i) for i in num2]
    for i in range(0, 8-len(num1_list)):
        num1_list = [0] + num1_list
    for i in range(0, 8-len(num2_list)):
        num2_list = [0] + num2_list
    print(f"Padded num1_list {num1_list}")
    print(f"Padded num2_list {num2_list}")
    sum = [0, 0, 0, 0, 0, 0, 0, 0]
    carry = 0
    for i in reversed(range(0, 8)):
        print(f"Processing index at {i} for num1_list={num1_list[i]} and  num2_list={num2_list[i]}")
        #import pdb;pdb.set_trace()
        if num1_list[i] == 1 and num2_list[i] == 1:
            print("1, 1")
            if carry:
                sum[i] = 1
            else:
                sum[i] = 0
            carry = 1
        elif (num1_list[i] == 0) and (num2_list[i] == 0):
            print("0, 0")
            if carry:
                sum[i] = 1
            else:
                sum[i] = 0
            carry = 0
        else:
            print("either 1, or 0")
            if carry:
                sum[i] = 0
                carry = 1
            else:
                sum[i] = 1
                carry = 0
        print(f"sum={sum}")
    print(sum)



add_binary(num1,num2)