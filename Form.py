import streamlit as st
from time import sleep

def form():
    st.title("Digital Channel and Helpline Assessment Form")
    
    intro_text = """
Welcome to the Digital Channel and Helpline Assessment Form. This form aims to gather information about the implementation, effectiveness, and accessibility of digital channels and helpline services in your country.

Please rate each question on a scale from 1 to 5, where 1 is the lowest and 5 is the highest. Your feedback will help us improve and enhance the support provided to children in need.
"""
    st.write(intro_text)
    
    # if st.button("Let's get started!"):

    with st.form("assessment_form"):

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
            st.success('Submitted! Check Your Score Now!')
            sleep(1)