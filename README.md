# ML Revision with Projects

## Overview

This repository documents my structured revision of core Machine Learning algorithms through hands-on projects. The goal is to reinforce theoretical understanding by implementing practical, real-world use cases for each algorithm.

Each project focuses on a specific algorithm and follows a complete workflow including preprocessing, exploratory data analysis (EDA), model building, evaluation, and optimization.

---

## Objectives

* Strengthen understanding of Machine Learning algorithms
* Build practical intuition through project-based learning
* Develop end-to-end ML pipelines
* Prepare for technical interviews and real-world applications

---

## Repository Structure

```
ml-revision-with-projects/
│
├── logistic-regression/
├── naive-bayes/
├── svm/
├── knn/
├── decision-tree/
├── random-forest/
├── clustering/
├── regression/
└── ...
```

Each folder contains:

* Dataset (or dataset link)
* Implementation (Notebook / Python scripts)
* Evaluation and results
* Project-specific details

---

## Best Projects

### 1. Handwritten Digit Recognition using SVM

* Built a classification system to recognize handwritten digits
* Applied Support Vector Machine (SVM) for high-dimensional data
* Implemented preprocessing, feature scaling, and model evaluation
* Achieved strong classification accuracy on image data

---

### 2. Cybersecurity Intrusion Detection System using Decision Tree

#### Overview

This project builds a **machine learning-based Intrusion Detection System (IDS)** that classifies network traffic as **Normal or Malicious (Attack)** using features extracted from network flows.

It simulates a real-world cybersecurity system for detecting malicious activities in network traffic.

---

#### Key Features

* End-to-end ML pipeline (EDA → preprocessing → modeling → evaluation → deployment)
* Handled real-world issues like **data leakage, imbalance, and unseen categories**
* Used **OrdinalEncoder with unknown handling** for robustness
* Hyperparameter tuning using **GridSearchCV**
* Built an interactive **Streamlit web application** for real-time prediction
* Feature importance analysis for interpretability

---

#### Dataset

* Name: UNSW-NB15 Dataset
* Type: Network Intrusion Detection Dataset
* Contains features like protocol, packet counts, byte size, traffic rate

---

#### Model Performance

* Accuracy: **90.6%**
* Precision: ~0.91
* Recall: ~0.92 (Attack detection)
* F1-score: ~0.91

---

#### Key Highlights

* Achieved **balanced performance across both classes**
* High recall for attacks (critical in cybersecurity systems)
* Avoided overfitting and unrealistic 100% accuracy
* Built a deployable ML system

---

### 3. Customer Segmentation Engine using Multinomial Logistic Regression

#### Overview

This project builds an end-to-end machine learning system to segment customers into **High Value, Medium Value, and Low Value groups** using RFM (Recency, Frequency, Monetary) analysis and Multinomial Logistic Regression.

It simulates a real-world marketing analytics pipeline for targeted decision-making.

---

#### Key Features

* Complete ML pipeline (data → preprocessing → feature engineering → modeling → evaluation)
* Industry-standard RFM segmentation
* Multiclass classification using Logistic Regression
* Hyperparameter tuning using GridSearchCV
* Probability-based predictions (`predict_proba`)
* Model interpretability via coefficients

---

#### Dataset

* Name: Online Retail Dataset
* Source: Kaggle
* Link: https://www.kaggle.com/datasets/carrie1/ecommerce-data

---

#### Model Performance

* Accuracy: **89%**
* Macro F1-score: **0.90**
* Weighted F1-score: **0.89**

---

#### Business Impact

* Enables targeted marketing strategies
* Identifies high-value and churn-risk customers
* Supports data-driven decision making

---

### 4. Email / Text Categorization System using Naive Bayes

* Built a multi-class text classification system using the 20 Newsgroups dataset
* Implemented text preprocessing, TF-IDF vectorization, and feature engineering
* Applied Multinomial Naive Bayes with hyperparameter tuning (GridSearchCV)
* Achieved approximately **89% accuracy** on a 20-class classification task
* Developed a Streamlit-based interface for real-time predictions

---

## Covered Algorithms (Ongoing)

* Linear Regression
* Logistic Regression
* Naive Bayes
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Decision Trees
* Random Forest
* Clustering Algorithms

This list will continue to expand as more algorithms are implemented.

---

## Approach

For each project:

1. Problem Definition
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Evaluation (Accuracy, Precision, Recall, F1-score)
7. Optimization (if applicable)
8. Optional Deployment

---

## Tools and Technologies

* Python
* Scikit-learn
* Pandas, NumPy
* Matplotlib, Seaborn
* NLTK
* Streamlit

---

## Status

This repository is actively maintained and continuously updated with new Machine Learning projects.

---

## Author

**Umer Rafiq**
*B.Tech CSE Student*
