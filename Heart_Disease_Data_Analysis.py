# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:26:37 2019

@author: ritap
"""
#import the packages 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 

#import the data
data = pd.read_csv('heart.csv')

#analize The age data
age_data = data['age']
print("Total Age Data| Count:"+str(len(age_data)))
print("Minimum age:"+str(min(age_data)))
print("Maximum age:"+str(max(age_data)))
print("Average age:"+str(np.mean(age_data)))
print("Median age:"+str(np.median(age_data)))

sorted_age = np.sort(age_data)
plt.figure(0)
plt.hist(age_data, bins = 8)
plt.title('Total Age Data')
plt.xlabel('Age')
plt.ylabel('No. of Person')
plt.show()

true_age_data = data[data.target==1]['age']
print("Diseased Age Data| Count:"+str(len(true_age_data)))
print("Minimum age:"+str(min(true_age_data)))
print("Maximum age:"+str(max(true_age_data)))
print("Average age:"+str(np.mean(true_age_data)))
print("Median age:"+str(np.median(true_age_data)))

sorted_age = np.sort(true_age_data)
plt.figure(1)
plt.hist(true_age_data, bins = 8)
plt.title('Diseased Age Data')
plt.xlabel('Age')
plt.ylabel('No. of Person')
plt.show()

#Analyze sex data 
sex_data = data['sex']
print("Total Sex Data and Diseased Sex Data")
plt.figure(2)
plt.subplot(2,1,1)
plt.hist(sex_data)
plt.title('Total Sex Data')
plt.ylabel('No. of Person')
plt.xticks([0,1],['', ''])

true_sex_data = data[data.target==1]['sex']
plt.subplot(2,1,2)
plt.hist(true_sex_data)
plt.title('Diseased Sex Data')
plt.xlabel('Sex')
plt.ylabel('No. of Person')
plt.xticks([0,1],['Female', 'Male'])
plt.show()

#Analyze cp data 
cp_data = data['cp']
print("Total Chest Pain Data and Diseased Chest Pain Data")
plt.figure(3)
plt.subplot(2,1,1)
plt.hist(cp_data)
plt.title('Total Chest Pain Data')
plt.ylabel('No. of Person')
plt.xticks([0,1, 2, 3],['', '', '', ''])

true_cp_data = data[data.target==1]['cp']
plt.subplot(2,1,2)
plt.hist(true_cp_data)
plt.title('Diseased Chest Pain Data')
plt.xlabel('Chest Pain')
plt.ylabel('No. of Person')
plt.xticks([0, 1, 2, 3])
plt.show()

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
	
    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

#Analyze cp data 
#Plotting a histogram
rbp_data = data['trestbps']
print("Total Blood Pressure Data")
print("Minimum BP:"+str(min(rbp_data)))
print("Maximum BP:"+str(max(rbp_data)))
print("Average BP:"+str(np.mean(rbp_data)))
print("Median BP:"+str(np.median(rbp_data)))
plt.figure(4)
plt.hist(rbp_data, bins=8)
plt.title('Total Resting Blood Pressure Data')
plt.ylabel('No. of Person')
plt.xlabel('Resting Blood Pressure')
plt.show()


true_rbp_data = data[data.target==1]['trestbps']
print("Diseased Resting Blood Pressure Data")
print("Minimum BP:"+str(min(true_rbp_data)))
print("Maximum BP:"+str(max(true_rbp_data)))
print("Average BP:"+str(np.mean(true_rbp_data)))
print("Median BP:"+str(np.median(true_rbp_data)))
plt.figure(5)
plt.hist(true_rbp_data, bins=8)
plt.title('Diseased Resting Blood Pressure Data')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('No. of Person')
plt.show()

#Making a comparison between diseased and non-diseased people's RBP using ECDF
x1, y1 = ecdf(true_rbp_data)
false_rbp_data = data[data.target==0]['trestbps']
x2, y2 = ecdf(false_rbp_data)
plt.figure(6, figsize=(10,7))
plt.scatter(x1, y1, marker='.')
plt.scatter(x2, y2, marker='.')
plt.legend(['Diseased', 'Non-diseased'])
plt.title("Comparison between diseased and non-diseased people's RBP")
plt.xlabel('Resting Blood Pressure')
plt.ylabel('ECDF')
plt.show() 

#Cholesterol analysis
chol_data = data['chol']
print("Total Cholesterol Data")
print("Minimum Cholesterol:"+str(min(chol_data)))
print("Maximum Cholesterol:"+str(max(chol_data)))
print("Average Cholesterol:"+str(np.mean(chol_data)))
print("Median Cholesterol:"+str(np.median(chol_data)))
plt.figure(7)
plt.hist(rbp_data, bins=8)
plt.title('Total Cholesterol Data')
plt.ylabel('No. of Person')
plt.xlabel('Cholesterol')
plt.show()


true_chol_data = data[data.target==1]['chol']
print("Diseased Cholesterol Data")
print("Minimum Cholesterol:"+str(min(true_chol_data)))
print("Maximum Cholesterol:"+str(max(true_chol_data)))
print("Average Cholesterol:"+str(np.mean(true_chol_data)))
print("Median Cholesterol:"+str(np.median(true_chol_data)))
plt.figure(8)
plt.hist(true_rbp_data, bins=8)
plt.title('Diseased Cholesterol Data')
plt.xlabel('Cholesterol')
plt.ylabel('No. of Person')
plt.show()


false_chol_data = data[data.target==0]['chol']
chol_com_data = [true_chol_data, false_chol_data]
plt.figure(8)
plt.boxplot(chol_com_data)
plt.title("Comaring cholesterol for people with heart disease and healthy people")
plt.xticks([1,2], [True, False])
plt.ylabel("Cholesterol")
plt.show()
