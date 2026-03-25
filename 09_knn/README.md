# 🚗 Ride Fare Prediction using KNN (Machine Learning Project)

##  Overview

This project predicts taxi ride fares based on trip details such as distance, time, and passenger count using the **K-Nearest Neighbors (KNN)** algorithm.

The goal is to simulate a real-world ride fare estimation system like Uber/Ola while demonstrating strong machine learning fundamentals.

---

##  Problem Statement

Given ride details:

* Pickup & drop coordinates
* Time of ride
* Passenger count

 Predict the **fare amount** accurately.

---

##  Dataset

* NYC Taxi Fare Dataset (sampled / reduced size)
* Features include:

  * `pickup_datetime`
  * `pickup_longitude`, `pickup_latitude`
  * `dropoff_longitude`, `dropoff_latitude`
  * `passenger_count`
  * `fare_amount` (target)

---

##  Project Workflow

### 1. Data Preprocessing

* Removed missing values
* Filtered invalid fares (≤ 0)
* Removed zero coordinates (0,0)
* Removed same pickup & drop locations
* Handled outliers (fare & distance)

---

### 2. Feature Engineering

* Calculated **distance (Haversine formula)** 
* Extracted time-based features:

  * Hour
  * Day
  * Month
  * Day of week
  * Weekend flag

---

### 3. Exploratory Data Analysis (EDA)

* Fare distribution visualization
* Distance vs Fare relationship
* Passenger count analysis
* Time-based fare trends
* Correlation heatmap

---

### 4. Model Building

* Algorithm: **K-Nearest Neighbors Regressor**
* Train-test split (80/20)
* Feature scaling using **StandardScaler**

---

### 5. Hyperparameter Tuning

Used **GridSearchCV** to find optimal parameters:

```python
{
  'n_neighbors': [3, 5, 7, 9],
  'weights': ['uniform', 'distance'],
  'metric': ['euclidean', 'manhattan']
}
```

---

##  Best Model Performance

* **Best Parameters:**

  * Metric: `euclidean`
  * Neighbors (K): `9`
  * Weights: `uniform`

* **Evaluation Metrics:**

  * MAE: **2.43**
  * RMSE: **5.17**

Interpretation:

* On average, the model predicts fare within **~2.4 units error**
* Model performs reasonably well for real-world noisy data

---

## 📈 Key Insights

*  **Distance is the most important feature**
*  Passenger count has minimal impact
*  Time (hour/weekend) slightly affects fare
*  Data cleaning significantly improves performance

---

##  Model Intuition

KNN predicts fare by:

> Finding similar past rides and averaging their fares

---

##  Tech Stack

* Python 🐍
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn

---

##  How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run notebook / script
```

---

##  Example Prediction

```python
predict_fare(distance=3.2, hour=18, passengers=2, day=4, weekend=0)
```

 Output:

```
Predicted Fare: ~₹X
```

---

## ⚠️ Limitations

* KNN is slow for large datasets
* Sensitive to outliers
* Does not learn explicit patterns (lazy learner)

---


##  Conclusion

This project demonstrates:

* End-to-end ML pipeline
* Real-world data handling
* Feature engineering impact
* Model tuning & evaluation

---

##  Author

**Umer Rafiq**

* BTech CSE Student


## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
