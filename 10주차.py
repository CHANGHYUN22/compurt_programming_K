import pandas as pd
columns = ['임신', 'A', 'B', 'C', 'D', 'E', 'F', 'G', '9', '0']
df = pd.read_csv("./data/08_pima-indians-diabetes.data.csv", names = columns)
df.describe().to_csv('./results/describe.csv')
df_2 = df[['임신', 'A']]
print(df_2.to_csv('./results/임신.csv'))
