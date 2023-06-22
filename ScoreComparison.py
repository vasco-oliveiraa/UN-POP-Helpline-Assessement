import streamlit as st
from ModelScoring import model_scoring
from RadarChart import radar_chart

def score_comparison(user_scores):
    
    if st.session_state['user_scores']:
    
        final_score = model_scoring(user_scores, output='final_score')

        st.title('Score Comparison')

        col1, col2, col3 = st.columns([3,2,3])
        
        with col1:
            st.empty()

        with col2:

            st.metric(label='Your Helpline Score',value="{:.2f}%".format(final_score))
        
        with col3:
            st.empty()
            
        with st.expander('How is this score calculated?'):
            st.markdown('''
            Your score was determined using an *AHP (Analytic Hierarchy Process)* model, which considered your responses and adjusted them according to the importances defined through expert insights. This approach enhances decision-making by distributing weights to certain areas and highlighting any shortcomings in these crucial areas.
            ''')

        tab1, tab2 = st.tabs(['Weighted Score Comparison','Non-Weighted Scores'])

        with tab1:
            st.markdown('''
            The graph below is a *weighted* representation of the scores you provided, adjusted to the importances provided by expert insights.Here you can visualize which areas represent the most opportunity for improvement, by looking at those with the greatest distance between *Your Score* and the *Target Score*.
            You can also determine the areas considered most important by the experts, by looking at those closer to the border of the circle.
            ''')
            fig = radar_chart(user_scores,version=2)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.markdown('The graph below is a non-weighted representation of the scores you provided for each area. Here you can easily visualize the absolute state of your helpline in regards to the areas evaluated.')
            fig = radar_chart(user_scores,version=1)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.write('Please submit the form to display the score comparison')