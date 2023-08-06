import pandas as pd

#reading files
df1=pd.read_csv("C:/Users/yashp/Downloads/healthcare_dataset 1.csv")
df2=pd.read_csv("C:/Users/yashp/Downloads/healthcare_dataset2.csv")

#map same columns but different name in both dataset
columns_to_map={
    'Problem':'Diseases',
    'Breathing Problem':'Difficulty Breathing',
    'Sex':"Gender",
    'SBP':'Systolic Blood Pressure',
    'DBP':'Diastolic Blood Pressure',
    'Cholesterol':'Cholesterol Level'
}

df2.rename(columns=columns_to_map,inplace=True)

#combining both data set

df3=pd.concat([df1,df2],ignore_index=True)

#saving data

df3.to_csv("C:/Users/yashp/Downloads/combined_dataset.csv",index=False)

print(df3)