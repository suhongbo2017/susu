import pandas as pd
import matplotlib as plt
import numpy as np

data= pd.read_excel(r'D:\vscode\susu\susu\susu\pandas学习\AMap_adcode_citycode_20210406.xlsx')
df= data.set_index('中文名')
print(df.dtypes)       
print(df.loc['冷水江市',['adcode']])

plt.plot(np.random.randn(50).cumsum())