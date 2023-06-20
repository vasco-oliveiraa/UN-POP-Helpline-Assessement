import streamlit as st

from Form import form
from Results import results

def app():
    # Set the page configuration
    st.set_page_config(
    page_title="UN Pop",
    page_icon="child",
    #layout="wide",
    #initial_sidebar_state="expanded",
    menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "mailto:vasco.oliveira260@gmail.com?subject=UN Pop - Bug Report",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    }
    )
    
    form()

if __name__ == "__main__":
    app()
    
    
