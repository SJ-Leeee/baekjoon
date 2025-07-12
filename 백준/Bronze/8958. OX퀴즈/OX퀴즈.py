
N = int(input())

def score_check(answer_list):
    result = 0
    for check in answer_list:
        if len(check) > 0:
            for i in range(1, len(check) + 1):
                result += i

    print(result)


for _ in range(N):
    input_data = input()
    answer_list = input_data.split("X")
    score_check(answer_list)
