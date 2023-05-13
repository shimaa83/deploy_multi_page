import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import cv2
import pandas as pd
import os
import sys

import io 
with st.sidebar:
    choose = option_menu("App Gallery", ["About",  "Project NLP", "OCEAN Data"],
                         icons=['house',  'kanban', 'book'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
profile = Image.open(r'shareable_life_models/1.jpeg')
if choose == "About":
                   # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)    
      
        st.write("The primary goal of this project is to develop a machine-learning model that can accurately match potential roommates based on their preferences, lifestyle, and psychological profiles. The model should be efficient, streamlined, and user-friendly.The project aims to: - Collect data on potential roommates, including information on their lifestyle,food preferences, and other factors that may impact their compatibility with others.- Develop a machine learning model that uses the collected data to identify potential matches.- Train and evaluate the model using a dataset of past matches- Develop a user-friendly app that incorporates the matching algorithm and enables users to input their preferences and receive recommendations for potential roommates.")    
        st.image(profile, width=700 )
elif choose == "Project NLP":
               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">NLP Model</p>', unsafe_allow_html=True)    
      
        st.image(profile, width=700 )
elif choose == "OCEAN Data":
               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">OCEAN Data</p>', unsafe_allow_html=True)    
      
        st.image(profile, width=700 )
    
