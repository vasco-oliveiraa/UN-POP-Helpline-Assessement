import streamlit as st

def age_appropriate_guidance():
    
    # Page title and description
    st.title("Age-Appropriate Guidance")
    
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
    st.write("Providing age-appropriate guidance is crucial for effectively addressing the needs and concerns of children in digital channels and helplines. Children of different ages have varying levels of understanding, communication skills, and developmental needs. By offering guidance that is tailored to their age and developmental stage, countries can ensure that children receive relevant information, support, and services, leading to more effective responses and improved outcomes.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Develop Age-Specific Guidance Materials
    with st.expander("1. Develop Age-Specific Guidance Materials"):
        st.write("Create age-specific guidance materials that are tailored to the developmental needs and understanding of children at different stages. Design informative and engaging resources, such as videos, interactive websites, or downloadable materials, that address age-appropriate topics, risks, and protective measures. Collaborate with child psychologists, educators, and child development experts to ensure the accuracy and effectiveness of the materials.")

    # Recommendation 2: Train Staff on Age-Appropriate Communication
    with st.expander("2. Train Staff on Age-Appropriate Communication"):
        st.write("Provide training to staff members on age-appropriate communication techniques when interacting with children. Equip them with the knowledge and skills to adapt their language, tone, and methods to effectively engage and support children of different ages. Incorporate strategies for active listening, empathy, and understanding the unique needs of each age group.")

    # Recommendation 3: Implement Effective Service Routing
    with st.expander("3. Implement Effective Service Routing"):
        st.write("Develop a service routing system that effectively directs children to the appropriate resources and support based on their age and specific needs. Use interactive tools, questionnaires, or chatbots to gather information about the child's age, concerns, and requirements. Based on this information, route them to the most relevant services, including age-appropriate counseling, information resources, or specialized support.")

    # Recommendation 4: Engage Child Advocates and Youth Representatives
    with st.expander("4. Engage Child Advocates and Youth Representatives"):
        st.write("Involve child advocates, youth representatives, or child advisory groups in the development and evaluation of digital channels and helplines. Seek their input to ensure that the guidance provided is relevant, engaging, and resonates with children of different ages. Incorporate their feedback to continuously improve the services and make them more age-appropriate.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Providing age-appropriate guidance is crucial for effectively supporting children through digital channels and helplines. By implementing the recommendations mentioned above, countries can ensure that children receive relevant information, support, and services that address their unique age and developmental needs.")