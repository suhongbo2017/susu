'''
字典与列表的嵌套查找
先要确认该变量的type,如果不是dic，可以用json.loads(str)把变量变成dic.
对这种嵌套类型的分析最重要的是要清楚层级。

如果您的字典中有一个列表，该列表包含多个字典，则可以使用以下代码访问列表中的第一个字典的第一个元素：

my_dict = {'my_list': [{'key': 'value'}, {'key2': 'value2'}]}
print(my_dict['my_list'][0]['key'])
输出结果为：value

如果您想访问列表中的第二个字典的第二个元素，则可以使用以下代码：

my_dict = {'my_list': [{'key': 'value'}, {'key2': 'value2'}]}
print(my_dict['my_list'][1]['key2'])
输出结果为：value2

'''
info= {'status': '1', 'count': '1', 'info': 'OK', 'infocode': '10000', 'lives': [{'province': '湖南', 'city': '冷水江市', 'adcode': '431381', 'weather': '雾', 'temperature': '18', 'winddirection': '西', 'windpower': '≤3', 'humidity': '72', 'reporttime': '2023-04-01 09:48:59', 'temperature_float': '18.0', 'humidity_float': '72.0'}]}
print(type(info))
# 我需要取到'city'的那条数据：
print(info['lives'][0]['city'])
