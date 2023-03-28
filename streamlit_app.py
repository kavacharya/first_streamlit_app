import streamlit
import pandas
import requests

streamlit.title('My parents new Healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭Build your own smoothie 🥝🍇')

my_fruits_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list=my_fruits_list.set_index('Fruit')
fruits_selected=streamlit.multiselect('Pick some fruits', list(my_fruits_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
fruityvice_response = requests.get("http://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())                                 

