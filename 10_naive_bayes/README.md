# Email / Text Categorization System using Naive Bayes

## Overview

This project implements an end-to-end Natural Language Processing (NLP) pipeline for multi-class text classification. The system categorizes input text into 20 different domains such as technology, sports, politics, religion, and science.

The model is trained on the **20 Newsgroups dataset** and deployed using a Streamlit web application for real-time predictions.

---

## Dataset

* Source: Scikit-learn 20 Newsgroups Dataset
* Total samples: 18,846 
* Number of classes: 20

Each document is labeled with a category representing its topic.

---

## Methodology

### Text Processing

* Lowercasing
* Removal of special characters
* Stopword removal
* Lemmatization using NLTK

### Feature Engineering

* TF-IDF Vectorization
* N-gram support (optimized during tuning)

### Model

* Multinomial Naive Bayes

### Hyperparameter Tuning

* GridSearchCV used to optimize:

  * Smoothing parameter (`alpha`)
  * TF-IDF parameters (e.g., max_features, ngram_range)

---

## Model Performance

### Before Tuning

* Accuracy: ~87%

### After Hyperparameter Tuning

* Accuracy: **88.9%** 

### Evaluation Metrics

* Macro F1-score: 0.89
* Weighted F1-score: 0.89

The model performs well across most categories, with slightly lower recall in overlapping domains such as politics and religion.

---

## Application (Streamlit)

A Streamlit-based interface is provided to interact with the model.

### Features

* Text input for prediction
* Predicted category output
* Confidence score display

---

## Screenshots

### Prediction Example

<img width="1920" height="1008" alt="Streamlit - Google Chrome 27-03-2026 12_00_20" src="https://github.com/user-attachments/assets/fb608c1f-480e-423d-9847-01ed5abf5850" />

---

## Project Structure

```
project/
│
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── labels.pkl
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

```
streamlit run app.py
```

---

## Example Predictions

| Input Text                    | Predicted Category |
| ----------------------------- | ------------------ |
| NASA launched a satellite     | sci.space          |
| The hockey team won the match | rec.sport.hockey   |
| New GPU released for gaming   | comp.graphics      |

---

## Key Learnings

* End-to-end NLP pipeline design
* Text preprocessing and feature engineering
* Model optimization using GridSearchCV
* Deployment using Streamlit


---

## Acknowledgements

* Scikit-learn for dataset and tools
* NLTK for text preprocessing
* Streamlit for deployment

## Author
* Umer Rafiq
* B.Tech CSE Student
