import streamlit as st
import snowflake.connector
from pathlib import Path
import time
import pandas as pd
from st_pages import Page, show_pages, show_pages_from_config, add_page_title
st.set_page_config(
  page_title="Leetcodeforsnowflake",
  page_icon="  ",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# Function to store Snowflake credentials in session state
def store_credentials(account, role, warehouse, database, schema, user, password):
    st.session_state.account = account
    st.session_state.role = role
    st.session_state.warehouse = warehouse
    st.session_state.database = database
    st.session_state.schema = schema
    st.session_state.user = user
    st.session_state.password = password

# Function to connect to Snowflake
# @st.cache    
# Create a Snowflake connection function
   
def create_snowflake_connection(account, role, warehouse, database, schema, user, password):
    try:
        conn = snowflake.connector.connect(
            account='mx31337.ca-central-1.aws', #account,
            role='ACCOUNTADMIN',#role,
            warehouse='COMPUTE_WH',##warehouse,
            database='DB',#database,
            schema='SCH',#schema,
            user='learnatozaboutdata04',#user,
            password='Learnatozaboutdata04@123#',#password,
            client_session_keep_alive=True
        )
        st.toast("Connection to Snowflake successfully!", icon='🎉')
        time.sleep(.5)
        st.balloons()
    except Exception as e:
        st.error(f"Error connecting to Snowflake: {str(e)}")    
    # return conn
with st.sidebar:
    show_pages(
                [
                    Page("snowflakesql.py", "Home", "🏠"),
                    Page("pages\Leet570.py", "Managers with at Least 5 Direct Reports", "1️⃣")
                ]
            )  
    st.markdown("[![Foo](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/mahantesh-hiremath/) Connect me.")
    st.sidebar.header("Snowflake Credentials")
    expander = st.expander("Set Up SF Connection")
    account = expander.text_input('Acount','mx31337.ca-central-1')
    role = expander.text_input('Role','ACCOUNTADMIN')
    warehouse = expander.text_input('Warehouse','COMPUTE_WH')
    database = expander.text_input('Database','DB')
    schema = expander.text_input('Schema','SCH')
    user = expander.text_input('User','learnatozaboutdata04')
    password = expander.text_input("Password", type="password")
    if expander.button("Connect"):
        store_credentials(account, role, warehouse, database, schema, user, password)
        # create_snowflake_connection(account, role, warehouse, database, schema, user, password)
# add_page_title()

# show_pages_from_config()









def main(): 
    st.title('1st Step App')

    # ... (other parts of your code)

    if st.sidebar.button("myconnn"):
        connection = create_snowflake_connection(
            st.session_state.account, st.session_state.role, st.session_state.warehouse,
            st.session_state.database, st.session_state.schema, st.session_state.user,
            st.session_state.password
        )
        
        # Use the 'connection' object as needed
        if connection:
            # Perform operations with the 'connection'
            pass
        else:
            st.error("Snowflake connection could not be established.")

st.write(st.session_state.account)
st.write(st.session_state.role)
st.write(st.session_state.warehouse)
st.write(st.session_state.database)
st.write(st.session_state.schema)
st.write(st.session_state.user)
st.write(st.session_state.password)
# st.write(create_snowflake_connection(account,',', role,',', warehouse,',', database,',', schema,',', user,',', password))

if __name__ == "__main__":
    main()
