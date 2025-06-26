# 🩺 Diabetic Retinopathy Detection using Deep Learning

A deep learning-based approach for detecting **Diabetic Retinopathy** using fundus eye images. The project uses a **CNN model** to classify the severity of DR, aiming to support early detection and treatment.

---

## 🚀 Tools Used

- 🐍 **Python**
- 🧠 **TensorFlow / Keras** – Building and training deep learning models
- 🖼️ **OpenCV** – Image processing and enhancement
- 📊 **Matplotlib / Seaborn** – Visualization of results
- 📁 **NumPy / Pandas** – Data manipulation
- 💻 **Google Colab** – GPU-accelerated training environment
- 📦 **Dataset** – [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection)

---

## 📊 Results & Insights

- ✅ Successfully built a **multi-class CNN model** to detect DR stages (0–4)
- 🧪 Used **image preprocessing**, **data augmentation**, and **class balancing** to improve accuracy
- 📉 Applied **early stopping** and **dropout** to prevent overfitting
- 🔍 Found better performance on binary classification compared to multi-class (due to class imbalance)

| Metric | Value (Example) |
|--------|-----------------|
| ✅ Training Accuracy | 85% |
| 📉 Validation Accuracy | 76% |
| 🧪 Test Accuracy | ~72% |

> 📈 *(Add your actual training/validation graph as an image if available)*

---

## 🧠 What I Learned

- 📚 How to work with **medical imaging datasets** and apply CNNs to classify them
- 🧪 Applied **data augmentation** techniques to overcome class imbalance
- 🧠 Gained deeper understanding of **convolutional layers**, **regularization**, and **dropout**
- ⚙️ End-to-end pipeline from data preprocessing to model evaluation

---

## ⚠️ Challenges Faced

- ⚖️ **Severe class imbalance** made it difficult for the model to generalize
- 🔁 Overfitting occurred in early versions of the model before applying regularization
- 🌫️ Image quality issues like blur and noise affected model performance
- 🕒 Long training times due to high-resolution images and dataset size

---

## ✅ Conclusion

- This project highlights how **deep learning can aid in early DR detection**.
- Though the results are promising, real-world applications require:
  - 🔁 **Transfer learning** (e.g., EfficientNet, Inception)
  - 🧠 **Ensemble techniques**
  - 🧪 Further testing and validation with real clinical data

---

## 📂 Dataset and References

- 📥 **Dataset**: [APTOS 2019 Blindness Detection](https://www.kaggle.com/competitions/aptos2019-blindness-detection)
- 📄 **Research Paper**: [Deep Learning for Detection of Diabetic Eye Disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6381472/)
