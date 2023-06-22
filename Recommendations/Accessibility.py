import streamlit as st

def accessibility():
    
    # Page title and description
    st.title("Accessibility")
    
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
    st.write("Ensuring accessibility across multiple platforms is essential for reaching and assisting a wider range of children through digital channels and helplines. Children access information and services using various devices, such as smartphones, tablets, computers, or feature phones. By optimizing digital channels and helplines for multi-platform accessibility, countries can overcome barriers and provide equal access to support for children, regardless of the devices they use.")

    # Divider
    st.divider()

    # Recommendation section
    st.subheader("Recommendations")
    st.markdown("Based on successful experiences in providing support for children in situations of danger through online channels and helplines, here are some recommendations:")

    # Recommendation 1: Responsive Design for Mobile Devices
    with st.expander("1. Responsive Design for Mobile Devices"):
        st.write("Optimize digital channels and helplines with responsive design principles to ensure seamless access and usability on various mobile devices. Responsive design allows the content and interface to automatically adapt to different screen sizes, orientations, and resolutions, providing a consistent and user-friendly experience for children accessing the services through smartphones or tablets.")

    # Recommendation 2: Cross-Platform Compatibility
    with st.expander("2. Cross-Platform Compatibility"):
        st.write("Ensure cross-platform compatibility by developing digital channels and helplines that can be accessed across different operating systems, such as iOS, Android, Windows, or web browsers. Test the compatibility of the platforms on various devices and operating systems to identify and address any compatibility issues that may hinder accessibility.")

    # Recommendation 3: Text-to-Speech and Screen Reader Support
    with st.expander("3. Text-to-Speech and Screen Reader Support"):
        st.write("Incorporate text-to-speech functionality and support for screen readers to assist children with visual impairments or reading difficulties. Ensure that the digital platforms and helplines are compatible with assistive technologies commonly used by individuals with disabilities. Test the accessibility features to guarantee their effectiveness and usability.")

    # Recommendation 4: Simplified Navigation and User Interface
    with st.expander("4. Simplified Navigation and User Interface"):
        st.write("Design a simplified and intuitive user interface with clear navigation menus and well-structured content. Avoid complex layouts, excessive scrolling, or reliance on small clickable elements that may pose challenges for children with motor skill limitations or visual impairments. Incorporate user testing and feedback to continuously improve the accessibility of the platforms.")

    # Divider
    st.divider()

    # Conclusion
    st.header("Conclusion")
    st.write("Ensuring multi-platform accessibility is crucial for reaching and assisting a diverse range of children through digital channels and helplines. By implementing the recommendations mentioned above, countries can overcome accessibility barriers and provide equal access to support services for children, regardless of the devices they use.")