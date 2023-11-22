import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

st.dataframe(df)
# st.dataframe(df.style.highlight_max(axis=0))