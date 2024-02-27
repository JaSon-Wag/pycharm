# 创建字典用于存储车票信息，使用车次作key，使用其他信息作value
dict_ticket = {
    'G1569': ['北京南-天津南', '18:06', '18:39', '00:33'],
    'G1567': ['北京南-天津南', '18:15', '18:49', '00:34'],
    'G8917': ['北京南-天津南', '18:20', '19:19', '00:59'],
    'G203': ['北京南-天津南', '18:35', '19:09', '00:34'],
}
print('车次\t出发站-到达站\t出发时间\t到达时间\t历时时间')
# 遍历字典中的元素
for key in dict_ticket.keys():
    print(key, end='\t')
    for item in dict_ticket.get(key):
        print(item, end='\t')
    print()

# 输入用户的购买要求
train_no = input('请输入要购买的车次:')
# 根据key获取值
info = dict_ticket.get(train_no, '车次不存在')
# 判断车次是否存在
if info != '车次不存在':
    person = input('请输入乘车人，如果是多位乘车人使用逗号分隔:')
    # 获取车次的出发站-到达站，还有出发时间
    s = info[0] + ' ' + info[1] + '开'
    print('您已购买了' + train_no + ' ' + s + ',请' + person + '尽快换取纸制车票。【铁路服务】')
else:
    print('对不起，选择的车次可能不存在')
