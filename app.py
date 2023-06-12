import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
import plotly as px
from plotly import graph_objects as GO

data = pd.read_csv("DATA/eda_data.csv")

# data Cleaning
columns = data.columns
check_columns = ['Job Title', 'avg_salary', 'Industry', "Location"]
drop_columns = [col for col in columns if col not in check_columns]

# removing outliers
# mask = data["Location"] != "New York, NY"
# data = data[mask]

# create new columns for iso of location

df = data.drop(columns=drop_columns)
df.dropna()
# print("df shape:  ", df.shape)

st.title("Salary Prediction App")
st.header("Predicting Average Salary with Location")
nav = st.sidebar.radio(label="Navigation", options=["Home", "Prediction", "Contribute"])

if nav == "Home":
    st.image("DATA/salaryPred.jpeg", width=300)
elif nav == "Prediction":
    st.write("Predict")
else:
    st.write("Contrib")

st.header("Histogram of Location")
fig = plt.figure(figsize=(10, 5))
df["Location"].hist(bins=10)
plt.xlabel("Location")
plt.title("Distribution of Location")
st.pyplot(fig=fig)


st.header("Line chart of Location Vs Average Salary")
st.line_chart(data=df, x="Location", y="avg_salary")

# st.header("Location Vs Salary")
# fig = plt.figure(figsize=(10, 5))
# df.plot(x="Location", y="avg_salary")
# plt.xlabel("Location")
# plt.ylabel("Salary")
# plt.title("Distribution of Location")
# st.pyplot(fig=fig)


check_box = st.checkbox("Show Table")
graph = st.selectbox("What kind of graph?", ["Interactive", "Non-Interactive"])
if graph == "Non-Interactive":
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(x=df["Location"], y=df["avg_salary"])
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
