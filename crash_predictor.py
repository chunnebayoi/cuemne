import streamlit as st
import random

st.set_page_config(page_title="Dự đoán Crash Game", page_icon="🎯")

st.title("🎯 Tool Dự Đoán Hệ Số Game Crash")
st.markdown("Dự đoán hệ số nổ tiếp theo dựa trên lịch sử gần nhất. Mô hình đơn giản nhưng vui vẻ 😉")

# Nhập lịch sử hệ số
crash_input = st.text_input(
    "🔢 Nhập lịch sử hệ số nổ (cách nhau bằng dấu phẩy):",
    value="1.35, 1.02, 1.10, 1.05, 1.87, 2.91, 1.12, 1.01, 1.30, 1.05"
)

def parse_input(text):
    try:
        return [float(x.strip()) for x in text.split(",") if x.strip()]
    except:
        return []

def analyze_trend(history):
    last_5 = history[-5:]
    under_2 = sum(1 for x in last_5 if x < 2.0)

    if under_2 >= 4:
        return "🟢 Dự đoán: Sắp nổ cao (>=2.0x)"
    else:
        return "🔴 Dự đoán: Nổ thấp (<2.0x) hoặc trung bình"

def predict_next(history):
    trend = analyze_trend(history)

    if "cao" in trend:
        predicted = round(random.uniform(2.0, 10.0), 2)
    else:
        predicted = round(random.uniform(1.01, 1.99), 2)

    return trend, predicted

if st.button("🎲 Dự đoán ngay"):
    history = parse_input(crash_input)
    if len(history) < 5:
        st.error("Vui lòng nhập ít nhất 5 hệ số!")
    else:
        trend_msg, next_crash = predict_next(history)
        st.success(trend_msg)
        st.metric("🎯 Dự đoán hệ số tiếp theo", f"{next_crash}x")
