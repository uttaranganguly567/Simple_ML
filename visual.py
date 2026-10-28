'''
How to display data 
'''
import pandas as pd
import matplotlib.pyplot as plt

def sep():
  print("-"*40)

data={
  "study_hours":[1,2,3,4,5,6,7,8],
  "marks":[35,40,50,65,70,75,80,90]
}

df=pd.DataFrame(data)
print('\n=====Complete DataSet===\n')
print(df)
sep()
x=df['study_hours']
y=df['marks']
plt.scatter(x,y,color='red')
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title('Study Hours VS Marks')

plt.show()
