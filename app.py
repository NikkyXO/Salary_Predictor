import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly as px
from plotly import graph_objects as GO

data = pd.read_csv("DATA/eda_data.csv")

# data Cleaning
columns = data.columns
check_columns = ['Job Title', 'avg_salary', 'Industry', "Location"]
drop_columns = [col for col in columns if col not in check_columns]

df = data.drop(columns=drop_columns)
df.dropna()
print("df shape:  ", df.shape)



st.title("Salary Prediction App")

nav = st.sidebar.radio(label="Navigation", options=["Home", "Prediction", "Contribute"])

if nav == "Home":
    st.image("DATA/salaryPred.jpeg", width=300)
elif nav == "Prediction":
    st.write("Predict")
elif nav == "Contribute":
    st.write("Contrib")

st.header("Histogram of average Price")
fig = plt.figure(figsize=(10, 5))
df["avg_salary"].hist()
st.pyplot(fig=fig)

st.header("Box Plot of  Average Salary")
fig, ax = plt.subplots(figsize=(15, 6))
df["avg_salary"].plot(kind="box", vert=False, title="Distribution of Average salary", ax=ax)
st.pyplot(fig=fig)

st.header("Line chart of Location Vs Average Salary")
st.line_chart(data=df, x="Location", y="avg_salary")



check_box = st.checkbox("Show Table")
graph = st.selectbox("What kind of graph?", ["Interactive", "Non-Interactive"])
if graph == "Non-Interactive":
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(x=df["Job Title"], y=df["avg_salary"])
    plt.ylim(0)
    plt.xlabel("Location of Job")
    plt.ylabel("Average Salary")
    plt.tight_layout()
    st.pyplot(fig=fig)
else:
    pass
    # layout = GO.Layout(xaxis=dict(range=[0, 15, 2]), yaxis=dict(range=[0, 2300000]))
    #
    # fig = GO.Figure(data=GO.Scatter(xaxis=dict(range=[0, 15, 2]), yaxis=dict(range=[0, 2300000])))

if check_box:
    st.table(df.head())  # Job TiTle
