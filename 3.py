'''
How to create a dataset using pandas
'''
import pandas as pd

data={
  "study_hours":[1,2,3,4,5,6,7,8],
  "attendance":[50,55,60,65,70,80,85,90],
  "marks":[35,40,50,65,70,75,80,90]
}

df=pd.DataFrame(data)
print('\n=====Complete DataSet===\n')
print(df)


print("\nFirst Five records")
print(df.head())

print("\nLast Five records")
print(df.tail())


print("\nstatistical information")
print(df.describe())

print("\ncolumns information")
print(list(df.columns))

for _ in list(df.columns):
  print(_)

# print(df.info())


