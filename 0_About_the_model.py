import streamlit as st

st.markdown('''
            ### Motivation
            
            Fire inside multistorage buildings may lead to considerable deflection of the (hollow) concrete decks used. In order to limit the spread of fire, 
            attachment of non-structual walls needs to be carefully considered. Currently, the span of the deck divided by 50 seems to be the guidance for the magnitude of deflection.

            This method is an attempt to generate a fast estimate for the deflection taking into account multiple parameters.

            ### Method explained
            The method is based on than planar cross-sections remain planar and the deck is considerably shorter in one direction (the span) than the other. By this assumption it
            is possible to provide the deflection when only parts of the deck is exposed to the fire and furthermore, investigate different spans and development over time.

            The main input to the model is the strain history for a cross-section of the considered deck. These strains are found by means of a transient FE model taking into account 
            various aspects of the concrete (e.g. temperature dependent stiffness). 


            ### Assumptions
            It is assumed that the deck is only spanning in one direction and that the strain history used is representative for the concrete deck in question. 


            ### Disclaimer
            The method and models shown are still under development and needs proper QA before is should be applied.

    ''')