import os
import sklearn
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
data=pd.read_csv('fake_dataset (1).csv', engine='python')
duplicates=['','ike','onate books ','alk to elderly','o to framer market','olunteer to a Cause','upport local produce',
            'uy  handmade products','upport startups ideas','ake an emergency package','ttend  community service',
            'elp someone with your skills','ontribute to local communities','ntroduce your self to your neighbours',
            'uy from "nothing group" facebook group','repare your emergency kit for fire diaster',
            'eliver grocery or medications to neighbours','nvitee community member to your celebrations',
            'ake a test to check your wellbeing after disaster','onate local hospitals and well being centres online',
            'heck if the house is at risk by looking at the flood map',
            'egister at flood warning service/ and bureau of meteorology warning service']
for i in range(data.shape[0]):
    temp_list=data['acts'].values[i].split(',')
    for item in temp_list:
        if item in duplicates:
            data['acts'].values[i]=None

data=data.dropna()
acts_list=[]
for i in range(data.shape[0]):
    temp_list=data['acts'].values[i].split(',')
    for item in temp_list:
        if not (item in acts_list):
            acts_list.append(item)

for item in acts_list:
    data[item]=None
for i in range(data.shape[0]):
    temp_list=data['acts'].values[i].split(',')
    for item in acts_list:
        if item in temp_list:
            
            data[item].values[i]=1
        else:
            data[item].values[i]=0

data=data.drop(['acts','name'],axis=1)

all_cols=data.columns
input_cols=all_cols[:10]
out_cols=all_cols[10:]
t = [('num', MinMaxScaler(), input_cols)]
col_transform = ColumnTransformer(transformers=t,remainder='passthrough')
model = Pipeline(steps=[('transformer', col_transform),
                      ('classifier',RandomForestClassifier())])

X=data.iloc[:,:10]#.astype(np.float32)
y=data.iloc[:,10:].astype(np.uint8)

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2)
model.fit(Xtrain,ytrain)

def predict(name,age,lat,lng,disable,outdoor,preparation,community,local_support,environment,asset_protection):
    
    input_vals=np.array([age,lat,lng,disable,outdoor,preparation,community,local_support,environment,asset_protection])

    df_input=pd.DataFrame(input_vals.reshape(1,-1))
    df_input.columns=input_cols
    transformed_output=np.squeeze(model.predict(df_input))
    pred_acts=[]
    for i in range(transformed_output.shape[0]):
        if transformed_output[i]:
            pred_acts.append(out_cols[i])
    return pred_acts