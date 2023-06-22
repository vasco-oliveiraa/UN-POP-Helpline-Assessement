import streamlit as st

def cultural_linguistic_needs():
    
    # Page title and description
    st.title("Cultural and Linguistic Needs")
    
    # Divider
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
            
        st.metric('Likelihood',value='Possible')
        
    with col2:
        
        st.metric('Severity',value='Tolerable')
        
    with col3:
        
        st.metric('Risk',value='Medium')

    # Divider
    st.divider()

    # Explanation
    st.subheader("Why is it important?")
    st.write("Addressing cultural and linguistic needs is crucial for effective communication in digital channels and helplines aimed at helping children. Recognizing and respecting cultural diversity, as well as providing language accessibility, ensures that children from various backgrounds can access support services without barriers. By prioritizing cultural and linguistic needs, countries can enhance the quality of communication, promote inclusivity, and provide culturally responsive assistance to children in need.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Ensure Language Accessibility
    with st.expander("1. Ensure Language Accessibility"):
        st.write("Provide language accessibility options for children who may require assistance in languages other than the national or dominant language. Offer multilingual helpline services, translation support, or interpretation services to ensure effective communication. Collaborate with language experts, interpreters, and translators to bridge the language gap and meet the linguistic needs of children.")

    # Recommendation 2: Promote Cultural Sensitivity and Awareness
    with st.expander("2. Promote Cultural Sensitivity and Awareness"):
        st.write("Implement cultural sensitivity training for staff members to enhance their understanding of different cultures, customs, and beliefs. Promote awareness of cultural norms, values, and potential biases that may influence interactions with children. Encourage staff to be open-minded, non-judgmental, and respectful of diverse cultural backgrounds when communicating with children and their families.")

    # Recommendation 3: Tailor Communication Approaches
    with st.expander("3. Tailor Communication Approaches"):
        st.write("Adapt communication approaches to meet the cultural and linguistic needs of children. Consider using visual aids, storytelling, or creative methods to convey information effectively. Employ plain language, avoid jargon, and explain complex concepts in a clear and understandable manner. Tailor communication styles to match the preferences and comfort levels of children from different cultural backgrounds.")

    # Recommendation 4: Engage Cultural Mediators and Community Representatives
    with st.expander("4. Engage Cultural Mediators and Community Representatives"):
        st.write("Collaborate with cultural mediators, community representatives, and organizations working with specific cultural communities. Seek their expertise, guidance, and support in understanding cultural nuances and effective communication strategies. Involve them in the development and implementation of digital channels and helplines to ensure the cultural appropriateness of the services provided.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Addressing cultural and linguistic needs is essential for ensuring the quality of communication in digital channels and helplines. By implementing the recommendations mentioned above, countries can promote inclusivity, cultural responsiveness, and effective support for children from diverse cultural backgrounds.")