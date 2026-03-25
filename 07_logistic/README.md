#  Customer Segmentation Engine (Marketing AI)

##  Overview

This project builds an **end-to-end machine learning system** to segment customers into **High Value, Medium Value, and Low Value groups** using **RFM (Recency, Frequency, Monetary) analysis** and **Multinomial Logistic Regression**.

It simulates a real-world marketing analytics pipeline where businesses can:

* Target high-value customers for premium campaigns
* Identify low-value users for retention strategies
* Make **data-driven decisions using probability-based predictions**

---

##  Key Features

* 📊 Complete ML pipeline (data → preprocessing → feature engineering → modeling → evaluation)
* 🧮 Industry-standard **RFM segmentation**
* 🤖 Multiclass classification using Logistic Regression
* ⚙️ **Hyperparameter tuning using GridSearchCV**
* 📈 Strong evaluation using F1-score, precision, recall
* 🔍 Model interpretability via coefficients
* 🎯 Probability-based predictions (`predict_proba`)
* 🚀 Ready for deployment (API / dashboard)

---

## 📂 Dataset

* **Name:** Online Retail Dataset
* **Source:** Kaggle
* **Link:** https://www.kaggle.com/datasets/carrie1/ecommerce-data

###  Dataset Description

The dataset contains transactional data of an online retail store:

| Column      | Description                |
| ----------- | -------------------------- |
| InvoiceNo   | Transaction ID             |
| StockCode   | Product code               |
| Description | Product name               |
| Quantity    | Number of items purchased  |
| InvoiceDate | Date of transaction        |
| UnitPrice   | Price per item             |
| CustomerID  | Unique customer identifier |
| Country     | Customer location          |

---

##  Data Preprocessing

* Removed missing `CustomerID`
* Removed cancelled transactions (InvoiceNo starting with 'C')
* Filtered out invalid entries (negative/zero values)
* Converted `InvoiceDate` to datetime format
* Created `TotalPrice = Quantity × UnitPrice`

---

##  Feature Engineering (RFM)

### RFM Metrics:

* **Recency:** Days since last purchase
* **Frequency:** Number of transactions
* **Monetary:** Total spending

### Segmentation Strategy:

* Quantile-based scoring (R, F, M)
* Combined into RFM score
* Final segments:

  * 🟢 High Value
  * 🟡 Medium Value
  * 🔴 Low Value

---

##  Model

* **Algorithm:** Multinomial Logistic Regression
* **Solver:** lbfgs
* **Scaling:** StandardScaler
* **Optimization:** GridSearchCV for hyperparameter tuning

---

##  Model Performance (After Tuning)

| Metric      | Score    |
| ----------- | -------- |
| Accuracy    | **89%**  |
| Macro F1    | **0.90** |
| Weighted F1 | **0.89** |

### Class-wise Performance:

* **High Value:** Precision 0.91 | Recall 0.89 | F1 0.90
* **Medium Value:** Precision 0.87 | Recall 0.88 | F1 0.87
* **Low Value:** Precision 0.92 | Recall 0.92 | F1 0.92

---

##  Key Improvements

* Applied **GridSearchCV** to tune regularization strength
* Improved class balance and overall performance
* Reduced misclassification in **Low Value segment**
* Achieved **~3% improvement in F1-score**

---

## 🔍 Model Interpretation

* Positive coefficient → increases likelihood of a class
* Negative coefficient → decreases likelihood

### Key Insights:

* Higher **Monetary value** strongly indicates High Value customers
* Higher **Recency** (long inactivity) reduces customer value
* Medium segment shows overlap (expected in real-world data)

---

##  Sample Prediction

```python
predict_customer(10, 20, 15000)
```

**Output:**

```
Predicted Segment: High Value
Probabilities:
High Value: 0.85
Medium Value: 0.10
Low Value: 0.05
```

---

##  Business Impact

* 🎯 Enables targeted marketing strategies
* 📉 Helps identify churn-risk customers
* 📊 Improves ROI by segment-based decision making
* 💡 Provides interpretable insights for stakeholders

---

##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib

---

## 📁 Project Structure

```
├── data/
│   └── data.csv
├── notebooks/
│   └── main.ipynb
├── requirements.txt
└── README.md
```


## 🧑‍💻 Author

**Umer Rafiq**

* BTech CSE Student


---
