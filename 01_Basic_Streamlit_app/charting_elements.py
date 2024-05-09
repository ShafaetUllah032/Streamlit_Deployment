import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import folium

st.divider()

df=pd.read_csv("../NOTEBOOK/data/sample.csv")

st.write(df)


# ploting line plot

st.line_chart(df,x="year",y=["col1","col2","col3"])

# Streamlit area chart 

st.area_chart(df,x="year",y=["col1","col2","col3"],color=["#abcdef","#04ff0a","#00aaf0"])


# Streamlit bar chart

st.bar_chart(df,x="year",y=["col1","col2","col3"],color=["#abcdef","#04ff0a","#00aaf0"])

st.divider()

df2=pd.read_csv("../NOTEBOOK/data/sample_map.csv")

st.write(df2)

# Steamlit map

st.map(df2,latitude="Latitude",longitude="Longitude")


# Matplotlib
# Sample DataFrame
data = {
    'Location': ['Dhaka', 'Chittagong', 'Cox\'s Bazar', 'Sylhet', 'Sundarbans'],
    'Latitude': [23.8103, 22.3569, 21.4272, 24.8949, 21.9497],
    'Longitude': [90.4125, 91.7832, 92.0058, 91.8687, 89.1833]
}
df = pd.DataFrame(data)

# Create a matplotlib figure
fig, ax = plt.subplots()

# Plot points
ax.scatter(df['Longitude'], df['Latitude'], color='red')

# Plot line
ax.plot(df['Longitude'], df['Latitude'], linestyle='-', color='blue')

# Customize plot
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Map with Line')

# Display plot in Streamlit
st.pyplot(fig)
