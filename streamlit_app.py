import streamlit
import pandas
import requests
import snowflake.connector
from urlib.error import URL Error
streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, Spinch & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
s
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe (fruits_to_show)
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice")
  fruityvice_normalized = pandas.json_normalized(fruityvice_response.json())
  return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!") 
try:
    fruitchoice = streamlit.text_input('what fruit would you like information about?')
    if not fruit_choice:
       streamlit.error("please select a fruit to get information.")
    else:                                 
        back_from_function = get_fruitvice_data(fruit_choice)                             
        streamlit.dataframe(back_from_function)                             
except URL Error as e:
  streamlit.error()
streamlit.stop()
                                     
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()                                    
warehouse = "pc_rivery_wh"                                     
database = "pc_rivery_db"                                     
schema = "public"  
my_cur.execute(" USE WAREHOUSE PC_RIVERY_WH")
my_cur.execute("SELECT * From PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()                                     
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)                                     
add_my_fruit = streamlit.text_input('what fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding',add_my_fruit)
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')") 
