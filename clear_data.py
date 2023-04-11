import pandas as pd
import os

names=os.listdir(r'D:\vscode\susu\susu\susu\old_lsj')
names.sort(reverse=True)
print(names)

for name in names:
    if name.endswith('.csv'):
        weather_data= pd.read_csv(r'D:\vscode\susu\susu\susu\old_lsj\\'+ name)
        weather_data.columns= weather_data.iloc[0]
        weather_data= weather_data.drop(weather_data.index[0])
        # print(weather_data)
        # weather_data.columns('')
        # print(weather_data.columns)
        weather_data.set_index('日期',inplace=True)
        # print(weather_data.index)
        weather_data.loc[:,'最低气温']= weather_data['最低气温/最高气温'].str[:2].str.replace('[\W]','').astype(int)
        weather_data.loc[:,'最高气温']= weather_data['最低气温/最高气温'].str[-4:].str.replace('[\W]','').astype(int)
        weather_data.drop(['最低气温/最高气温'],axis= 1,inplace=True)
        # print(weather_data.loc[:,'最高气温'])
        # print(weather_data)
        # print(weather_data['最高气温'].sort_values(ascending=True))
        weather_data.to_csv(f'./lsj/new_{name}')

#         # break
# weather_data= pd.read_csv(r'D:\vscode\susu\susu\susu\冷水江历史天气预报 2015年12月份.csv')
# weather_data.columns= weather_data.iloc[0]
# weather_data= weather_data.drop(weather_data.index[0])
# # print(weather_data)
# # weather_data.columns('')
# # print(weather_data.columns)
# weather_data.set_index('日期',inplace=True)
# # print(weather_data.index)
# weather_data.loc[:,'最低气温']= weather_data['最低气温/最高气温'].str[:2].str.replace('[\W]','').astype(int)
# weather_data.loc[:,'最高气温']= weather_data['最低气温/最高气温'].str[-4:].str.replace('[\W]','').astype(int)
# weather_data.drop(['最低气温/最高气温'],axis= 1,inplace=True)
# # print(weather_data.loc[:,'最高气温'])
# print(weather_data)
# # print(weather_data['最高气温'].sort_values(ascending=True))
# # weather_data.to_csv(f'./lsj/new_{name}')