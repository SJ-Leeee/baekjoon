num1 = int(input())
num2 = int(input())

def cal3(num1, num2):
    hundreds_digit = num2 // 100
    tens_digit = num2 % 100 // 10
    ones_digit = num2 % 10

    answer_3 = ones_digit * num1
    answer_4 = tens_digit * num1
    answer_5 = hundreds_digit * num1
    answer_6 = answer_5 * 100 + answer_4 * 10 + answer_3

    print(answer_3)
    print(answer_4)
    print(answer_5)
    print(answer_6)

    return


cal3(num1, num2)
