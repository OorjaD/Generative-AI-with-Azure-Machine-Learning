import pandas as pd

data = pd.read_csv('emotions_dataset_large.csv',header=0)
mapp = {0:'sadness',1:'joy',2:'love',3:'anger',4:'fear',5:'surprise'}
data['label_string'] = data['label'].map(mapp)

data.to_csv('emotions_dataset_large_modified.csv')
