#imports here
import matplotlib.pyplot as plt
import streamlit as st

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

st.header("A simple figure with st.pyplot!")
st.pyplot(fig)
