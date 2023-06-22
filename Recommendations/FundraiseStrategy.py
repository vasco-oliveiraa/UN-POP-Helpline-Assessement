import streamlit as st

def fundraise_strategy():
    
    # Page title and description
    st.title("Fundraise Strategy")
    
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
    st.write("Developing an effective fundraise strategy is crucial to ensure sustainable funding for digital channels and helplines aimed at keeping children safe. It enables countries to secure financial resources necessary for infrastructure development, platform maintenance, staff training, and ongoing support services. A well-executed fundraise strategy helps create partnerships, mobilize resources, and raise public awareness about the importance of child protection and the role of digital channels in ensuring their safety.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Identify Funding Sources
    with st.expander("1. Identify Funding Sources"):
        st.write("Conduct a thorough assessment to identify potential funding sources for the implementation and sustainability of digital channels and helplines. Explore government funding opportunities, grants from international organizations, corporate social responsibility programs, and partnerships with philanthropic foundations. Engage with stakeholders to secure long-term financial commitments and support for child protection initiatives.")

    # Recommendation 2: Develop a Fundraising Plan
    with st.expander("2. Develop a Fundraising Plan"):
        st.write("Create a comprehensive fundraising plan that outlines clear goals, strategies, and timelines. Define fundraising targets, both short-term and long-term, and develop a diversified approach to attract funding from multiple sources. Incorporate strategies such as crowdfunding campaigns, donor outreach programs, corporate partnerships, and fundraising events to maximize fundraising opportunities.")

    # Recommendation 3: Establish Partnerships with Donors
    with st.expander("3. Establish Partnerships with Donors"):
        st.write("Develop strategic partnerships with donors who share the vision and goals of child protection. Engage with corporations, foundations, and individuals who have demonstrated a commitment to social impact and child well-being. Collaborate on joint initiatives, leverage their networks, and explore opportunities for sustained funding, including multi-year commitments and capacity-building support.")

    # Recommendation 4: Raise Public Awareness
    with st.expander("4. Raise Public Awareness"):
        st.write("Launch targeted awareness campaigns to educate the public about the importance of digital channels and helplines in safeguarding children. Highlight success stories, showcase the impact of these platforms, and emphasize the need for continued financial support. Utilize various communication channels, including social media, traditional media, and community events, to raise awareness, engage the public, and encourage donations.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Developing a robust fundraise strategy is essential to secure sustainable funding for digital channels and helplines, ensuring the safety and well-being of children. By implementing the recommendations mentioned above, countries can attract financial resources, foster partnerships, and raise public awareness, thus strengthening their fundraise strategies and supporting effective child protection initiatives.")