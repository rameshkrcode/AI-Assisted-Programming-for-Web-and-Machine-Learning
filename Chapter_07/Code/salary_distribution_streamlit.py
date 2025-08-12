
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Salary Distribution Viewer")
fig, ax = plt.subplots()
sns.histplot(df['Salary'], kde=True, ax=ax)
st.pyplot(fig)
