import streamlit as st

from ModelScoring import model_scoring
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

def recommendations(user_scores):
    
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

        tab1, tab2, tab3 = st.tabs([area.replace('_', ' ').title() for area in improvement_areas])

        with tab1:
            page(improvement_areas[0])

        with tab2:
            page(improvement_areas[1])

        with tab3:
            page(improvement_areas[2])
