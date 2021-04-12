import csv
import math

f=open('std_deviation.csv')
read=csv.reader(f)
read=list(read)
data=read[0]
#print(data)

length=len(data)

sum=0
for i in data:
    sum=sum+int(i)

mean=sum/length
print("The mean=",str(mean))

dm=0
dmSq=0
dmSum=0
for i in data:
    dm=int(i)-mean
    print("Dm=",str(dm))
    dmSq=dm**2
    dmSum+=dmSq
    print("Dm square=",str(dmSq),"Dm sum=",str(dmSum))
    total=(dmSum)/length
    sd=math.sqrt(total)
print("The Standard Deviation of following data is: ",str(sd))
