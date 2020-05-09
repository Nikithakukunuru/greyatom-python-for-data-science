# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census=np.concatenate([data,new_record])
#print(data.shape)
#print(census.shape)

age=np.array(census[:,0])
#print(age.shape)
max_age=max(age)
min_age=min(age)
#print(max_age)
#print(min_age)
age_mean=age.mean().round(2)
#print(age_mean)
age_std=age.std().round(2)
#print(age_std)
race_0=np.array(census[:,2][census[:,2]==0])

race_1=np.array(census[:,2][census[:,2]==1])
race_2=np.array(census[:,2][census[:,2]==2])
race_3=np.array(census[:,2][census[:,2]==3])
race_4=np.array(census[:,2][census[:,2]==4])
#print(race_4.shape)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

if(min(len_0,len_1,len_2,len_3,len_4)==len_0):
    minority_race=0
elif(min(len_0,len_1,len_2,len_3,len_4)==len_1):
    minority_race=1
elif(min(len_0,len_1,len_2,len_3,len_4)==len_2):
    minority_race=2
elif(min(len_0,len_1,len_2,len_3,len_4)==len_3):
    minority_race=3
else:
    minority_race=4
#print(minority_race)
senior_citizens=np.array(census[census[:,0]>60])
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours.round(2))
high=np.array(census[census[:,1]>10])
low=np.array(census[census[:,1]<=10])
avg_pay_high=(np.mean(high[:,7])).round(2)
avg_pay_low=(np.mean(low[:,7])).round(2)
print(avg_pay_high)
print(avg_pay_low)




