import pandas as pd
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, accuracy_score

healthdatasets=pd.read_csv("C:/Users/yashp/Downloads/Prepared dataset.csv")

#selecting features and target variables
features =['Fever','Systolic Blood Pressure','Diastolic Blood Pressure','Cholesterol Level']
target= 'Diseases'

#split this data into features and target
X =healthdatasets[features]
y=healthdatasets[target]

#split the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#applying gradient boosting classifier model
gbc = GradientBoostingClassifier(n_estimators=100, random_state=42)

#train the model
gbc.fit(X_train,y_train)

#make prediction on test data
y_pred =gbc.predict(X_test)

#calculationg accuracy
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# Generate classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)


# as my accuracy is only 5% which is very low because i have created random data, and the size of data is also small
#but i this project is to learn the full process of data analysis and Machine Learning