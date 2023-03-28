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
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice= streamlit.text_input("What fruit would you like information about?", 'Kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("http://fruityvice.com/api/fruit/"+fruit_choice)                             

#take the json version of the response and normalize it
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output of the screen  as a table
streamlit.dataframe(fruityvice_normalized)
