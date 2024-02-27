def read(name):
    new = []
    with open(name, 'r', encoding='utf-8-sig') as file:
        for sub in file.readlines():
            if sub[0] not in list('\n0123456789') and sub[-2] not in list('0123456789'):
                new.append(sub)
    new = [ele.strip() for ele in new]
    return new


def write(name, new, n):
    with open(name, 'a', encoding='utf-8') as file:
        file.write(f"{name.split('_')[0]}e{n}\n")
        for item in new:
            file.write(item + '\n')


if __name__ == '__main__':
    m = eval(input('请输入第几季:'))
    n = eval(input('请输入该季共有多少集:'))
    for i in range(1, n + 1):
        new = read(f'{i}.txt')
        write(f's{m}_new.txt', new, i)
