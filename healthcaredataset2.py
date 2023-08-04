import pandas as pd
import numpy as np
import random

#list of problem

problem =[
    "Influenza", "Eczema", "Diabetes", "Hyperthyroidism", "Migraine",
    "Liver Cancer", "Rheumatoid Arthritis", "Stroke", "Dengue Fever", "Asthma", "Bronchitis",
    "Urinary Tract Infection", "Hypertensive Heart Disease", "Gastroenteritis", "Psoriasis",
    "Tuberculosis", "Chickenpox", "Eating Disorders (Anorexia, Bulimia)", "Autism Spectrum Disorder (ASD)",
    "Cerebral Palsy"
]

#generating random data set

sample_num=700
dataset = {
    'Problem': random.choices(problem, k=sample_num),
    'Fever':np.random.choice([np.nan, *range(95,105)], size=sample_num),
    'Cough':np.random.choice([True, False,np.nan], size=sample_num),
    'Fatigue':np.random.choice([True,False,np.nan], size=sample_num),
    'Breathing Problem':np.random.choice([True,False,np.nan],size=sample_num),
    'Age':np.random.choice([np.nan, *range(18,81)],size=sample_num),
    'Sex':np.random.choice(["Male","Female",np.nan],size=sample_num),
    'SBP':np.random.choice([np.nan, *range(90,161)],size=sample_num),
    'DBP':np.random.choice([np.nan,*range(60,101)],size = sample_num),
    'Cholesterol':np.random.choice([np.nan,*range(120,241)],size=sample_num)
}
#coverting it into dataframe

df=pd.DataFrame(dataset)

#save this to csv file
df.to_csv("C:/Users/yashp/Downloads/healthcare_dataset2.csv",index=False)
print("Dummy dataset saved to 'healthcare_dataset.csv")
