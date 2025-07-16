def solution(my_string, indices):
    
    my_string_list = list(my_string)
    for i in indices:
        my_string_list[i] = ""

    answer = "".join(my_string_list)
    return answer