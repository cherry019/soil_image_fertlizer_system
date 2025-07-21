# 🌱 Soil Fertilizer Recommender - Mini Project

This is a **mini machine learning project** built with **Streamlit**, which recommends suitable **fertilizers** for a given **soil type image**. The app supports output in **Telugu and English** for better accessibility and understanding.

---

## 🚀 Features

- 📷 **Image Upload**: Upload a soil image to predict the soil type.
- 🌾 **Fertilizer Recommendation**: Based on the predicted soil type, get the best matching fertilizer.
- 🌐 **Bilingual Output**: Results displayed in both **Telugu** and **English**.
- 🧠 **Machine Learning**: Uses image classification models (TensorFlow/Keras).
- 🖼️ Built with an interactive **Streamlit UI**.
- 📄 **3-page structure** in UI:
  1. **Home** – Introduction and instructions.
  2. **Soil Detection** – Upload image and view prediction.
  3. **Recommendation** – View fertilizer suggestion and download results.

---

## 🧰 Tech Stack & Libraries

- `streamlit` – Web UI
- `pandas` – Data handling
- `numpy` – Numerical computation
- `scikit-learn` – Preprocessing & ML tools
- `tensorflow` – Deep learning backend
- `keras` – Model training & prediction
- `Pillow` – Image processing
- `opencv-python` – Image manipulation
- `joblib` – Model serialization
- `requests` – Optional API interaction

---

## 📂 Project Structure

soil-fertilizer-recommender/
├── app.py
├── pages/
│ ├── 1_Home.py
│ ├── 2_Soil_Detection.py
│ └── 3_Recommendation.py
├── model/
│ └── soil_model.h5 / .pkl
├── utils/
│ └── helper.py
├── images/
│ └── sample.jpg
├── requirements.txt
└── README.md

