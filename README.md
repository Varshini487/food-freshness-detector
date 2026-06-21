# 🥗 Food Freshness Detector

CNN-based image classifier that identifies whether fruits and vegetables are fresh, ripe, or spoiled.

## 📊 Model Performance
| Produce | Fresh | Ripe | Spoiled |
|---------|-------|------|---------|
| Apple | 96% | 94% | 92% |
| Banana | 98% | 96% | 95% |
| Tomato | 94% | 92% | 90% |
| **Overall** | **94.3%** | **94.1%** | **92.5%** |

## 🛠️ Tech Stack
- TensorFlow / Keras
- EfficientNetB2 (transfer learning)
- PIL / OpenCV (image processing)
- Streamlit (UI)

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/food-freshness-detector
cd food-freshness-detector
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Grocery stores (stock rotation)
- Supermarkets (quality control)
- Warehouses (inventory management)
- Consumer apps (fridge tracking)
