import pandas as pd
import numpy as np
import random

#list of diseases
diseases = [
    "Influenza", "Eczema", "Influenza", "Diabetes", "Hyperthyroidism", "Migraine",
    "Liver Cancer", "Rheumatoid Arthritis", "Stroke", "Dengue Fever", "Asthma", "Bronchitis",
    "Urinary Tract Infection", "Hypertensive Heart Disease", "Gastroenteritis", "Psoriasis",
    "Tuberculosis", "Chickenpox", "Eating Disorders (Anorexia, Bulimia)", "Autism Spectrum Disorder (ASD)",
    "Cerebral Palsy"
]

#generating random dataset
num_samples=500
data = {
    'Diseases': random.choices(diseases, k=num_samples),
    'Fever': np.random.choice([np.nan, *range(95, 110)], size=num_samples),
    'Cough': np.random.choice([True, False, np.nan], size=num_samples),
    'Fatigue': np.random.choice([True, False, np.nan], size=num_samples),
    'Difficulty Breathing': np.random.choice([True, False, np.nan], size=num_samples),
    'Age': np.random.choice([np.nan, *range(18, 81)], size=num_samples),
    'Gender': np.random.choice(["Male", "Female", np.nan], size=num_samples),
    'Systolic Blood Pressure': np.random.choice([np.nan, *range(90, 161)], size=num_samples),
    'Diastolic Blood Pressure': np.random.choice([np.nan, *range(60, 101)], size=num_samples),
    'Cholesterol Level': np.random.choice([np.nan, *range(120, 241)], size=num_samples),
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)


# Save the DataFrame to a CSV file
df.to_csv("C:/Users/yashp/Downloads/healthcare_dataset.csv", index=False)

print("Dummy dataset saved to 'healthcare_dataset.csv'")



