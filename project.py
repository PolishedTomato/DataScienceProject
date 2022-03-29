#Deye Lei
#Deye.Lei76@myhunter.cuny.edu
#Title: Association and prediction of daily corona virus infection with vaccination accumulation. 
#Resources: https://stackoverflow.com/questions/28371674/prevent-scientific-notation-in-matplotlib-pyplot
#https://stackoverflow.com/questions/60252480/how-to-plot-3d-multiple-linear-regression-with-2-features-using-matplotlib
#URL: https://polishedtomato.github.io/DataScienceProject/

from matplotlib import colors
import pandas as pd
import datetime 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

import random

#compute the slope, intercept, correlation of linear regression of xes to yes
def compute_r_line(xes, yes):
    std_x = np.std(xes)#compute std for a list
    std_y = np.std(yes)

    s1 = pd.Series(xes)#create series
    s2 = pd.Series(yes)

    r = s1.corr(s2)
    slope = r*std_y/std_x
    b = yes[0]-slope*xes[0]

    return slope, b, r



#read dataset into dataframe
Corona_count = pd.read_csv('CoronaCountByDate.csv')
vaccine_dose = pd.read_csv('vaccine.csv')

#First graph for daily case count of virus infection since the beginning of the pandamic

#sns.lineplot(x = 'date_of_interest', y = 'CASE_COUNT', data= Corona_count)
pos = ['03/01/2020','04/01/2020','05/01/2020','06/01/2020','07/01/2020','08/01/2020','09/01/2020','10/01/2020','11/01/2020','12/01/2020','01/01/2021','02/01/2021','03/01/2021','04/01/2021','05/01/2021','06/01/2021','07/01/2021','08/01/2021','09/01/2021','10/01/2021']
labels = ['Mar 2020','Apr 2020','May 2020','Jun 2020','Jul 2020','Aug 2020','Sep 2020','Oct 2020','Nov 2020','Dec 2020'
,'Jan 2021','Feb 2021','Mar 2021','Apr 2021','May 2021','Jun 2021','Jul 2021','Aug 2021','Sep 2021','Oct 2021']
#plt.xticks(pos, labels,rotation=45)#rotation rotate the label with 45 degree
#plt.title('CoronaCaseTrend')
#plt.autoscale()
#plt.xlabel('Date')
#fig1 =plt.gcf()#get current figure
#fig1.savefig('CoronaTrendByMonth.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
#plt.show()



#Second graph for cumulative dose1 and 2 since the beginning of the vaccination of NYC
"""
plt.clf()

sns.lineplot(x = 'DATE', y = 'ADMIN_DOSE1_CUMULATIVE', data = vaccine_dose)
sns.lineplot(x = 'DATE', y = 'ADMIN_DOSE2_CUMULATIVE', data = vaccine_dose)
"""
pos1 = ['2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01','2021-06-01','2021-07-01','2021-08-01','2021-09-01','2021-10-01']
labels1 = ['Jan 2021','Feb 2021','Mar 2021','Apr 2021','May 2021','Jun 2021','Jul 2021','Aug 2021','Sep 2021','Oct 2021']
"""
plt.xticks(pos1, labels1, rotation = 45)
plt.yticks([0,1000000,2000000,3000000,4000000,5000000,6000000,7000000],[0,1000000,2000000,3000000,4000000,5000000,6000000,7000000])
plt.ylim(0, 7000000)
plt.ylabel('Number Of Perople Vaccinated')
plt.legend(labels = ['First Dose', 'Second Dose'])
plt.title('Covid-19 Vaccination of NYC')

fig1 =plt.gcf()#get current figure
fig1.savefig('Vaccine_Trend.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()
"""
""""""
#change date formation so two dataframe can merge
vaccine_dose['DATE'] = pd.to_datetime(vaccine_dose['DATE']).dt.strftime('%m/%d/%Y')#change datetime format, Y for four digit, y for two digit in year 

vaccine_Corocase = pd.merge(left= Corona_count, right= vaccine_dose, how = 'inner', left_on='date_of_interest', right_on='DATE')
#take subset of the merged result
vaccine_Corocase = vaccine_Corocase[['date_of_interest','CASE_COUNT','ADMIN_DOSE1_CUMULATIVE','ADMIN_DOSE2_CUMULATIVE']]


#build linear regression for dose1,2 to case_count. Follow code and be use twice by changing ADMIN_DOSE2_CUMULATIVE to ADMIN_DOSE1_CUMULATIVE

plt.clf()
sns.lmplot(x = 'ADMIN_DOSE1_CUMULATIVE', y = 'CASE_COUNT', data = vaccine_Corocase)

plt.xticks([0,1000000,2000000,3000000,4000000,5000000,6000000],[0,1000000,2000000,3000000,4000000,5000000,6000000], rotation = 45)
plt.xlabel('Dose 1 Cumulative')
plt.title('Association of Dose 1 Comulative with Corona Case Count')

#compute the slope, coorelation and intercept
slope, m, r = compute_r_line(vaccine_Corocase['ADMIN_DOSE1_CUMULATIVE'],vaccine_Corocase['CASE_COUNT'])
plt.suptitle(f'Correlation = {round(r,6)}, Slope = {slope:.6f}, Intercept = {m:.2f}')

fig1 =plt.gcf()#get current figure
fig1.savefig('association_Dose1.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()



#build multilinear model
multiLinear = linear_model.LinearRegression()#create linear model
multiLinear.fit(vaccine_Corocase[['ADMIN_DOSE1_CUMULATIVE','ADMIN_DOSE2_CUMULATIVE']], vaccine_Corocase['CASE_COUNT'])

vaccine_Corocase['MultiLinear_Prediction'] = multiLinear.predict(vaccine_Corocase[['ADMIN_DOSE1_CUMULATIVE','ADMIN_DOSE2_CUMULATIVE']])
#get the coefficient and intercept for multi linear model
coefs = multiLinear.coef_
intercept = multiLinear.intercept_

# build the figure instance
#3d graph for two independent variabel
"""
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

#plot actual data of dose1,2 to virus infection in 3d figure
ax.scatter(vaccine_Corocase['ADMIN_DOSE1_CUMULATIVE'], vaccine_Corocase['ADMIN_DOSE2_CUMULATIVE'], vaccine_Corocase['CASE_COUNT'], c='blue', marker='o')

#plot prediction of multi-linear model
ax.plot(vaccine_Corocase['ADMIN_DOSE1_CUMULATIVE'], vaccine_Corocase['ADMIN_DOSE2_CUMULATIVE'], vaccine_Corocase['MultiLinear_Prediction'], c='green',marker = 's')

# set your labels
ax.set_xlabel('Dose 1 Cumulative')
ax.set_ylabel('Dose 2 Cumulative')
ax.set_zlabel('Case Count')

np.set_printoptions(suppress=True)
plt.title('Multi-Linear Regression of Dose_1_Cumulative and Dose_2_Cumulative to Case Count')
plt.xticks([0,1000000,2000000,3000000,4000000,5000000,6000000,7000000],[0,1000000,2000000,3000000,4000000,5000000,6000000,7000000])
plt.yticks([0,1000000,2000000,3000000,4000000,5000000,6000000,7000000],[0,1000000,2000000,3000000,4000000,5000000,6000000,7000000])
plt.suptitle(f'Intercept = {round(intercept,2)}, coefficient of Dose 1 = {round(coefs[0],4)}, coefficient of Dose 2 = {coefs[1]:.6f}')#f'<variable>:.<decimal to keep>f' will suppress the scientific notation
plt.legend(labels=['Multi-Linear regression','Case Count on Dose 1,2 Culmulative'])
fig = plt.gcf()
fig.savefig('MultiLinearRegression.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()
"""

#preparing residual graph
slope1, m1, r1 = compute_r_line(vaccine_Corocase['ADMIN_DOSE1_CUMULATIVE'],vaccine_Corocase['CASE_COUNT'])
slope2, m2, r2 = compute_r_line(vaccine_Corocase['ADMIN_DOSE2_CUMULATIVE'],vaccine_Corocase['CASE_COUNT'])

#adding attributes to existing dataframe
vaccine_Corocase['prediction1'] = vaccine_Corocase['ADMIN_DOSE1_CUMULATIVE'].apply(lambda x : slope1*x +m1)
vaccine_Corocase['prediction2'] = vaccine_Corocase['ADMIN_DOSE2_CUMULATIVE'].apply(lambda x : slope2*x +m2)

vaccine_Corocase['Error1'] = vaccine_Corocase['CASE_COUNT'] - vaccine_Corocase['prediction1']
vaccine_Corocase['Error2'] = vaccine_Corocase['CASE_COUNT'] - vaccine_Corocase['prediction2']

#print(vaccine_Corocase[['date_of_interest','Error1', 'Error2']].head())

pos2 = ['01/01/2021','02/01/2021','03/01/2021','04/01/2021','05/01/2021','06/01/2021','07/01/2021','08/01/2021','09/01/2021','10/01/2021']
labels2 = ['Jan 2021','Feb 2021','Mar 2021','Apr 2021','May 2021','Jun 2021','Jul 2021','Aug 2021','Sep 2021','Oct 2021']

#plot residual graphs, this code was used 2 times for three linear models builded above with some minor change in the code
"""
plt.clf()
sns.scatterplot(x = 'date_of_interest', y = 'Error1', data= vaccine_Corocase)
sns.lineplot(x= 'date_of_interest', y = 0, data= vaccine_Corocase, color = 'red')
plt.xticks(pos2, labels2, rotation = 45)
plt.ylabel('Error')
plt.title('Residual Graph of Dose1 Linear Model Prediction')
fig = plt.gcf()
fig.savefig('ResidualGraph1.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()
"""

#residual graph for multi-linear model
vaccine_Corocase['Error3'] = vaccine_Corocase['CASE_COUNT'] - vaccine_Corocase['MultiLinear_Prediction']
"""
plt.clf()
sns.scatterplot(x = 'date_of_interest', y = 'Error3', data= vaccine_Corocase)
sns.lineplot(x= 'date_of_interest', y = 0, data= vaccine_Corocase, color = 'red')
plt.xticks(pos2, labels2, rotation = 45)
plt.ylabel('Error')
plt.title('Residual Graph of Multi-Linear Model Prediction')
fig = plt.gcf()
fig.savefig('ResidualGraph3.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()
"""


#Graph prediction of multi-linear model
predictx_y = pd.DataFrame(np.arange(0,8800001,10000),columns = ['dose2'])
#0 = c0* dose1 + c1* dose2 + intercept
#-c0*dose1 = c1*dose2 + intercept
# dose1 = (c1*dose2)/-c0 + intercept/-c0 
# dose1 = -1*(intercept/c0) + (c1*dose2)/-c0
predictx_y['dose1'] = predictx_y['dose2'].apply(lambda x : -1*(intercept/coefs[0]) + (coefs[1]*x/(-1*coefs[0])))

#filter dataframe because people have to take dose1 before dose2. Thus, dose2 must have lesser amount than dose1
predictx_y = predictx_y[predictx_y['dose2']<=predictx_y['dose1']]


plt.clf()
plt.ticklabel_format(useOffset=False, style='plain')#turn off scientific notation on axis
Graph = sns.lineplot(x = 'dose2', y = 'dose1', data = predictx_y, color = 'green')
plt.xlabel('Predicted vaccine Dose2 Cumulative')
plt.ylabel('Predicted vaccine Dose1 Cumulative')
plt.title('The Expected Pairs of Dose1 and Dose2 Cumulative to Reach Zero Infection of Coronavirus in NYC based on Multi-Linear Model')
plt.xticks([0,1000000, 2000000,3000000,4000000,5000000,6000000],[0,1000000, 2000000,3000000,4000000,5000000,6000000], rotation = 45)
#plt.yticks([0, 6500000, 6520000, 6540000,6560000,6580000,6600000,6620000],[0, 6500000, 6520000, 6540000,6560000,6580000,6600000,6620000])
fig = plt.gcf()

#ax = plt.gca

fig.savefig('ExpectValue_Pair_Of_Dose12.png', bbox_inches = "tight")#bbox_inches = 'tight' recover the xlabel got cutt off
plt.show()
print(predictx_y[predictx_y['dose2'] == 5470000])
#print(intercept + coefs[0]*6500509 + coefs[1]*470000)#varification