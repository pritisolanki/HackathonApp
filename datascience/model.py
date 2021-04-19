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
import random 

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

outdoor_0_acts=['Prepare your emergency kit for flood diaster','Prepare your emergency kit for fire diaster',
               'Create educational material to show impact of disaster impact',
                'Register at flood warning service/ and bureau of meteorology warning service',
                'Check if the house is at risk by looking at the flood map',
                'Make an emergency package','Support startups ideas','Donate local hospitals and well being centres online',
                'Donate plants/tree to school or communitysupport local meetup group'
               ]
data['outdoor']=1
for i in range(data.shape[0]):
    for outdoor_act in outdoor_0_acts:
        if data[outdoor_act].values[i]:
            data['outdoor'].values[i]=0


disaster_history=pd.read_csv('disaster_history_coord.csv')
disaster_history.head(2)
fire_lat_lon=disaster_history[['lat','lon']][disaster_history['cateogory']=='Bushfire']
flood_lat_lon=disaster_history[['lat','lon']][disaster_history['cateogory']=='Flood']
fire_acts=['Prepare your emergency kit for fire diaster','Create educational material to show impact of disaster impact',
          'Make an emergency package']
flood_acts=['Create educational material to show impact of disaster impact',
           'Prepare your emergency kit for fire diaster','Register at flood warning service/ and bureau of meteorology warning service',
           'Check if the house is at risk by looking at the flood map','Make an emergency package']

for i in range(data.shape[0]):
    for fire_act in fire_acts:
        if data[fire_act].values[i]:
            rand_fire_act_ind=np.random.randint(fire_lat_lon.shape[0])
            dec_lat = random.random()/100
            dec_lng = random.random()/100
            data['lat'].values[i]=fire_lat_lon.values[rand_fire_act_ind,0]+dec_lat
            data['lng'].values[i]=fire_lat_lon.values[rand_fire_act_ind,1]+dec_lng
            
    for flood_act in flood_acts:
        if data[flood_act].values[i]:
            rand_flood_act_ind=np.random.randint(flood_lat_lon.shape[0])
            dec_lat = random.random()/100
            dec_lng = random.random()/100
            data['lat'].values[i]=flood_lat_lon.values[rand_flood_act_ind,0]+dec_lat
            data['lng'].values[i]=flood_lat_lon.values[rand_flood_act_ind,1]+dec_lng

            




all_cols=data.columns
input_cols=all_cols[:10]
out_cols=all_cols[10:]
t = [('num', MinMaxScaler(), input_cols)]
col_transform = ColumnTransformer(transformers=t,remainder='passthrough')

### MULTIMODEL TRAINING
model_list=[]
for col in out_cols:
    temp_model = Pipeline(steps=[('transformer', col_transform),
                  ('classifier',RandomForestClassifier(n_estimators=100))
                   #('classifier',KNeighborsClassifier())
                                ])

    X=data.iloc[:,:10]#.astype(np.float32)
    y=data[col].astype(np.uint8)
    Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.0033,random_state=2021)
    temp_model.fit(Xtrain,ytrain)
    model_list.append(temp_model)


X=data.iloc[:,:10]#.astype(np.float32)
y=data.iloc[:,10:].astype(np.uint8)
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.0033,random_state=2021)  
pred_ytest=np.zeros(ytest.shape)
pred_ytrain=np.zeros(ytrain.shape)
for i in range(y.shape[1]):
    pred_ytest[:,i]=model_list[i].predict(Xtest)
    pred_ytrain[:,i]=model_list[i].predict(Xtrain)

print('Hard accuracies')
total=0
correct=0
for i in range(ytrain.shape[0]):
    if (ytrain.values[i,:]==pred_ytrain[i,:]).all():
        correct+=1
    total+=1
print('Training accuracy',100*correct/total)


total=0
correct=0
for i in range(ytest.shape[0]):
    if (ytest.values[i,:]==pred_ytest[i,:]).all():
        correct+=1
    total+=1
print('Test accuracy',100*correct/total)


print('Soft accuracies')
total=0
correct=0
for i in range(ytrain.shape[0]):
    for j in range(ytrain.shape[1]):
        if (ytrain.values[i,j]==pred_ytrain[i,j]):
            correct+=1
        total+=1
print('Training accuracy',100*correct/total)


total=0
correct=0
for i in range(ytest.shape[0]):
    for j in range(ytest.shape[1]):
        if (ytest.values[i,j]==pred_ytest[i,j]):
            correct+=1
        total+=1
print('Test accuracy',100*correct/total)

def MultiModelpredict(name,age,lat,lng,disable,outdoor,preparation,community,local_support,environment,asset_protection):
    
    input_vals=np.array([age,lat,lng,disable,outdoor,preparation,community,local_support,environment,asset_protection])

    df_input=pd.DataFrame(input_vals.reshape(1,-1))
    df_input.columns=input_cols
    transformed_output=np.zeros(len(out_cols))
    transformed_output_probs=np.zeros(len(out_cols))
    for i in range(len(out_cols)):
        transformed_output[i]=np.squeeze(model_list[i].predict(df_input))
        transformed_output_probs[i]=max(np.squeeze(model_list[i].predict_proba(df_input)))

    pred_acts=[]
    confidence=[]
    for i in range(transformed_output.shape[0]):
        if transformed_output[i]:
            pred_acts.append(out_cols[i])
            confidence.append(transformed_output_probs[i])
    return pred_acts,confidence

