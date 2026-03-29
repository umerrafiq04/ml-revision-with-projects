# 🖼️ Image Processing Suite using K-Means Clustering

## 🚀 Overview

This project is an **interactive web application** built using **Streamlit** that applies **K-Means Clustering** to perform various image processing tasks.

It demonstrates how **unsupervised machine learning** can be used in **computer vision** for real-world applications like image compression and segmentation.

---

## ✨ Features

* 📦 **Image Compression**

  * Reduces number of colors using K-Means
  * Smaller file size with minimal quality loss

* 🧠 **Image Segmentation**

  * Divides image into meaningful regions
  * Uses RGB + spatial features

* 🔴 **Segmentation with Boundaries**

  * Highlights region borders
  * Better visualization of clusters

* 🟢 **Segmentation + Edge Detection**

  * Combines clustering with edge detection
  * Uses OpenCV (Canny Edge Detector)

* 🎛️ **Interactive Controls**

  * Adjustable number of clusters (K)
  * Real-time output updates

* 📥 **Download Option**

  * Save processed image directly

---

## 🧠 How It Works

### 🔹 K-Means Clustering

* Each pixel is treated as a data point
* Features used:

  * RGB values
  * (Optional) Spatial coordinates (X, Y)
* Pixels are grouped into **K clusters**
* Each cluster represents a region or color

---

## ⚙️ Tech Stack

* Python 🐍
* Streamlit
* NumPy
* OpenCV
* Scikit-learn
* Pillow (PIL)

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/image-processing-kmeans.git
cd image-processing-kmeans
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 🎯 Key Concepts Covered

* Unsupervised Learning
* K-Means Clustering
* MiniBatchKMeans (optimized version)
* Image Processing
* Feature Engineering (RGB + Spatial)
* Edge Detection (Canny)

---

## 📊 Insights

* Lower **K value** → fewer colors → smaller file size
* Higher **K value** → more detail → larger file size
* Adding spatial features improves segmentation quality

---

## 🏆 Project Highlights

* Combines **Machine Learning + Computer Vision**
* Real-time interactive UI
* Optimized using **MiniBatchKMeans**
* Beginner-friendly but scalable

---

## 🙌 Author

**Umer Rafiq**

* BTech CSE Student
---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
