import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Heart Disease Risk Prediction

## Fill out the Following Questions:
"""

st.title("Personal Detail Question")
username = st.text_input("Enter your name")
sex = st.radio("Select Gender:", ("Male", "Female"))
age = st.selectbox("Select Age Group:", ["Select One", "18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54",
                                        "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"])
race = ("Select Race:", ["Select One", "White", "Hispanic", "Black", "Asian", "American Indian/Alaskan Native"])
height_unit = st.selectbox("Select Height Unit:", ["Centimeters", "Feet and Inches"])

if height_unit == "Centimeters":
  cm_height = st.slider("Select Height (in centimeters):", min_value=100, max_value=250)
else:
  feet_height = st.selectbox("Enter Height in Centimeters:", range(3, 8))
  inch_height = st.selectbox("Enter Height in Centimeters:", range(0, 12))

weight_unit = st.selectbox("Select Height Unit:", ["kg", "lb"])

if weight_unit == "kg":
  # kg_weight = st.selectbox("Select Weight (in kilograms):", [f"{weight:.2f}" for weight in range(30, 151)])
  if 'weight' not in st.session_state:
    st.session_state.weight = 70.0
  if st.button('-'):
    st.session_state.weight = max(30.0, st.session_state.weight - 0.01)
  if st.button('+'):
    st.session_state.weight = min(150.0, st.session_state.weight + 0.01)

# Display the adjusted weight
#st.success(f"Adjusted Weight: {st.session_state.weight:.2f} kg")
else:
  lb_weight = st.selectbox("Enter Height in Centimeters:", range(60, 301))

"""
sleep = 
activity = 
smoking = 
drinking =

genhealth = 
physicalhealth =
mentalhealth =
diffwalking = 
asthma = 




Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
