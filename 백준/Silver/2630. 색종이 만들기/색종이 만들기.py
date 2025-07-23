def count_paper(paper_list, r, start_row=0, start_col=0):
    global white, blue
    
    # 첫 번째 원소로 전체가 같은지 확인
    first_value = paper_list[start_row][start_col]
    is_uniform = True
    
    # 조기 종료: 다른 값이 발견되면 바로 분할
    for i in range(start_row, start_row + r):
        for j in range(start_col, start_col + r):
            if paper_list[i][j] != first_value:
                is_uniform = False
                break
        if not is_uniform:
            break
    
    if is_uniform:
        if first_value == 0:
            white += 1
        else:
            blue += 1
        return
    
    # 분할정복 (새 리스트 생성하지 않고 인덱스만 전달)
    half = r // 2
    count_paper(paper_list, half, start_row, start_col)                    # 좌상단
    count_paper(paper_list, half, start_row, start_col + half)             # 우상단  
    count_paper(paper_list, half, start_row + half, start_col)             # 좌하단
    count_paper(paper_list, half, start_row + half, start_col + half)
    
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

count_paper(data, n)
print(white)
print(blue)