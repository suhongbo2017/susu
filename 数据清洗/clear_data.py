import pandas as pd

df= pd.read_csv(r'D:\vscode\susu\susu\susu\lsj\concat_weather.csv')
df.set_index('日期',inplace=True,)
df.sort_index(inplace=True)
# print(df)
df.to_csv(r'D:\vscode\susu\susu\susu\数据清洗\concat_weather.csv')
# print(df.loc[:,['最高气温','最低气温']])