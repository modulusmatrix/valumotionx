import streamlit as st
from core import valumotion_hesapla
st.title("ValuMotionX")
z = st.slider("Zaman",1,120,10)
m = st.slider("Maddi",0.0,1.0,0.7)
ma = st.slider("Manevi",0.0,1.0,0.7)
d = st.slider("Dis",0.0,1.0,0.6)
x = st.slider("X",0.0,1.0,0.75)
s = valumotion_hesapla(z,m,ma,d,x,"birey")
st.write(s)
