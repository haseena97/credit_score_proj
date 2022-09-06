import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import	KMeans
import seaborn as sns
# Kmeans on University Data set 
Univ1 = pd.read_excel("C:/Users/Acer/Desktop/Data Analytics/Python for Analytics (Advance)/Python for Analytics (Advanced)/Day 5/absolute.xlsx")
Univ1 = Univ1[Univ1["Lifetime"] > 100]
Univ1.describe()
Univ = Univ1[['retailer_names','MonetaryValue', 'Frequency', 'Recency','Lifetime']]
Univ_num = Univ1[['MonetaryValue', 'Frequency', 'Recency','Lifetime']]
Univ_num.Recency.describe()
for i in df_norm.columns:
    plt.hist(df_norm[i])
    plt.title(i)
    plt.show()
    

# Normalized data frame (considering the numerical part of data)
## Function to check skewness
def check_skew(df_skew, column):
    skew = stats.skew(df_skew[column])
    skewtest = stats.skewtest(df_skew[column])
    plt.title('Distribution of ' + column)
    sns.distplot(df_skew[column])
    print("{}'s: Skew: {}, : {}".format(column, skew, skewtest))
    return
#Removing Skewness
df_rfm_log = np.log(Univ_num)
plt.figure(figsize=(9, 9))
plt.subplot(4, 1, 1)
check_skew(df_rfm_log,'Recency')
plt.subplot(4, 1, 2)
check_skew(df_rfm_log,'Frequency')
plt.subplot(4, 1, 3)
check_skew(df_rfm_log,'MonetaryValue')
plt.subplot(4, 1, 4)
check_skew(df_rfm_log,'Lifetime')
plt.tight_layout()

# scale data
scaler = StandardScaler()
scaler.fit(df_rfm_log)
df_norm= scaler.transform(df_rfm_log)
###### scree plot or elbow curve ############
TWSS = []
k = list(range(2,9))
# iteration cluster 1 sampai 9 nak fitkan dalam data
for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)

TWSS
# Scree plot (elbow curve)
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 4 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 5)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
Univ['clust'] = mb # creating a  new column and assigning it to new column 

Univ = Univ.iloc[:, [5,0,1,2,3,4]]
Univ.head()
# kira start dari yg ada value je sampai (hujung column+1)
Univ.iloc[:, 2:5].groupby(Univ.clust).mean()

Univ.to_csv("Kmeans_university.csv", encoding="utf-8")
Univ.columns


# barplot
import seaborn as sns
sns.countplot(x="clust", data=Univ)
plt.show()
# KIRA SETIAP CLUSTER ADA BRAPA NEGARA
Univ.clust.value_counts()
# Joint Plot ikut cluster untuk numerical variable je
plt.figure(figsize=(30,25))
grouped_Univ = Univ[['retailer_names', 'MonetaryValue', 'Frequency', 'Recency',
       'Lifetime','clust']].groupby('clust').mean()
axes = grouped_Univ.plot.bar(subplots=True)
plt.show()

# Profiling all features together
grouped_Univ.plot(kind='bar', colormap='Accent')    
grouped_Univ.plot(kind='bar',logy=True, colormap='Accent')    
plt.show()

Univ.loc[Univ['clust'] == 3,'clust'] ='01. high engagement & high value'
Univ.loc[Univ['clust'] == 4,'clust'] ='02. high engagement & low value'
Univ.loc[Univ['clust'] == 2,'clust'] ='03. recent activity & low frequency	'
Univ.loc[Univ['clust'] == 1,'clust'] ='04. old activity & high frequency'
Univ.loc[Univ['clust'] == 0,'clust'] ='05. low engagement & low value	'

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('segment.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
Univ.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()