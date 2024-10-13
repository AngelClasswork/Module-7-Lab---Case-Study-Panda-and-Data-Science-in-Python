import pandas as pd

#create
#create from a csv
df = pd.read_csv('telco_churn.csv')

#create from a dictionary
tempdict = {'coll':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf= pd.DataFrame.from_dict(tempdict)

#Read
df.head(10)

dictdf.head()

df.tail()

#2.2 show columns and data types

df.dtypes
#2.3 summary statistics
df.describe()
df.describe(include='object')

#2.4 filtering columns
df.State
df['Internatioal plan']
df[['State', 'International plan']]
df.Churn.unique()

#2.4 filtering rows
df.head()
df[(df['Internatioal plan']=='No') & (df['Churn']==True)]

#2.6 indexing with iloc
df.iloc[14]
df.iloc[14,-1]
df.iloc[22:33]

#2.7 indexing the iloc
state=df.copy
state.set_index('State', inplace=True)
state.head()
state.loc['OH']

#3.1 dropping rows
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

#3.2 dropping columns
df.drop('Area code', axis=1)

#3.3 Creating Calculated coulumns
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
df.head

#3.4 Updating an entire column
df['New Column']=100
df.head

#3.5 Updating a single value
df.iloc[0,-1]=10
df.head

#3.6 condition based updating using apply 
df['Churn Binary']= df['Churn'].apply(lambda x: 1 if x==True else 0)
df.head

#4.1 output to csv
df.to_csv('output.csv')

#4.2 output to JSON
df.to_json()

#4.3 output to HTML
df.to_html()

#4.4 Delete a DataFrame
del df