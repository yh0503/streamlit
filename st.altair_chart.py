import streamlit as st
import altair as alt
import seaborn as sns

df_iris = sns.load_dataset('iris')

df_iris_chart = alt.Chart(df_iris).mark_circle().encode(
    x='petal_length',
    y='petal_width',
    color='species',
).interactive()


# Use the native Altair theme.
st.altair_chart(df_iris_chart, theme=None, use_container_width=True)