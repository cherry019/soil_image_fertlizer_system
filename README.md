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


---

## 📸 How It Works

1. **Upload a soil image** through the Streamlit UI.
2. The image is processed and passed to a pre-trained model.
3. The model predicts the **soil type**.
4. Based on the prediction, the system recommends a **fertilizer** in:
   - ✅ English
   - ✅ Telugu
5. Displays the result neatly in a clean layout.

---

## 🌾 Project Preview

### 🧪 Soil Detection Page
![Soil Detection](![WhatsApp Image 2025-07-15 at 22 58 12_e5d7003b](https://github.com/user-attachments/assets/a14f61ea-62a1-4fb4-9775-9f91757df83a)
)

### 🌱 Recommendation Page
![Fertilizer Suggestion](![WhatsApp Image 2025-07-15 at 22 58 12_09aee4f7](https://github.com/user-attachments/assets/9587ea2e-679f-45ff-adb7-22b0f953f437)
)

## 🔧 Installation

```bash
git clone https://github.com/your-username/soil-fertilizer-recommender.git
cd soil-fertilizer-recommender
pip install -r requirements.txt
streamlit run app.py


## 📂 Project Structure
