# Retailer Credit Score Classifier: Project Overview
- Created a tool that estimates credit score of retailers to help manufacturers assess creditworthiness of retailers based on their purchasing behaviour.
- Assessment of creditworthiness is based on RFM values of retailers.
- There are 2 part in this project:
> **Step 1. Clustering:** Cluster the observations into segments of credit score (Excellent, Good, Moderate, Fair, Poor).
>
> **Step 2. Prediction:** Predict credit score of retailers by using output from Step 1. 
- Built a client facing API using flask
- Created a Tableau dashboard on [retailer purchasing habits](https://public.tableau.com/views/rfm_16624639585820/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

## Codes and Resources Used
**Python Version:** Python 3.9<br>
**Packages:** numpy, matplotlib, seaborn, sklearn, xgboost, flask, json, pickle<br>
**RFM Analysis Notebook:** https://www.kaggle.com/code/yaowenling/rfm-customer-segmentation/notebook<br>
**Cluster-then-predict Article:** https://towardsdatascience.com/cluster-then-predict-for-classification-tasks-142fdfdc87d6<br>
**Flask Productionization Github:** https://github.com/PlayingNumbers/ds_salary_proj/tree/master/FlaskAPI<br>
**Flask Productionization Article:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku

## Data
Masked data is obtained from a manufacturing company for my capstone project, so I won't share the dataset.
Overall, with each retailer, we got the following:

- Order ID
- Order Status
- Date
- Item Quantity
- Product Name
- Item Unit Price
- Product ID
- Value
- Location Group
- Distributor Name
- Bill Amount

## Step 1: Clustering 
### Data Cleaning
- Removed rows without price
- Created new column `invoice_id` which is unique to each retailer and the location they perform transactions from
- Exclude `rejected` and `cancelled` orders

### RFM Analysis
I segregated retailers by calculating their Recency, Frequency and Monetary values.
1. Recency : the number of days between maximum date in dataset and the last purchase date of each retailer.
2. Frequency: the number of transactions of each retailer.
3. Monetary : the sum of bill amount of each retailer.
Then I cluster the retailers into 5 credit score groups based on their RFM values using<br> 
K-Means Clustering. Below are a few highlights.
<p float="left">
  <img src="https://user-images.githubusercontent.com/71859510/189015598-aebf67d9-f9b7-4c95-a626-24dcd96eb433.png" width="398" height="238">
  <img src="https://user-images.githubusercontent.com/71859510/189014980-4d64ab52-a08b-4aa3-a1f0-6a0f65e8b344.png" width="498" height="338">
</p>

## Step 2: Prediction
### EDA
I looked at the distributions of the numerical data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.
<p float="left">
  <img src="https://user-images.githubusercontent.com/71859510/189017824-1bcc3db7-1469-4426-9a13-292adb31e631.PNG" width="198" height="138">
  <img src="https://user-images.githubusercontent.com/71859510/189019269-4dadffd5-1120-4dfc-85e7-a658ecebfc32.png" width="98" height="38">
  <img src="https://user-images.githubusercontent.com/71859510/189017447-9136f34d-6060-4b01-b9ae-3fbf499cf71b.png" width="398" height="238">
</p>

![heatmap](https://user-images.githubusercontent.com/71859510/189018249-a14a8087-f9b1-40e8-a630-5ba6f673a5b5.png)

### Model Building
First, I transformed the categorical variables into dummy variables. Then I split the data into train and tests sets with a test size of 30% and scaled them.

I tried five different models and evaluated them using Accuracy Score:
- Decision Tree
- Random Forest
- Naive Bayes
- SVM
- XGBoost

### Model Performance
The XGBoost model outperformed the other approaches on the training and test sets.
![model accuracy](https://user-images.githubusercontent.com/71859510/189018735-96704fb7-638d-4f64-8f84-86b6e9894f78.PNG)

### Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the tutorial in the reference section above. The API endpoint takes in a request with a list of values from a retailer transaction and returns an estimated credit score.






