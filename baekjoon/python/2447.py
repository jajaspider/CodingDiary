def print_star(star_matrix):
    # i는 횟수
    matrix = []
    for i in range(0, 3 * len(star_matrix)):
        print(i)
        print(len(star_matrix))
        print("---------------------")
        # 두번째 줄만
        if i // len(star_matrix) == 1:
            matrix.append(
                star_matrix[i % len(star_matrix)] + " " * len(star_matrix) + star_matrix[i % len(star_matrix)])
        else:
            matrix.append(star_matrix[i % len(star_matrix)] * 3)
    return matrix


def replace_star(value):
    n = 1
    star = ["***", "* *", "***"]

    while True:
        if 3 ** n == value:
            break
        n += 1

    for i in range(0, n - 1):
        star = print_star(star)
    for i in star:
        print(i)


value = int(input())
replace_star(value)
