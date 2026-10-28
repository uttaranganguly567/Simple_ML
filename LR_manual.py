'''
LR without any ML algorithm
'''
def sep():
  print("-"*40)

hours=[1,2,3,4,5,6,7,8]
marks=[35,40,50,65,70,75,80,90]

n=len(hours)

mean_x=sum(hours)/n
mean_y=sum(marks)/n

numerator=0
denominator=0

for i in range(n):
  numerator+=((hours[i]-mean_x)*(marks[i]-mean_y))
  denominator+=(hours[i]-mean_x)**2

#LEARN SLOPE AND INTERCEPT

slope=numerator/denominator
intercept=mean_y-slope*mean_x

print("Learned slope:",slope)
print("Learned intercept:",intercept)

sep()

'''
predict marks for 6 hours study
'''

new_hours=int(input('enter study hours....'))

predicted_marks=slope*new_hours+intercept # y=mx+c

print("predicted marks: ",predicted_marks)


