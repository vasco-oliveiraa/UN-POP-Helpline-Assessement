import streamlit as st

def confidentiality_data_protection():
    
    # Page title and description
    st.title("Confidentiality and Data Protection")
    
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
    st.write("Maintaining confidentiality and ensuring data protection are critical aspects of providing safe and secure digital channels and helplines for children. Protecting the privacy and personal information of children is essential to build trust and encourage them to seek help. It is vital to establish robust security measures, implement data protection policies, and comply with relevant laws and regulations to safeguard children's confidentiality and maintain the integrity of the digital platforms.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Establish Strict Data Protection Policies
    with st.expander("1. Establish Strict Data Protection Policies"):
        st.write("Develop and implement comprehensive data protection policies and procedures. Ensure that all collected data, including personal information and communication records, are treated with the utmost confidentiality. Define guidelines for data handling, storage, access, and retention. Regularly review and update these policies to align with evolving data protection standards and regulations.")

    # Recommendation 2: Secure Digital Infrastructure
    with st.expander("2. Secure Digital Infrastructure"):
        st.write("Implement robust security measures to protect the digital infrastructure supporting the channels and helplines. This includes employing encryption protocols, secure network configurations, access controls, and firewall protection. Regularly monitor and update security systems to address emerging threats and vulnerabilities. Conduct security audits and penetration tests to identify potential weaknesses and ensure the integrity of the systems.")

    # Recommendation 3: Train Staff on Confidentiality and Data Protection
    with st.expander("3. Train Staff on Confidentiality and Data Protection"):
        st.write("Provide comprehensive training to all staff members involved in operating and maintaining the digital channels and helplines. Train them on the importance of confidentiality, data protection best practices, and compliance with privacy regulations. Empower staff with knowledge and skills to handle sensitive information securely, identify potential risks, and respond appropriately to incidents or breaches.")

    # Recommendation 4: Regularly Audit and Monitor Data Handling Practices
    with st.expander("4. Regularly Audit and Monitor Data Handling Practices"):
        st.write("Establish a robust system for auditing and monitoring data handling practices. Regularly review access logs, data transfers, and user activities to detect any unauthorized access or suspicious behavior. Implement mechanisms to promptly investigate and respond to potential data breaches. Conduct periodic external audits to assess compliance with data protection standards and identify areas for improvement.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Ensuring confidentiality and data protection is paramount in providing secure digital channels and helplines for children. By implementing the recommendations mentioned above, countries can establish a culture of privacy, protect children's personal information, and maintain the integrity of the digital platforms, fostering trust and promoting effective child protection.")