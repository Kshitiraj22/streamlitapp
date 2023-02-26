import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
image = Image.open("titanic.jpg")
# Load Titanic dataset
@st.cache
def load_data():
    df = pd.read_csv("titanic.csv")
    return df

df = load_data()

# Add a title to the Streamlit app
st.title('Titanic Data Visualization')
st.image(image, caption='Kashti')

# Add a sidebar with options for selecting which plots to show
show_gender_plot = st.sidebar.checkbox('Show Survival Rate by Gender Plot', value=True)
show_age_plot = st.sidebar.checkbox('Show Age Distribution of Passengers Plot', value=True)
show_class_plot = st.sidebar.checkbox('Show Survival Rate by Passenger Class Plot', value=True)

# Add a selectbox to choose a gender for the histogram plot
gender_options = df['sex'].unique().tolist()
selected_gender = st.sidebar.selectbox('Select a gender to plot:', gender_options)

# Plot survival rate by gender
if show_gender_plot:
    survival_rate_by_gender = df.groupby(['sex'])['survived'].mean()
    fig, ax = plt.subplots()
    ax.bar(survival_rate_by_gender.index, survival_rate_by_gender.values)
    ax.set_title('Survival Rate by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Survival Rate')
    st.pyplot(fig)

# Plot age distribution of passengers
if show_age_plot:
    fig, ax = plt.subplots()
    ax.hist(df[df['sex'] == selected_gender]['age'].dropna(), bins=20)
    ax.set_title(f'Age Distribution of {selected_gender} Passengers')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Plot survival rate by passenger class
if show_class_plot:
    survival_rate_by_class = df.groupby(['parch'])['survived'].mean()
    fig, ax = plt.subplots()
    ax.bar(survival_rate_by_class.index, survival_rate_by_class.values)
    ax.set_title('Survival Rate by Passenger Class')
    ax.set_xlabel('Passenger Class')
    ax.set_ylabel('Survival Rate')
    st.pyplot(fig)

# Add a table showing summary statistics for the dataset
st.write('## Summary Statistics')
st.write(df.describe())
