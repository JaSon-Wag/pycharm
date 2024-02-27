def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            # 字符串的劈分操作
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    question = input('HI,XXX小主,小蜜在此等主人很久了,有什么烦恼和小蜜说说吧:')
    while True:
        if question == 'bye':
            break
        else:
            # 开始查找要回复的答案
            reply = find_answer(question)
            if reply == False:
                question = input('小蜜不知道你在说什么，您可以问我一些关于订单、物流、支付、账户方面的问题，退出请输入bye:')
            else:
                print(reply)
                question = input('小主，您可以问我一些关于订单、物流、支付、账户方面的问题，退出请输入bye:')
    print('小主再见！')
