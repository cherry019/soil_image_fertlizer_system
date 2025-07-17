import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
from gtts import gTTS
from io import BytesIO
from IPython.display import Audio
import base64

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("soil_cnn_model.h5")

# Load fertilizer CSV
@st.cache_data
def load_fertilizer_data():
    df = pd.read_csv("Fertilizer Prediction.csv")
    df['Soil Type'] = df['Soil Type'].str.lower().str.strip()
    return df

# Predict soil from image
def predict_soil(image, model):
    img = image.resize((150, 150))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions)
    class_labels = ['Alluvial soil', 'Black soil', 'Clay soil', 'Red soil']
    return class_labels[class_idx]

# Recommend fertilizer
def recommend_fertilizer(soil, df):
    soil_mapping = {
        "Red soil": "red",
        "Black soil": "black",
        "Clay soil": "clayey",
        "Alluvial soil": "loamy"
    }
    mapped_soil = soil_mapping.get(soil)
    if not mapped_soil:
        return "Invalid soil type.", "చెల్లని నేల రకం."

    matches = df[df['Soil Type'] == mapped_soil]
    if matches.empty:
        return "No matching fertilizer found.", "ఈ నేల రకానికి ఎరువు లేదు."

    eng = f"Fertilizer recommendations for {soil}:\n"
    tel = f"{soil} కోసం ఎరువు సూచనలు:\n"
    for _, row in matches.iterrows():
        eng += f"- Crop: {row['Crop Type']}, Fertilizer: {row['Fertilizer Name']} (NPK: {row['Nitrogen']}-{row['Phosphorous']}-{row['Potassium']})\n"
        tel += f"- పంట: {row['Crop Type']}, ఎరువు: {row['Fertilizer Name']} (NPK: {row['Nitrogen']}-{row['Phosphorous']}-{row['Potassium']})\n"
    return eng, tel

# Speak Telugu
def speak_telugu(text):
    tts = gTTS(text=text, lang='te')
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

# UI
st.title("🌱 Soil-Based Fertilizer Recommender (Telugu/English)")

df = load_fertilizer_data()
model = load_model()

soil = None
uploaded_file = st.file_uploader("📷 Upload soil image (optional)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Soil Image", use_column_width=True)
    soil = predict_soil(image, model)
    st.success(f"🧠 Predicted Soil Type: {soil}")

# Manual fallback
soil_option = st.selectbox("🌾 Or select soil type manually", ["", "Red soil", "Black soil", "Clay soil", "Alluvial soil"])
if not soil and soil_option:
    soil = soil_option

# Run recommendation
if soil:
    eng, tel = recommend_fertilizer(soil, df)
    st.subheader("📋 English Output:")
    st.text(eng)
    st.subheader("🈶 Telugu Output:")
    st.text(tel)

    # Voice output
    if st.button("🔊 Speak in Telugu"):
        speak_telugu(tel)
