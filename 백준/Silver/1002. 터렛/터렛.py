def find_enemy(x1, y1, r1, x2, y2, r2):
    # 위치가 겹칠때
    if x1 == x2 and y1 == y2:
        if r1 == r2:  # 완전히 겹침
            return -1
        else:  # 중심은 같지만 반지름이 다름 (교점 없음)
            return 0
        
    # 두 위치 사이의 거리 구하기
    loca_distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

    # 두 사정거리의 합
    enemy_range_add = (r1 + r2) ** 2

    # 두 사정거리의 ck
    enemy_range_sub = (r1 - r2) ** 2

    # 교점이 두개인 경우
    if enemy_range_sub < loca_distance < enemy_range_add:
        return 2

    # 교점이 한개인 경우
    if enemy_range_sub == loca_distance or enemy_range_add == loca_distance:
        return 1

    return 0

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    result = find_enemy(x1, y1, r1, x2, y2, r2)
    print(result)