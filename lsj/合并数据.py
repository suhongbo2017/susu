import pandas as pd
import os


path= os.chdir('./lsj')
# print(os.getcwdb())
file_list= os.listdir(path)
# print(file_list)

# 调取csv文件，columns设置为：'日期','天气状况','风力风向(夜间/白天)','最低气温','最高气温'，设置变量为concat_weather
concat_weather= pd.read_csv(r'D:\vscode\susu\susu\susu\lsj\concat_weather.csv',names=['日期','天气状况','风力风向(夜间/白天)','最低气温','最高气温'])

# 保存CSV文件。
# concat_weather.to_csv(r'D:\vscode\susu\susu\susu\lsj\concat_weather.csv')

# for循环file_list中后缀是‘月份.csv’的文件concat到concat_weather.csv中。
for file in file_list:
    if file.endswith('月份.csv'):
        
        data= pd.read_csv(file) #读取CSV文件到data

        concat_weather= pd.concat([concat_weather,data],axis=0,join='inner') #按行把data添加到concat_weather变量中。

# 把concat_weather写到CSV文件。(索引为空)
concat_weather.to_csv('concat_weather.csv',index=False)
    



# df_data= pd.read_csv()
