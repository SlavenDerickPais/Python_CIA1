import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



#Read the historical dataset
hist=pd.read_csv("historical_silver_price.csv")
#to show the historiacal price chart with the given filter ≤ 20,000 INR per kgBetween 20,000 and 30,000 INR per kg≥ 30,000 INR per kg

st.table(hist.head())
st.title("Historical Pice Chart of Silver")
price_filter=st.selectbox("Select Price Filter",["≤ 20,000 INR per kg","Between 20,000 and 30,000 INR per kg","≥ 30,000 INR per kg"])
if price_filter=="≤ 20,000 INR per kg":
    filtered_data=hist[hist['Silver_Price_INR_per_kg']<=20000]
elif price_filter=="Between 20,000 and 30,000 INR per kg":
    filtered_data=hist[(hist['Silver_Price_INR_per_kg']>20000) & (hist['Silver_Price_INR_per_kg']<=30000)]
else:
    filtered_data=hist[hist['Silver_Price_INR_per_kg']>30000]
st.line_chart(filtered_data.set_index('Year')['Silver_Price_INR_per_kg'])
st.write("Data Source: historical_silver_price.csv")
st.write("This chart shows the historical price of silver based on the selected price filter.")
st.write("You can analyze the trends in silver prices over time with different price ranges.")

# Allow users to enter: Weight of silver (in grams or kilograms) and Current price of silverper gram. Calculate and display the total cost of silver based on the input values. Provide acurrency conversion option (INR to USD or other currency). 
st.title("Silver Cost Calculator")
weight_unit=st.selectbox("Select Weight Unit",["grams","kilograms"])
weight=st.number_input("Enter Weight of Silver",min_value=0.0,step=0.01)
current_price_per_gram=st.number_input("Enter Current Price of Silver per gram (INR)",min_value=0.0,step=0.01)
if weight_unit=="kilograms":
    weight_in_grams=weight
else:
    weight_in_grams=weight
total_cost_inr=weight_in_grams*current_price_per_gram
currency=st.selectbox("Select Currency",["INR","USD"])
if currency=="USD":
    conversion_rate=0.012 # Example conversion rate
    total_cost=total_cost_inr*conversion_rate
    st.write(f"Total Cost of Silver: {total_cost:.2f} USD")
else:
    st.write(f"Total Cost of Silver: {total_cost_inr:.2f} INR")

# load the state-wise data 

state_wise =pd.read_csv("state_wise_silver_purchased_kg.csv")
st.title("State-wise Silver Purchased")
st.dataframe(state_wise)
 
# #import inida shape file Load the provided state-wise silver purchase dataset into the Streamlit application. Displayan India state-wise map using GeoPandas, where darker shades represent higher silverpurchases (in kg).
import geopandas as gpd
# india_states = gpd.read_file("/Users/slaven/Downloads/MCA/IIIrd SEM/APP/cia1/India Shape/india_st.shp")
# state_wise.columns=['State','Silver_Purchased_kg']
# india_states = india_states.merge(state_wise, left_on='st_nm', right_on='State', how='left')
# india_states['Silver_Purchased_kg'] = india_states['Silver_Purchased_kg'].fillna(0)

# To display the sate with top 5 silver purchased
st.title("Sate wise Top 5 Siver Purchasers")
sorted_states=state_wise.sort_values(by='Silver_Purchased_kg',ascending=False).head(5)
st.bar_chart(sorted_states.set_index('State')['Silver_Purchased_kg'])
st.write("This bar chart displays the top 5 states with the highest silver purchases in kg.")
# st.title("India State-wise Silver Purchased Map")
# fig, ax = plt.subplots(1, 1, figsize=(10, 10))
# india_states.plot(column='Silver_Purchased_kg', ax=ax, legend=True,legend_kwds={'label': "Silver Purchased (kg)", 'orientation': "horizontal"},cmap='OrRd', missing_kwds={"color": "lightgrey"})
# ax.set_title("India State-wise Silver Purchased (kg)")
# ax.axis('off')
# st.pyplot(fig)
# st.write("This map visualizes the silver purchased (in kg) across different states in India. Darker shades indicate higher purchases.")

# Trend Analysis of January Monthly Silver Purchases
st.title("January Monthly Silver Purchases Trend")
# For demonstration, let's assume January purchases are 5% of the annual price
hist['January_Silver_Purchase_kg'] = hist['Silver_Price_INR_per_kg'] * 0.05
st.line_chart(hist.set_index('Year')['January_Silver_Purchase_kg'])
st.write("This line chart shows the trend of January monthly silver purchases (in kg) over the years based on historical silver prices.")



