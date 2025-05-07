import pandas as pd
import datacmp

df = pd.read_csv('data/Students_Grading_Dataset.csv')
print(df.head())

print(datacmp.get_detailed(df))

df['Missing_Parent_Ed'] = df['Parent_Education_Level'].isna()
df.groupby('Missing_Parent_Ed')['Total_Score'].mean()

df['Parent_Education_Level'].fillna('Missing', inplace=True)

print(df.describe())
print(df.columns)

df = df.drop(['Student_ID', 'First_Name', 'Last_Name', 'Email'], axis=1)
df = df.drop_duplicates()

print(datacmp.get_detailed(df))

df.to_csv("data/cleaned_data.csv", index=False)
