'''
LR with ML algorithm
'''
import numpy as np
from sklearn.linear_model import LinearRegression
def sep():
  print("-"*40)

#FEATURE: study_hours
X=np.array([
  [1],[2],[3],[4],[5],[6],[7],[8]
])

#TARGET: marks
y=np.array([30,40,50,60,70,80,90,100])

# CREATE The MODLEL

model=LinearRegression()

print('befor training ML model object is ',model)

# Train the Model

model.fit(X,y)

print('after training ML model object is ',model)

#Inspect Learned parameters

print("Coeffiecient: ",model.coef_)
print("Intercept: ",model.intercept_)

#Predict marks for 6.5 hours

new_student=np.array([[6.5]])

#Predict Marks for new data

prediction=model.predict(new_student)

print("Predicted Marks: ",prediction[0])





