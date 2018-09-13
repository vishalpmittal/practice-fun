from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


#
# filename: full path to the file
#
# This routine reads a csv files. Removes rows with missing values
# encode catgorical variables
# and return the data frame
#
def get_dataframe(filename):
    data = pd.read_csv(filename, index_col=0)
    data=data.dropna(axis=0) # drop along rows

    #on hot encode categorical variables
    # we are lisiting two different coding styles for the same
    data['NAME_CONTRACT_TYPE']=(pd.get_dummies(data['NAME_CONTRACT_TYPE']).values).argmax(axis=1)
    data['CODE_GENDER']=(pd.get_dummies(data['CODE_GENDER']).values).argmax(axis=1)
    data['FLAG_OWN_CAR']=(pd.get_dummies(data['FLAG_OWN_CAR']).values).argmax(axis=1)
    data['FLAG_OWN_REALTY']=(pd.get_dummies(data['FLAG_OWN_REALTY']).values).argmax(axis=1)

    colname = ['NAME_TYPE_SUITE',
    'NAME_INCOME_TYPE',
    'NAME_EDUCATION_TYPE',
    'NAME_FAMILY_STATUS',
    'NAME_HOUSING_TYPE',
    'OCCUPATION_TYPE',
    'WEEKDAY_APPR_PROCESS_START',
    'ORGANIZATION_TYPE',
    'FONDKAPREMONT_MODE',
    'HOUSETYPE_MODE',
    'WALLSMATERIAL_MODE',
    'EMERGENCYSTATE_MODE']

    for l in colname:
        data[l] = (pd.get_dummies(data[l]).values).argmax(axis=1)

    return data

data=get_dataframe('c:\\workspace\\homeloan_train.csv')

X = data.loc[:,'NAME_CONTRACT_TYPE':]
y = data.loc[:,'TARGET']

X1_tr, X1_tst, y_tr, y_tst = train_test_split(X,y, shuffle=True, random_state=32, test_size=0.8)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X1_tr, y_tr)
sc=knn.score(X1_tst, y_tst)
print('Scocre ', sc)
#6602516508
# add  code here to
# read application_test.csv
# 2. dropnad along axis=0
# 3. one hot encoding of categorical variables
# 4. predict
# 5. list applications likely to miss payments

print('Hello')