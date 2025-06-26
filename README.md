# 🩺 Diabetic Retinopathy Detection using Deep Learning

A deep learning-based project to detect **Diabetic Retinopathy (DR)** from retinal fundus images using **Convolutional Neural Networks (CNNs)**. The goal is to automate early diagnosis and assist ophthalmologists in identifying DR severity efficiently.

---

## 📁 Table of Contents

- [🚀 Tools & Technologies Used](#-tools--technologies-used)
- [🧠 Problem Statement](#-problem-statement)
- [📊 Results & Insights](#-results--insights)
- [📌 What We Learned](#-what-we-learned)
- [⚠️ Challenges Faced](#-challenges-faced)
- [✅ Conclusion](#-conclusion)
- [👨‍💻 Team Contribution](#-team-contribution)
- [📂 Dataset & References](#-dataset--references)

---

## 🚀 Tools & Technologies Used

- 🐍 **Python 3**
- 🧠 **TensorFlow / Keras** – Model building and training
- 🖼️ **OpenCV** – Image preprocessing
- 📊 **Matplotlib / Seaborn** – Visualization
- 📁 **NumPy / Pandas** – Data manipulation
- 💻 **Google Colab** – GPU-accelerated training
- 📦 **Dataset** – [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection)

---

## 🧠 Problem Statement

> Diabetic Retinopathy is one of the leading causes of blindness globally. Early detection is essential to prevent severe complications.  
> This project aims to build a machine learning model that can classify fundus images into 5 stages of diabetic retinopathy, from healthy to severe cases.

---

## 📊 Results & Insights

- 🧪 Developed a **multi-class CNN model** to classify DR stages (0–4)
- 📈 Applied **data augmentation**, **class balancing**, **dropout**, and **early stopping**
- 📊 Achieved promising results despite data imbalance

| Metric              | Value (Example) |
|---------------------|-----------------|
| ✅ Training Accuracy | 85%             |
| 📉 Validation Accuracy | 76%          |
| 🧪 Test Accuracy     | ~72%            |

> 🔍 Binary classification between "No DR" and "DR" showed better accuracy due to data skew

---

## 📌 What We Learned

- Building CNNs for medical image classification tasks  
- Importance of **image preprocessing** and **augmentation**  
- Handling **class imbalance** in real-world datasets  
- Optimizing model performance with **regularization** techniques  
- Collaborative workflow using **Git/GitHub** and **Colab Notebooks**

---

## ⚠️ Challenges Faced

- ⚖️ **Highly Imbalanced Dataset** – Most images belonged to Class 0 (No DR)  
- 🌫️ **Variable Image Quality** – Affected consistency in training  
- 🔁 **Overfitting** – Resolved using dropout, augmentation, and early stopping  
- ⏱️ **Training Time** – High-resolution images increased compute needs

---

## ✅ Conclusion

This project demonstrated how **deep learning** can support healthcare by detecting diabetic retinopathy with promising accuracy.  
Further improvements can be made by:
- 🔁 Implementing **transfer learning** (EfficientNet, Inception)
- 📦 Using **segmentation + classification pipelines**
- 🔍 Validating on real-world clinical datasets

---

## 👨‍💻 Team Contribution

A team of 5 passionate students collaboratively completed this project:

- 👤 **Sai Balaji** – Model development, preprocessing pipeline  
- 👤 **Vandana** – Data cleaning, augmentation strategy  
- 👤 **Raj Kamal** – Exploratory data analysis, visualizations  
- 👤 **Nikitha** – Hyperparameter tuning, training loops  
- 👤 **Preetham** – GitHub repo management, presentation & documentation  

> 🙌 Each team member contributed equally to research, coding, debugging, and model improvement.

---

## 📂 Dataset & References

- 📥 Dataset: [APTOS 2019 Blindness Detection – Kaggle](https://www.kaggle.com/competitions/aptos2019-blindness-detection)
- 📄 Paper: [Deep Learning for Detection of Diabetic Eye Disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6381472/)
- 📚 Further Reading: [Retinopathy on Wikipedia](https://en.wikipedia.org/wiki/Diabetic_retinopathy)

---

> 📌 *For questions, collaboration, or feedback, feel free to open an issue or reach out via GitHub!*

