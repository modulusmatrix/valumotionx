import streamlit as st

st.set_page_config(page_title="ValuMotionX Test")
st.title("✅ Deploy Çalışıyor")
st.write("Eğer bunu görüyorsan sorun app.py içinde.")

try:
    import numpy as np
    import plotly.graph_objects as go
    from core import valumotion_hesapla
    st.success("Tüm importlar OK")
except Exception as e:
    st.error(f"Import hatası: {e}")
