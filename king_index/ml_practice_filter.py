import pandas as pd
df_01 = pd.read_excel('./data/日常消费品.xls')
df_01.columns = ['id',
                 'name',
                 'publish_date',
                 'roe_17',
                 'roe_18',
                 'roe_19',
                 'apl_18',
                 'apl_19']
# Expected life is proportional to existing life span.
df_01 = df_01[df_01['publish_date'] < '2017-01-01']

# Don't invest company with incomplete data.
df_01 = df_01[pd.to_numeric(df_01['roe_17'], errors='coerce').notnull()]
df_01 = df_01[pd.to_numeric(df_01['roe_18'], errors='coerce').notnull()]
df_01 = df_01[pd.to_numeric(df_01['roe_19'], errors='coerce').notnull()]
df_01 = df_01[pd.to_numeric(df_01['apl_18'], errors='coerce').notnull()]
df_01 = df_01[pd.to_numeric(df_01['apl_19'], errors='coerce').notnull()]

df_01['roe_17'] = pd.to_numeric(df_01['roe_17'])
df_01['roe_18'] = pd.to_numeric(df_01['roe_18'])
df_01['roe_19'] = pd.to_numeric(df_01['roe_19'])
df_01['apl_18'] = pd.to_numeric(df_01['apl_18'])
df_01['apl_19'] = pd.to_numeric(df_01['apl_19'])

# roe great than 5% during 2017~2019
df_01 = df_01[df_01['roe_17'] >8]
df_01 = df_01[df_01['roe_18'] >8]
df_01 = df_01[df_01['roe_19'] >8]
df_01.to_excel("./data/filtered_stocks.xlsx")


