import streamlit as st
from streamlit_option_menu import option_menu

from Form import form

from ScoreComparison import score_comparison
from Recommendations.Recommendations import recommendations


def app():
    # Set the page configuration
    st.set_page_config(
    page_title="UN POP - Helpline Assessment",
    page_icon="child",
    #layout="wide",
    #initial_sidebar_state="expanded",
    menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "mailto:vasco.oliveira260@gmail.com?subject=UN Pop - Bug Report",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    }
    )
    
    if 'user_scores' not in st.session_state:
        st.session_state['user_scores'] = None
    
    if 'selected' not in st.session_state:
        st.session_state['selected'] = None
        
    selected = option_menu(
            menu_title = None,
            options = ['Assessment Form', 'Score Comparison', 'Recommendations'],
            icons = ['file-text', 'bar-chart', 'lightbulb'],
            menu_icon = 'cast',
            default_index = 0,
            orientation = 'horizontal'
        )

    if selected == 'Assessment Form':
        form()
    if selected == 'Score Comparison':
        score_comparison(st.session_state['user_scores'])
    if selected == 'Recommendations':
        recommendations(st.session_state['user_scores'])

if __name__ == "__main__":
    app()
    
    
