def check_grade(score):
    if 90 <= score <= 100:
        print("A")
    elif 80 <= score <= 89:
        print("B")
    elif 70 <= score <= 79:
        print("C")
    elif 60 <= score <= 69:
        print("D")
    else:
        print("F")

        
score = int(input())
check_grade(score)