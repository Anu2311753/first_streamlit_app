import streamlit

streamlit.title('My Parents New Healthy Dinnerr')

streamlit.header('Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔🥑Hard-Boiled Free-Range Egg')
streamlit.text('🍞Avocado toast')


streamlit.header('🥗🥣Build your own fuit smoothie🐔🥑')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
