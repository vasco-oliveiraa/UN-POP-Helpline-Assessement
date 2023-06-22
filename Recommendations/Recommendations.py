import streamlit as st
import pycountry

from ModelScoring import model_scoring

from GetCountryFromIP.GetCountryFromIP import get_country_from_ip

from Recommendations.DigitalChannelImplementation import digital_channel_implementation
from Recommendations.TechnologyStack import technology_stack
from Recommendations.FundraiseStrategy import fundraise_strategy
from Recommendations.ConfidentialityDataProtection import confidentiality_data_protection
from Recommendations.Responsiveness import responsiveness
from Recommendations.QualityImpact import quality_impact
from Recommendations.StaffExpertise import staff_expertise
from Recommendations.CulturalLinguisticNeeds import cultural_linguistic_needs
from Recommendations.AgeAppropriateGuidance import age_appropriate_guidance
from Recommendations.Accessibility import accessibility
from Recommendations.CountrySpecificRecommendations import country_specific_recommendations

def recommendations(user_scores):
    
    if user_scores:
        
        improvement_areas = model_scoring(user_scores, output='improvement_areas')

        area_function = {
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

        def page(area):
            area_function[area]()

        with st.container():

            st.title('Recommendations')
            
            tab1, tab2 = st.tabs(['Top 3 Improvement Areas','Country-Specific Recommendations'])
            
            with tab1:
                
                tab_titles = [area.replace('_', ' ').title() for area in improvement_areas]

                tab11, tab12, tab13 = st.tabs(tab_titles)

                with tab11:
                    page(improvement_areas[0])

                with tab12:
                    page(improvement_areas[1])

                with tab13:
                    page(improvement_areas[2])
                
            with tab2:

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
                        if country in countries:
                            st.session_state['country'] = country

                    else:
                        # Create a dropdown in Streamlit
                        country = st.selectbox('Country*', countries, index=countries.index('Select a country'))
                        if country in countries:
                            st.session_state['country'] = country

                if country and (country!='Select a country'):

                    st.subheader(f'Recommendations for {country}')

                    with st.spinner("Generating Country-Specific Recommendations"):

                        message = country_specific_recommendations(country={country}, improvement_areas=improvement_areas)

                        try:
                            exec(message)
                        except:
                            message = country_specific_recommendations(country={country}, improvement_areas=improvement_areas)
                            exec(message)
                    
    else:
        st.write('Please submit the form to display recommendations.')
