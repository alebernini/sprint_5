import pandas as pd
from pathlib import Path
import streamlit as st

df = pd.read_csv(Path("../data/turnover.csv"))

st.title("Análise de Turnover")

fig = px.histogram(df, x = 'RendaMensal', color = 'Turnover')
st.plotpy_chart(fig)





