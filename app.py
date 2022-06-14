#imports here
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpld3
import streamlit.components.v1 as components

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

st.pyplot(fig)
