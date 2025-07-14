count = 0


def z_print(N, row_locate, col_locate, row, col):
    # 다 만들 필요가 없음
    global count

    if N == 1:
        if row_locate == row and col_locate == col:
            return count
        count += 1
        if row_locate == row and col_locate + 1 == col:
            return count
        count += 1
        if row_locate + 1 == row and col_locate == col:
            return count
        count += 1
        if row_locate + 1 == row and col_locate + 1 == col:
            return count
        count += 1
        return

    half = 2 ** (N - 1)
    # 4 4
    # 2 2
    # my = 1, 2

    one_sector = 4 ** (N - 1)

    if col >= col_locate + half and row >= row_locate + half:
        count += one_sector * 3
        z_print(N - 1, row_locate + half, col_locate + half, row, col)
    elif col >= col_locate + half:
        count += one_sector
        z_print(N - 1, row_locate, col_locate + half, row, col)
    elif row >= row_locate + half:
        count += one_sector * 2
        z_print(N - 1, row_locate + half, col_locate, row, col)
    else:
        z_print(N - 1, row_locate, col_locate, row, col)

    return
    # row >= x + add_x
    # 이친구는 1사분면인거야


N, r, c = map(int, input().split())
z_print(N, 0, 0, r, c)
print(count)
