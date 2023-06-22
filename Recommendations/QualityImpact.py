import streamlit as st

def quality_impact():
    
    # Page title and description
    st.title("Quality and Service")
    
    # Divider
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
            
        st.metric('Likelihood',value='Possible')
        
    with col2:
        
        st.metric('Severity',value='Unacceptable')
        
    with col3:
        
        st.metric('Risk',value='High')

    # Divider
    st.divider()

    # Explanation
    st.subheader("Why is it important?")
    st.write("Ensuring high quality and service standards is essential for digital channels and helplines aimed at helping children. Delivering excellent service ensures that children receive the support they need in a professional and compassionate manner. Quality service builds trust, instills confidence, and encourages children to seek help. By prioritizing quality and service, countries can provide an effective and impactful support system for children in need.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Define Service Standards and Protocols
    with st.expander("1. Define Service Standards and Protocols"):
        st.write("Establish clear service standards and protocols for digital channels and helplines. Define guidelines for communication, active listening, problem-solving, and handling sensitive information. Ensure that staff members are trained and adhere to these standards, ensuring consistent and high-quality service delivery.")

    # Recommendation 2: Empower Staff with Training and Resources
    with st.expander("2. Empower Staff with Training and Resources"):
        st.write("Invest in comprehensive training programs for staff members to equip them with the necessary skills and knowledge to provide quality service. Train them in areas such as active listening, empathy, trauma-informed care, and cultural sensitivity. Provide resources, such as reference materials and toolkits, to support staff in addressing various issues and providing appropriate guidance to children.")

    # Recommendation 3: Implement Quality Assurance Mechanisms
    with st.expander("3. Implement Quality Assurance Mechanisms"):
        st.write("Establish quality assurance mechanisms to monitor and evaluate the service provided through digital channels and helplines. Conduct regular audits, reviews, or case evaluations to assess service quality, adherence to protocols, and identify areas for improvement. Utilize feedback from children, parents, and other users to continuously enhance the service and address any shortcomings.")

    # Recommendation 4: Foster Collaboration and Partnerships
    with st.expander("4. Foster Collaboration and Partnerships"):
        st.write("Collaborate with relevant stakeholders and partners to enhance service quality and expand support options. Engage with child protection organizations, mental health professionals, legal experts, and community organizations to leverage their expertise and resources. Foster collaborations that enable a comprehensive and holistic approach to support children effectively.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Ensuring high quality and service standards is crucial for digital channels and helplines aimed at supporting children. By implementing the recommendations mentioned above, countries can provide a supportive and reliable system that meets the diverse needs of children, ensuring their safety and well-being.")
    