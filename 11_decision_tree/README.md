# 🚨 Cybersecurity Intrusion Detection System (UNSW-NB15)

## 📌 Overview

This project builds a **machine learning-based Intrusion Detection System (IDS)** that classifies network traffic as **Normal or Malicious (Attack)** using features extracted from network flows.

The system is trained on the **UNSW-NB15 dataset**, a modern benchmark dataset for cybersecurity research.

---

## 🎯 Objectives

* Detect malicious network traffic in real-time
* Build a robust ML pipeline with proper preprocessing
* Avoid data leakage and overfitting
* Deploy the model using a **Streamlit web app**

---

## 📊 Dataset

* **Dataset**: UNSW-NB15
* Contains network flow features such as:

  * Packet counts (`spkts`, `dpkts`)
  * Byte counts (`sbytes`, `dbytes`)
  * Traffic rate (`rate`, `sload`, `dload`)
  * Protocols (`proto`, `service`, `state`)
* Target:

  * `label` → 0 (Normal), 1 (Attack)

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit (Deployment)
* Joblib (Model Saving)

---

## 🔄 Workflow

### 1. Data Preprocessing

* Removed leakage column (`attack_cat`)
* Handled missing values
* Shuffled dataset to avoid bias
* Encoded categorical features using:

  * `OrdinalEncoder (handle_unknown = -1)`

---

### 2. Exploratory Data Analysis (EDA)

* Target distribution analysis
* Feature distributions
* Correlation heatmap
* Feature vs target relationships

---

### 3. Model Building

* Algorithm: **Decision Tree Classifier**
* Controlled overfitting using:

  * `max_depth`
  * `min_samples_split`
  * `min_samples_leaf`
* Used `class_weight='balanced'` to handle imbalance

---

### 4. Hyperparameter Tuning

* Used **GridSearchCV**
* Optimized using **F1-score**
* 5-fold cross-validation

---

### 5. Evaluation Metrics

```
Final Accuracy: 0.9063

Precision:
Normal → 0.91
Attack → 0.91

Recall:
Normal → 0.88
Attack → 0.92

F1-Score:
Normal → 0.89
Attack → 0.92
```

✅ Model performs well on both classes
✅ High recall for attack detection (critical in cybersecurity)

---

## 🖥️ Streamlit Web App

The project includes an interactive web app where users can:

* Input network traffic features
* Load sample attack/normal data
* Get real-time predictions

### App Preview
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/47febad6-3d1c-4423-a94e-42c546be58fa" />

##Normal Traffic:
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/83c89b64-f701-4fc5-9e86-eb8d877e0727" />

##Attack:
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/2c664f75-541e-409e-b8d9-0ed9f22befbf" />
---

## 🚀 How to Run

### 1. Clone Repository

```
git clone https://github.com/your-username/intrusion-detection-system.git
cd intrusion-detection-system
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Streamlit App

```
streamlit run app.py
```

---

## 📂 Project Structure

```
├── data/
├── notebooks/
├── app.py
├── model.pkl
├── encoder.pkl
├── features.pkl
├── cat_cols.pkl
├── requirements.txt
└── README.md
```

---

## 🧠 Key Learnings

* Importance of avoiding **data leakage**
* Handling **unseen categories** in real-world data
* Preventing **overfitting in decision trees**
* Building **end-to-end ML pipelines**
* Deploying ML models with **Streamlit**

---

## 🙌 Author

**Umer Rafiq**
BTech CSE | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
