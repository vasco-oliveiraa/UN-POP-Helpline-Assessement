import streamlit as st

def staff_expertise():
    
    # Page title and description
    st.title("Staff Expertise")
    
    # Divider
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
            
        st.metric('Likelihood',value='Probable')
        
    with col2:
        
        st.metric('Severity',value='Tolerable')
        
    with col3:
        
        st.metric('Risk',value='Medium')

    # Divider
    st.divider()

    # Explanation
    st.subheader("Why is it important?")
    st.write("Staff expertise plays a vital role in ensuring the effectiveness and customer satisfaction of digital channels and helplines aimed at helping children. Well-trained and knowledgeable staff members can provide accurate information, offer appropriate guidance, and address the diverse needs and concerns of children. By prioritizing staff expertise, countries can enhance the quality of service, build trust with users, and improve overall customer satisfaction.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Invest in Staff Training and Development
    with st.expander("1. Invest in Staff Training and Development"):
        st.write("Allocate resources and invest in comprehensive training programs for staff members to enhance their expertise. Provide training on child protection, trauma-informed care, active listening, crisis management, and cultural sensitivity. Offer ongoing professional development opportunities to keep staff updated with the latest knowledge and best practices.")

    # Recommendation 2: Foster Collaboration and Learning Networks
    with st.expander("2. Foster Collaboration and Learning Networks"):
        st.write("Encourage collaboration and learning networks among staff members to share knowledge, experiences, and best practices. Facilitate regular team meetings, case discussions, and peer-to-peer learning sessions. Create a supportive environment that encourages continuous learning, growth, and the exchange of expertise within the team.")

    # Recommendation 3: Provide Access to Expert Consultation
    with st.expander("3. Provide Access to Expert Consultation"):
        st.write("Establish mechanisms for staff members to seek expert consultation when dealing with complex cases or specialized concerns. Create partnerships with child protection organizations, mental health professionals, legal experts, or other relevant institutions to provide access to expert advice, guidance, and support. This collaboration ensures that staff have the necessary resources to address diverse and challenging situations.")

    # Recommendation 4: Implement Quality Monitoring and Feedback Systems
    with st.expander("4. Implement Quality Monitoring and Feedback Systems"):
        st.write("Implement systems to monitor and evaluate staff performance, knowledge, and customer satisfaction. Conduct regular performance reviews, provide constructive feedback, and recognize outstanding performance. Utilize user feedback mechanisms to gather insights on staff interactions, professionalism, and expertise to continuously improve staff performance and enhance customer satisfaction.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Staff expertise is critical for providing effective support through digital channels and helplines for children. By implementing the recommendations mentioned above, countries can enhance staff competence, improve the quality of service, and ultimately increase customer satisfaction.")