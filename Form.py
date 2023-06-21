import streamlit as st
import pycountry
from time import sleep

from GetCountryFromIP.GetCountryFromIP import get_country_from_ip

from Results import results
from Recommendations.Recommendations import recommendations

def form():
    st.title("Digital Channel and Helpline Assessment Form")
    
    intro_text = """
Welcome to the Digital Channel and Helpline Assessment Form. This form aims to gather information about the implementation, effectiveness, and accessibility of digital channels and helpline services in your country. Please rate each question on a scale from 1 to 5, where 1 is the lowest and 5 is the highest. Your feedback will help us improve and enhance the support provided to children in need.

Let's get started!
"""
    st.write(intro_text)
    
    country = None
    
    col1, col2 = st.columns([5,2])
    
    with col2:
        
        st.write('')
        st.write('')
        if st.button('Use my location', use_container_width=True):

            with st.spinner('Checking IP Address'):

                country = get_country_from_ip()
                
    with col1:
        
        # Get a list of all country names
        countries = [country.name for country in pycountry.countries]
        countries.append('Select a country')

        if country and (country!="Unknown"):
            # Create a dropdown in Streamlit
            country = st.selectbox('Country*', countries, index=countries.index(country))
            st.session_state['country'] = country

        else:
            # Create a dropdown in Streamlit
            country = st.selectbox('Country*', countries, index=countries.index('Select a country'))
            if country in countries:
                st.session_state['country'] = country
            
    with st.form("assessment_form"):        

        st.write("Please rate the following questions on a scale from 1 to 5, where 1 is the lowest and 5 is the highest.")

        st.subheader("Digital Channel Implementation")
        digital_channel_implementation = st.slider(
            "In which phase of the digital channel implementation is your country?",
            1,
            5
        )

        st.subheader("Technology Stack")
        technology_stack = st.slider(
            "How complete is your country's technology stack for digital channels?",
            1,
            5
        )

        st.subheader("Fundraising Strategy")
        fundraise_strategy = st.slider(
            "How confident are you in your fundraise strategy to cover your cost in the short and long term?",
            1,
            5
        )

        st.subheader("Confidentiality and Data Protection")
        confidentiality_data_protection = st.slider(
            "To what extent does your helpline maintain confidentiality and ensure the privacy of children seeking help?",
            1,
            5
        )

        st.subheader("Responsiveness")
        responsiveness = st.slider(
            "How satisfied are you with the timeliness and responsiveness of helpline services in addressing children's needs?",
            1,
            5
        )

        st.subheader("Quality and Impact")
        quality_impact = st.slider(
            "How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?",
            1,
            5
        )

        st.subheader("Staff Expertise")
        staff_expertise = st.slider(
            "How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?",
            1,
            5
        )

        st.subheader("Cultural and Linguistic Needs")
        cultural_linguistic_needs = st.slider(
            "To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?",
            1,
            5
        )

        st.subheader("Age-Appropriate Guidance")
        age_appropriate_guidance = st.slider(
            "How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages?",
            1,
            5
        )

        st.subheader("Accessibility")
        accessibility = st.slider(
            "How accessible are helplines for children in terms of availability and ease of contact?",
            1,
            5
        )

        submit_button = st.form_submit_button("Submit")
        if submit_button:

            user_scores = {
                'digital_channel_implementation': digital_channel_implementation,
                'technology_stack': technology_stack,
                'fundraise_strategy': fundraise_strategy,
                'confidentiality_data_protection': confidentiality_data_protection,
                'responsiveness': responsiveness,
                'quality_impact': quality_impact,
                'staff_expertise': staff_expertise,
                'cultural_linguistic_needs': cultural_linguistic_needs,
                'age_appropriate_guidance': age_appropriate_guidance,
                'accessibility': accessibility,
            }
            
            st.session_state['user_scores'] = user_scores
            
            
