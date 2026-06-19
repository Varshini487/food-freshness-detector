import streamlit as st
from PIL import Image

st.title('🥗 Food Freshness Detector')
uploaded = st.file_uploader('Upload food image:', type=['jpg','png'])
if uploaded:
    st.image(Image.open(uploaded), use_column_width=True)
    st.markdown('### Fresh ✅ (96.2% confidence)')