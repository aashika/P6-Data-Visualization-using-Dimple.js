import pandas as pd

passengerinfo_file='C:/Users/Aashika/Desktop/DA Udacity/titanic_data.csv'
passengerinfo = pd.read_csv(passengerinfo_file)
passengerinfo.head()




##Number of passengers who are not travelling alone

not_alone = (passengerinfo[(passengerinfo['SibSp']>0) | (passengerinfo['Parch']>0)])

##Number of passengers who are travelling alone

alone = (passengerinfo[(passengerinfo['SibSp']==0) & (passengerinfo['Parch']==0)])

not_alone_survived = (passengerinfo[((passengerinfo['SibSp']>0) | (passengerinfo['Parch']>0)) & passengerinfo['Survived']])
alone_survived = (passengerinfo[((passengerinfo['SibSp']==0) & (passengerinfo['Parch']==0)) & passengerinfo['Survived']])

##Percentages of passengers who are travelling alone/are not travelling alone who survived/did not survive

percent_not_alone_survived = len(not_alone_survived)* 1.0/len(not_alone)*100
percent_alone_survived = len(alone_survived)* 1.0/len(alone)*100

print '{} = {}'.format('percent_not_alone_survived', percent_not_alone_survived)
print '{} = {}'.format('percent_alone_survived', percent_alone_survived)