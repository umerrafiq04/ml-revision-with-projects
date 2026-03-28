# 🎯 Ad Click Prediction System (CTR Prediction using Random Forest)

## 📌 Overview

This project builds an **end-to-end Machine Learning system** to predict whether a user will click on an advertisement (**Click-Through Rate prediction**).

The model uses **Random Forest with hyperparameter tuning** and includes a complete pipeline:

* Data preprocessing
* Feature engineering
* Model training
* Evaluation
* Prediction system

---

## 🚀 Problem Statement

Given user behavior, device details, and ad information:

👉 Predict whether a user will **click (1)** or **not click (0)** an advertisement.

---

## 📊 Dataset Features

| Feature          | Description                         |
| ---------------- | ----------------------------------- |
| age              | User age                            |
| gender           | User gender                         |
| device_type      | Device used (Mobile/Desktop/Tablet) |
| ad_position      | Ad placement (Top/Side/etc.)        |
| browsing_history | User interest category              |
| time_of_day      | Morning/Afternoon/Evening/Night     |
| click            | Target variable (0/1)               |

---

## ⚙️ Project Pipeline

### 1. 🧹 Data Preprocessing

* Removed irrelevant columns (`id`, `full_name`)
* Handled missing values:

  * Numerical → Median imputation
  * Categorical → "Unknown"

---

### 2. 🧠 Feature Engineering

* Age grouping (`young`, `adult`, `senior`)
* Interaction features:

  * `device_type + ad_position`
  * `age * device_type`
* Time encoding (Morning → 0, Night → 3)
* One-hot encoding for categorical variables

---

### 3. 🤖 Model Training

* Algorithm: **Random Forest Classifier**
* Hyperparameter tuning using **RandomizedSearchCV**

```python
params = {
    'n_estimators': [200, 300, 500],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
```

---

### 4. 📈 Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

👉 Achieved performance:

* Accuracy: ~0.71
* F1 Score: ~0.80
* ROC-AUC: ~0.74

---

## 🔍 Key Insights

* Model performs well in identifying clicks (**high recall**)
* Device + Ad position plays an important role
* CTR datasets are highly **imbalanced**, requiring careful evaluation

---

## 💾 Model Saving

The following components are saved:

* `model.pkl` → Trained Random Forest model
* `columns.pkl` → Feature columns
* `age_median.pkl` → Median value for preprocessing

---

## 🎯 Prediction System

The project includes a prediction pipeline that:

1. Takes raw user input
2. Applies preprocessing + feature engineering
3. Aligns features with training data
4. Outputs:

   * Click probability
   * Final prediction (0/1)

---

### 🧪 Example Prediction

```python
sample = {
    "age": 22,
    "gender": "Male",
    "device_type": "Desktop",
    "ad_position": "Top",
    "browsing_history": "Shopping",
    "time_of_day": "Afternoon"
}
```

Output:

```
Probability: 0.78
Prediction: 1 (Click)
```

---

## 🏗️ Project Structure

```
ctr_prediction/
│
├── data/
├── notebooks/
├── model.pkl
├── columns.pkl
├── age_median.pkl
├── train.py
├── predict.py
└── README.md
```

