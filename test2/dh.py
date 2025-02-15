def generate_snake_matrix(n):
    matrix = [[0] * (n - i) for i in range(n)]  # 创建一个n行的上三角矩阵

    current_number = 1
    for col in range(n):
        for row in range(col + 1):
            matrix[row][col - row] = current_number
            current_number += 1

    for row in matrix:
        print(' '.join(map(str, row)).strip())  # 打印每一行，去掉末尾空格

# 输入处理
n = int(input())
if n < 1 or n > 100:
    print("输入不在范围内，程序退出。")
else:
    generate_snake_matrix(n)