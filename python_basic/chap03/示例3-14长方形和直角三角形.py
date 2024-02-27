# 长方形
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='')
    print()

print('-' * 20)

# 直角三角形
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

print('-' * 20)

# 倒直角三角形
for i in range(1, 6):
    for j in range(1, 6 + 1 - i):
        print('*', end='')
    print()

print('-' * 20)

# 等腰三角形
for i in range(1, 6):
    # 倒空格三角形
    for j in range(1, 6 - i):
        print(' ', end='')
    # 等腰三角形
    for k in range(1, 2 * i):
        print('*', end='')
    print()

print('-' * 20)

# 菱形
rows = eval(input('请输入菱形的行数:'))
while rows % 2 == 0:
    print('请重新输入菱形的行数:')
    rows = eval(input('请输入菱形的行数:'))

# 菱形的上半部分
top_rows = (rows + 1) // 2
for i in range(1, top_rows + 1):
    # 倒空格三角形
    for j in range(1, top_rows + 1 - i):
        print(' ', end='')
    # 等腰三角形
    for k in range(1, 2 * i):
        print('*', end='')
    print()
# 菱形的下半部分
bottom_row = rows // 2
for i in range(1, bottom_row + 1):
    # 空格直角三角形
    for j in range(1, i + 1):
        print(' ', end='')
    # 倒三角
    for k in range(1, 2 * (bottom_row + 1 - i)):
        print('*', end='')
    print()

print('-' * 20)

# 空心菱形
rows = eval(input('请输入空心菱形的行数:'))
while rows % 2 == 0:
    print('请重新输入空心菱形的行数:')
    rows = eval(input('请输入空心菱形的行数:'))

# 菱形的上半部分
top_rows = (rows + 1) // 2
for i in range(1, top_rows + 1):
    # 倒空格三角形
    for j in range(1, top_rows + 1 - i):
        print(' ', end='')
    # 等腰三角形
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 菱形的下半部分
bottom_row = rows // 2
for i in range(1, bottom_row + 1):
    # 空格直角三角形
    for j in range(1, i + 1):
        print(' ', end='')
    # 倒三角
    for k in range(1, 2 * (bottom_row + 1 - i)):
        if k == 1 or k == 2 * (bottom_row + 1 - i) - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
