import pandas as pd
import numpy as np
from openpyxl.chart.data_source import Level

#reading the saved healthcare dataset

healthdataset = pd.read_csv("C:/Users/yashp/Downloads/combined_dataset.csv")

#Data Analysis

#print the data
print(healthdataset)

#Decribing our data
print(healthdataset.describe())

#counting null values
null_counts = healthdataset.isnull().sum()
print(null_counts)

#percent of null count
total_rows = healthdataset.shape[0]
null_percentcount = (null_counts/total_rows) *100
print(null_percentcount)

#as we can see that we have less null percent of columns fever, age,SBP, DBP and Cholesterol level
#and cough, fatigue, difficulty breathing and gender has high percent of null

# as we now we replace numerical null values with mean/median and categorical values with mode
# so we replace fever, age,SBP , DBP and Cholesterol level with mean because our dataset is not ordered
# Convert the dictionary to a DataFrame
healthdatasets = pd.DataFrame(healthdataset)
healthdatasets['Fever']=healthdatasets['Fever'].fillna(healthdatasets['Fever'].mean())
healthdatasets['Age']=healthdatasets['Age'].fillna(healthdatasets['Age'].mean())
healthdatasets['Systolic Blood Pressure']=healthdatasets['Systolic Blood Pressure'].fillna(healthdatasets['Systolic Blood Pressure'].mean())
healthdatasets['Diastolic Blood Pressure']=healthdatasets['Diastolic Blood Pressure'].fillna(healthdatasets['Diastolic Blood Pressure'].mean())
healthdatasets['Cholesterol Level']=healthdatasets['Cholesterol Level']. fillna(healthdatasets['Cholesterol Level'].mean())

#now we replace categorical null values like cough , fatigue, diifulty breathing and gender with mode

healthdatasets['Cough']=healthdatasets['Cough'].fillna(healthdatasets['Cough'].mode()[0])
healthdatasets['Fatigue']=healthdatasets['Fatigue'].fillna(healthdatasets['Fatigue'].mode()[0])
healthdatasets['Difficulty Breathing']=healthdatasets['Difficulty Breathing'].fillna(healthdatasets['Difficulty Breathing'].mode()[0])
healthdatasets['Gender']=healthdatasets['Gender'].fillna(healthdatasets['Gender'].mode()[0])

null_count= healthdatasets.isnull().sum()
print(null_count)

#healthdatasets.to_csv("C:/Users/yashp/Downloads/no_null_dataset.csv")

print(healthdatasets['Fever'].describe())
print(healthdatasets['Age'].describe())
print(healthdatasets['Systolic Blood Pressure'].describe())
print(healthdatasets['Diastolic Blood Pressure'].describe())
print(healthdatasets['Cholesterol Level'].describe())

# as from the statistics we can say that fever has less scatter of data , and Age, SBP , DBP and Cholesterol level has more scattered data

import matplotlib.pyplot as plt
import seaborn as sns

# giving style to our graph layout
sns.set(style="whitegrid")

#creating a histogram for all the fields for which we get SD high so that w can see the distribution of data

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
sns.histplot(healthdatasets,x="Age",kde=True)
plt.title("Age Distribution")

plt.subplot(2,2,2)
sns.histplot(healthdatasets,x="Systolic Blood Pressure", kde=True)
plt.title("SBP Distribution")

plt.subplot(2,2,3)
sns.histplot(healthdatasets,x="Diastolic Blood Pressure", kde=True)
plt.title("DBP Distribution")

plt.subplot(2,2,4)
sns.histplot(healthdatasets,x="Cholesterol Level", kde=True)
plt.title("Cholesterol Level Distribution")

plt.tight_layout()
plt.show()

#after seeing the distribution of data . now we have to see the outliers
#but because i have created random data by giving the range so there is no outlier in this dataset .
# but i will provide the code to check the outliers with the help of box plot

plt.figure(figsize=(8,8))

plt.subplot(2,2,1)
sns.boxplot(healthdatasets,y="Age")
plt.title("Age")
plt.ylabel("Age")

plt.subplot(2,2,2)
sns.boxplot(healthdatasets,y="Systolic Blood Pressure")
plt.title("SBP")

plt.subplot(2,2,3)
sns.boxplot(healthdatasets,y="Diastolic Blood Pressure")
plt.title("DBP")

plt.subplot(2,2,4)
sns.boxplot(healthdatasets,y="Cholesterol Level")
plt.title("Cholesterol Level")

plt.show()

#there is no outlier as i mention above the reason. But if there is a outlier then we treat it by imputing values or
# removing that columns

#now the next step is data transformation
#so first we do one hot encoing for Gender column it will automatically assign code to male and female
# Assuming healthdatasets is your DataFrame

# Perform encoding for Gender Column and make a new column for it
# Define the mapping for encoding 'Gender'
gender_mapping = {'Male': 1, 'Female': 0}

# Apply the mapping to the 'Gender' column
healthdatasets['Gender_Encoding'] = healthdatasets['Gender'].map(gender_mapping)

# now we have to do make bins for the age columns
# Define the age bins and corresponding labels
age_bins = [18,20, 30, 40, 60, 82]
age_labels = ['Teen', 'Young Adult', 'Adult', 'Middle Aged', 'Old']

# Create a new column 'Age_Category' with the categorized age labels
healthdatasets['Age_Category'] = pd.cut(healthdatasets['Age'], bins=age_bins, labels=age_labels, right=False)
#pd.cut = This is a function provided by the pandas library that is used to create categorical bins based on a given numerical column.
# Print the modified dataset to verify the changes
print(healthdatasets)

# after this data transformation the next step comes is  Feature Engineering

# so now we have to create a new feature like Blood Pressure in the form SBP / DBP
# Define the conditions and corresponding categories
conditions = [
    (healthdatasets['Systolic Blood Pressure'] < 120) & (healthdatasets['Diastolic Blood Pressure'] < 80),
    ((healthdatasets['Systolic Blood Pressure'] >= 120) & (healthdatasets['Systolic Blood Pressure'] <= 129)) &
    (healthdatasets['Diastolic Blood Pressure'] < 80),
    ((healthdatasets['Systolic Blood Pressure'] >= 130) & (healthdatasets['Systolic Blood Pressure'] <= 139)) &
    ((healthdatasets['Diastolic Blood Pressure'] >= 80) & (healthdatasets['Diastolic Blood Pressure'] <= 89)),
    ((healthdatasets['Systolic Blood Pressure'] >= 140) & (healthdatasets['Diastolic Blood Pressure'] >= 90)),
    ((healthdatasets['Systolic Blood Pressure'] >= 140) & (healthdatasets['Diastolic Blood Pressure'] >= 120))
]

choices = ['Normal', 'Elevated', 'Higher Blood Pressure Stage 1', 'High Blood Pressure Stage 2', 'Hypertensive Crisis']

# Create the 'Blood Pressure Category' column
healthdatasets['Blood Pressure Category'] = np.select(conditions, choices, default='Wrong reading')

# Print the modified dataset
print(healthdatasets)

healthdatasets.to_csv("C:/Users/yashp/Downloads/Prepared dataset.csv")

#now after doing preprocessing, tranformation and feature engineering our next step is to do Visulatisation and Machine Learning and Deep Learning
