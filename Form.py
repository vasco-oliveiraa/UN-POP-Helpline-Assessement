import streamlit as st
import pycountry

from GetCountryFromIP.GetCountryFromIP import get_country_from_ip
from GetCountryFromIP.GetIPAddress import get_ip_address

from ModelScoring import model_scoring
from RadarChart import radar_chart

def form():
    st.title("Digital Channel and Helpline Assessment Form")

    with st.form("assessment_form"):
        
        ip_address = get_ip_address()

        country = get_country_from_ip(ip_address)

        # Get a list of all country names
        countries = [country.name for country in pycountry.countries]

        # Create a dropdown in Streamlit
        selected_country = st.selectbox('Select a country', countries,index=countries.index(country))

        
        st.write("Please rate the following questions on a scale from 1 to 5, where 1 is the lowest and 5 is the highest.")

        digital_channel = st.slider(
            "In which phase of the digital channel implementation is your country?",
            1,
            5
        )

        tech_stack = st.slider(
            "How complete is your country's technology stack for digital channels?",
            1,
            5
        )

        fundraise_strategy = st.slider(
            "How confident are you in your fundraise strategy to cover your cost in the short and long term?",
            1,
            5
        )

        confidentiality = st.slider(
            "To what extent does your helpline maintain confidentiality and ensure the privacy of children seeking help?",
            1,
            5
        )

        responsiveness = st.slider(
            "How satisfied are you with the timeliness and responsiveness of helpline services in addressing children's needs?",
            1,
            5
        )

        quality_impact = st.slider(
            "How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?",
            1,
            5
        )

        staff_knowledge = st.slider(
            "How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?",
            1,
            5
        )

        cultural_linguistic_needs = st.slider(
            "To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?",
            1,
            5
        )

        age_appropriate_guidance = st.slider(
            "How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages?",
            1,
            5
        )

        accessibility = st.slider(
            "How accessible are helplines for children in terms of availability and ease of contact?",
            1,
            5
        )

        submit_button = st.form_submit_button("Submit")
        if submit_button:
            
            user_scores = {
                'digital_channel': digital_channel,
                'tech_stack': tech_stack,
                'fundraise_strategy': fundraise_strategy,
                'confidentiality': confidentiality,
                'responsiveness': responsiveness,
                'quality_impact': quality_impact,
                'staff_knowledge': staff_knowledge,
                'cultural_linguistic_needs': cultural_linguistic_needs,
                'age_appropriate_guidance': age_appropriate_guidance,
                'accessibility': accessibility,
            }
            
            st.success("Thank you for your submission!")
            
            final_score = model_scoring(user_scores, output='final_score')
            
            st.write(f'Your score is {final_score}%')
            
            tab1, tab2 = st.tabs(['User Inputs','Comparison'])
            
            with tab1:
                fig = radar_chart(user_scores,version=1)
                st.plotly_chart(fig)
                
            with tab2:
                fig = radar_chart(user_scores,version=2)
                st.plotly_chart(fig)
            
            
            
            
            
            
            
            