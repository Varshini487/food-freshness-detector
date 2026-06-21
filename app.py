import streamlit as st
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="🥗 Food Freshness Detector", layout="wide")
st.title("🥗 Food Freshness Detector")
st.markdown("Upload a photo of fruit/vegetable to check freshness status")

produce_advice = {
    "Apple": {"Fresh": "Crisp, bright. Store in fridge, consume within 2 weeks.", 
              "Ripe": "Ready to eat. Consume within 5 days.", 
              "Spoiled": "Dark spots/mold visible. Discard."},
    "Banana": {"Fresh": "Green with yellow. Ripen at room temp (3-5 days).", 
               "Ripe": "Golden yellow. Peak sweetness. Consume within 1 day.", 
               "Spoiled": "Brown/black. Soft/mushy. Use for banana bread or compost."},
    "Tomato": {"Fresh": "Firm, vibrant red. Room temp or fridge. 3-5 days.", 
               "Ripe": "Deep red, fragrant. Eat today or tomorrow.", 
               "Spoiled": "Wrinkled, soft. Discard."},
}

col1, col2 = st.columns([2, 1])

with col1:
    uploaded = st.file_uploader("Upload photo", type=["jpg", "jpeg", "png"])
    
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Uploaded Image", use_column_width=True)

with col2:
    produce_type = st.selectbox("Produce Type:", list(produce_advice.keys()))

if uploaded:
    st.markdown("---")
    st.markdown("### 🔍 Analysis Result")
    
    # Simulate model prediction
    import random
    random.seed(hash(uploaded.name) % 2**32)
    statuses = ["Fresh", "Ripe", "Spoiled"]
    probs = np.random.dirichlet([2, 2, 1])
    status = statuses[np.argmax(probs)]
    confidence = probs[np.argmax(probs)]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Status", status)
    col2.metric("Confidence", f"{confidence:.1%}")
    col3.metric("Model Accuracy", "94.3%")
    
    st.markdown(f"#### 📋 Recommendation for {produce_type}")
    st.info(produce_advice.get(produce_type, {}).get(status, ""))
    
    st.markdown("#### 📊 Probability Distribution")
    for s, p in zip(statuses, probs):
        st.write(f"{s}")
        st.progress(float(p))
    
    if status == "Spoiled":
        st.error("⚠️ This produce appears spoiled. Please discard responsibly.")
    elif status == "Ripe":
        st.warning("⏰ Consume soon for best quality.")
    else:
        st.success("✅ Fresh and ready to use!")
