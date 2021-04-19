
## WorldHackathon Day Apr 2021

This repository is setup for all the challenge hackathon artifacts.

## Problem Statement

Bushfires and floods are the top two natural disasters in Australia. Geographically, bushfires occur mainly in south-eastern Australia, whereas floodsoccur mainly on the eastern coastline. According to the historical disaster data, houses destroyed were higher by disasters from bushfires compared to floods. Inthe years between 1967 and 2013, bushfires cost approximately A$4.7 billion, including deaths and injuries but excluding most indirect losses (link). Royal Commission into National Natural Disaster Arrangements had an inquiry that Australia is not well-prepared for natural disasters.  For several months spanning late 2019 and early 2020, bushfires devastated communities across Australia. One of the most brutal fire seasons in recent memory saw thousands of acres of property burnt, homes destroyed, and lives lost. (link). Post-traumatic stress disorder (PTSD) is the most commonly seen after natural disasters. Approximately 30-40% among direct victims, 10-20% among rescue workers, and 5-10% among the general population experienced PTSD after a natural disaster (link). 

Minderoo foundation (link), a modern philanthropic organisation, aims to build resilience to fires and floods by harnessing the collective power of the communities, industry, and government. We support Noble Minderoo Mission anddevelop ideas that will help build resilient communities through self-awareness and acts of kindness. The organisation is reaching out to the leaders of the communities to build a resilient community (top-down approach). We aim to build awareness and contribution at the individual level to build community resilience (bottom-up).  We are providing an app where each and everyone can register and prepare themselves for disaster and actively give them 
recommendations of acts of kindness they can do at their pace to build Resilient Communities. The power of individuals is immeasurable. For example, a nine-year-old girl started actions to ban plastic straws in her community, and now it has influenced major franchise like Starbucks to use a paper straw instead (link). Both top-down and bottom-up approach will need to be used for effective implementation to build community resilience. 

## Hackathon Solution Highlight
### Recommendation system (Machine Learning)
### Pre-processing
We use ColumnTransformer from scikit-learn where MinMaxScaler is used to normalize each data point. Majority of variables have values 0/1 which makes it a sparse dataset. Two-third of the dataset is split into training and one-third is used for evaluating the model. For deployment all the data is used for model training.
ML Model
We are using Random Forest Classifier which is an ensembled model built on top of decision trees. Since our data majorly consists of categorical variables, we preferred tree algorithm over other classifiers e.g., Nearest Neighbours and SVM etc.
We treat each act as a label independent from other labels which is why a list of models are trained for the data. Number of model estimators and iterations are kept default as per scikit-learn documentation.
Both the ColumnTransformer and the ML model are pipelined for end-to-end training. This makes it easier to get prediction through the API.

### Deployment
Once we have the trained model, we deploy it on localhost through Flask API. For remote tunnelling we are using Ngrok which gives us prediction through all act’s classifier under 2 seconds. Prediction from model can be taken through:
URL : http://c41fe2352ab4.ngrok.io/api/predict

### Future plans
AI model improvements:
<ul>
<li> Once we have a substantial amount of user data our existing generated data will start getting replaced with real user’s data. This will give strength to the model as it will begin finding patterns that affect the act’s we are predicting.</li>
<li>We propose to use collaborative filtering based recommendation engine which can recommend acts based on user’s history and his attributes. We assume that if a user is following a set of acts, he will be interested in another act that is close to his cluster of interest.</li>
<li>We plan to have the option of adding dynamic tasks in our dataset. These new tasks will be recommended to the users with the help of language models like BERT. We can compute semantic similarity between the task sentence and our data so we can place it under the relevant interests categories. For computing similarity, we will be interested in using pre-trained language models.</li>
</ul>

### Future plan of app:
#### Mental health checks:
We would like to add Post-traumatic stress disorder (PTSD) questionnaires (link) in the app for users to do one before the disaster as the baseline. The user can do this test whenever they want, and the app will track the scores longitudinally. When there is a disaster, the user can check their mental health by doing this questionnaire, and the app can notify the user if the score diverts from the past average, which recommends the user to seek professional help. We will need to collaborate with the mental health organisation and disaster management experts to reduce the potential harm and improve clinical relevance.

## How this repository is setup

### appcodebase

    This folder contains a bare minimum working app for iConnect
    
### datascience

    This folder contains scripts and model which team developed during challenge

### projectartifacts

    This folder contains all artifacts developed during team collaboration.


## Contributing Team

Priti Solanki, Neeti Sharma, Anil Kumar Sahoo, Nabeel Raza, Doshagya, Asit Kumar Panda, Mari Takashima, Aviral Pandey
    
## Team Apollo 
### Challenge Category : Health and Wellbeing
### Building resilience communties through act of self-awareness and kindness

Design Members (UI/UX) -  Neeti Sharma <br/>

Subject Matter Experts (SMEs) - Mari Takashima <br/>

Software Engineering Members (Building solution) - Anil Kumar Sahoo, Nabeel Raza, Doshagya Kumar,Asit Kumar Panda, Priti Solanki <br/>

Business Members (Business modelling, financial analysis and validation) - Aviral <br />

Presenters/Media (responsible for delivery of video and presentation elements) -  Aviral + Team <br/>

Project Manager (Keeps the team to schedule) - Mari Takashima <br/>

Team Captain / Representative (Represents the team, acts as a final decision point when there is a conflict) - Priti Solanki <br/>
