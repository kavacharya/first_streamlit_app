
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + this_fruit_choice)                             
 #take the json version of the response and normalize it
 fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
  
#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please select a fruit to get information")
 else:
  back_from_function=get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
      my_cur.execute("Select * from fruit_load_list")
      return my_cur.fetchall()
 
if streamlit.button('Get fruit load list'):
 my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)
 
def insert_row_snowflake(new_fruit):
 with my_cnx.cursor as my_cur:
  my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit')")
  return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('what fruits would you like to add?')
if streamlit.button('Add a fruit to the list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 back_from_function = insert_row_snowflake(add_my_fruit)
 streamlit.text(back_from_function)


