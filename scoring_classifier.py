import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel("C:/Users/Acer/Desktop/Data Analytics/Python for Analytics (Advance)/Python for Analytics (Advanced)/Day 5/final_cluster.xlsx")
df_2.columns
# missing values
df.isnull().sum()
# drop columns
df_2 = df.drop(['Unnamed: 0.1','Unnamed: 0','MonetaryValue', 'Frequency','Recency','Lifetime'], axis=1)
# quick way to separate numeric columns 
df_2.describe().columns
# look at numeric and categorical values separately 
df_num = df_2[['master_order_id', 'order_id', 'ordereditem_quantity',
       'ordereditem_unit_price_net', 'ordereditem_product_id', 'value',
       'bill_amount', 'dummy_name', 'dummy_group', 'invoice_id',
       'created_year', 'created_month', 'created_hour', 'created_dayofweek','created_year_month']]
df_cat = df_2[['created','master_order_status','order_status','prod_names','group','dist_names','retailer_names',
               'CreditScore']]
# How is the distribution for numerical values
# Histograms and boxplots
#distributions for all numeric variables (df_num) --histogram
for i in df_num.columns:
    plt.hist(df_num[i])
    plt.title(i)
    plt.show()
#distributions for all numeric variables (df_num) --boxplot
for i in df_num.columns:
    plt.boxplot(df_num[i])
    plt.title(i)
    plt.show()
# Perhaps we should take the non-normal distributions and consider normalizing them
# Correlation between the metrics 
print(df_num.corr())
sns.heatmap(df_num.corr())

# compare credit score across numerical variables
pd.pivot_table(df_2, index = 'CreditScore', values = ['Age','SibSp','Parch','bill_amount'])