import streamlit as st
from ModelScoring import model_scoring
from RadarChart import radar_chart

def results(user_scores):
    
    final_score = model_scoring(user_scores, output='final_score')
    
    with st.container():
    
        st.title('Your Results')

        col1, col2, col3 = st.columns([3,2,3])

        with col2:

            st.metric(label='Your Helpline Score',value=str(final_score)+'%')
        
        tab1, tab2 = st.tabs(['User Inputs','Comparison'])

        with tab1:
            fig = radar_chart(user_scores,version=1)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            fig = radar_chart(user_scores,version=2)
            st.plotly_chart(fig, use_container_width=True)