# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(f"Example Streamlit App :balloon: {st.__version__}")
st.header("List of fruits own by dinanath")


# Get the current credentials
#session = get_active_session()
cnx=st.connection("Snowflake")
session = cnx.session()

sql = """ select * from FRUIT_OPTIONS where FRUIT_ID in (2,5,6)
"""
results = session.sql(sql).collect()
st.write(results)



session = get_active_session()

my_df=session.table("FRUIT_OPTIONS").select(col('FRUIT_NAME'))
#editable_df = st.data_editor(my_df)

ingredients_list = st.multiselect('choose upto 5 items:',my_df)

if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)

    ingredients_string = ''
    name_on_order = 'Sham'
#To convert the LIST to a STRING we can add a FOR LOOP block. A FOR LOOP will repeat once FOR every value in the LIST. 

    for fruit_chosen in ingredients_list:
       ingredients_string += fruit_chosen + ' '
       name_on_order = 'Sham'
    # st.write(ingredients_string)


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)
    #st.stop()
    # if ingredients_string:
    #     session.sql(my_insert_stmt).collect()
    #     st.success('Your Smoothie is ordered!', icon="✅")
    time_to_insert = st.button('Placed your order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success ('Your Smoothie is ordered!', icon="✅")
