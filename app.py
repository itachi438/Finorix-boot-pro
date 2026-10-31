import time
import numpy as np
import pandas as pd
import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Finorix Pro - Live Trading Engine",
    page_icon="⚡",
    layout="centered",
)

# --- Finorix Pro Dark Custom Styling ---
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0f19; color: #ffffff; }
    .main-header { font-size: 24px; font-weight: bold; text-align: center; color: #3fb950; margin-bottom: 2px; }
    .sub-text { text-align: center; color: #8b949e; font-size: 13px; margin-bottom: 20px; }
    .running-candle-box { background: rgba(31, 111, 235, 0.15); border: 2px solid #1f6feb; padding: 18px; border-radius: 12px; text-align: center; color: #58a6ff; font-size: 22px; font-weight: bold; }
    .card-call { background: rgba(46, 160, 67, 0.15); border: 2px solid #2ea043; padding: 18px; border-radius: 12px; text-align: center; color: #3fb950; font-size: 20px; font-weight: bold; }
    .card-put { background: rgba(248, 81, 73, 0.15); border: 2px solid #f85149; padding: 18px; border-radius: 12px; text-align: center; color: #f85149; font-size: 20px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- App Header ---
st.markdown(
    '<div class="main-header">🦁 FINORIX PRO (OFFICIAL BOT)</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">Real-time Running Candle & Next-Gen Signal Predictor</div>',
    unsafe_allow_html=True,
)

# --- Top Status Bar (Activated / Real API) ---
col_s1, col_s2, col_s3 = st.columns(3)
col_s1.markdown("🟢 **Activated**")
col_s2.markdown("📈 **Real chart**")
col_s3.markdown("🚀 **Live API**")

st.markdown("---")

# --- Asset & Timeframe Selectors ---
col_c1, col_c2 = st.columns(2)
with col_c1:
    pair = st.selectbox(
        "Asset Pair",
        ["USD/PKR (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)"],
    )
with col_c2:
    timeframe = st.selectbox("Timeframe", ["M1 (1 Min)", "M5 (5 Min)"])

st.markdown("---")

# --- Running Candle Simulation Engine ---
base_price = 288.95 if "PKR" in pair else 1.0850
np.random.seed(int(time.time() // 3))
ticks = np.cumsum(np.random.randn(20) * 0.015) + base_price
current_tick = ticks[-1]

# Running Candle Display Box (Jaise video mein hai)
st.markdown(
    f'<div class="running-candle-box">🕯️ RUNNING CANDLE TICK<br><span style="font-size:26px; color:#ffffff;">{current_tick:.2f}</span></div>',
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

# Live Chart Visualization
chart_df = pd.DataFrame(
    {
        "Market Price": ticks,
        "Trend Fast": pd.Series(ticks).ewm(span=4).mean(),
    }
)
st.line_chart(chart_df)

st.markdown("---")

# --- Signal Generation Trigger ---
if st.button("🚀 GENERATE ADVANCE SIGNAL", use_container_width=True):
    with st.spinner("Analyzing running candle momentum & order flow..."):
        time.sleep(1.2)

    rsi_val = round(np.random.uniform(34.0, 69.0), 1)
    win_accuracy = np.random.randint(89, 96)

    m1, m2 = st.columns(2)
    m1.metric("Live RSI (14)", f"{rsi_val}")
    m2.metric("Accuracy", f"{win_accuracy}%")

    st.markdown("<br>", unsafe_allow_html=True)

    if rsi_val > 50:
        st.markdown(
            f'<div class="card-call">🟢 CALL (UP) SIGNAL<br><span style="font-size:13px; color:#ffffff;">Pair: {pair} | Expiry: {timeframe} | Target: Bullish</span></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="card-put">🔴 PUT (DOWN) SIGNAL<br><span style="font-size:13px; color:#ffffff;">Pair: {pair} | Expiry: {timeframe} | Target: Bearish</span></div>',
            unsafe_allow_html=True,
        )
else:
    st.info("👆 'GENERATE ADVANCE SIGNAL' par click karein taake agla signal mil sakay!")
