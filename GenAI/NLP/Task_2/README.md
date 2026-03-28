# 📊 Sentiment Analysis using NLP & Machine Learning

This project focuses on building a complete end-to-end **Sentiment Analysis system** using Natural Language Processing (NLP) techniques and Machine Learning models.

The goal is to transform raw text data into meaningful features and train models to classify sentiment as **Positive or Negative**.

---

## 📌 Project Overview

In real-world applications, text data is often unstructured and noisy. This project demonstrates how to:

- Clean and preprocess text data
- Convert text into numerical features
- Train multiple ML models
- Evaluate and compare their performance

---

## 📂 Dataset

- Source: Kaggle  
- Dataset Used: IMDb Movie Reviews Dataset  
- Total Samples: 50,000  
- Labels: Positive / Negative  

---

## 🔧 NLP Preprocessing Steps

The following preprocessing techniques were applied:

- Lowercasing text
- Removing HTML tags and URLs
- Removing special characters and punctuation
- Tokenization (splitting text into words)

> Note: Stopword removal and stemming were tested but not used in the final model as they reduced accuracy for this dataset.

---

## 🧠 Feature Engineering

Two techniques were used to convert text into numerical form:

- **Bag of Words (BoW)**
- **TF-IDF (Term Frequency - Inverse Document Frequency)**

TF-IDF performed better as it reduces the importance of common words and captures meaningful features.

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Naive Bayes
- Decision Tree

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|------|--------|----------|--------|---------|
| Logistic Regression (TF-IDF) | 0.90 | 0.90 | 0.90 | 0.90 |
| Naive Bayes (BoW) | 0.85 | 0.85 | 0.85 | 0.85 |
| Decision Tree (TF-IDF) | 0.72 | 0.72 | 0.72 | 0.72 |

---

## 📈 Key Insights

- Logistic Regression achieved the best performance (~90% accuracy)
- TF-IDF outperformed Bag of Words due to better feature weighting
- Decision Tree performed poorly due to overfitting on text data
- Proper preprocessing significantly improved model performance

---

## ⚖️ Trade-offs

- Naive Bayes is fast but slightly less accurate
- Logistic Regression provides the best balance between performance and accuracy
- Decision Tree is not suitable for high-dimensional sparse text data

---

## 🔄 NLP Pipeline Flow

Raw Text  
→ Preprocessing  
→ Feature Engineering (BoW / TF-IDF)  
→ Model Training  
→ Evaluation  
→ Comparison  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  

---

## 📌 Conclusion

This project demonstrates how NLP preprocessing and feature engineering play a crucial role in building effective sentiment analysis models.

Among all models, **Logistic Regression with TF-IDF** gave the best results, showing that simple models can perform well with the right preprocessing and features.

---

## 🔗 Author

**MD Javeed Khan**  
📧 mdjaveedkhanofficial@gmail.com  
🌐 Portfolio: https://mdjaveedkhan.me  
