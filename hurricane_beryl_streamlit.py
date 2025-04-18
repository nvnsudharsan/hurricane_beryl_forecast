#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:18:42 2024

@author: geo-ns36752
"""

import streamlit as st
from PIL import Image
import base64

def displayLocalGIF(placeholder, localImagePath, caption):
    imgFile  = open(localImagePath, "rb")
    contents = imgFile.read()
    imgData  = base64.b64encode(contents).decode("utf-8")
    imgFile.close()
    
 
    container_style = (
        "position: relative;"       
        "display: inline-block;"    
    )
    
    caption_style = (
        "font-size: 14px;"      
        "color: #888888;"       
        "text-align: center;"   
    )
    
   
    placeholder.markdown(f"""<div style="{container_style}">
                    <img src="data:image/gif;base64,{imgData}"> 
                    <p style="{caption_style}">{caption}</p>
                    </div>""", unsafe_allow_html=True)





# Set the title of the app
st.markdown("<H1 style='text-align: center;'>Hurricane Beryl Forecast</H1>", unsafe_allow_html=True)
#st.title("")
st.write('Experimental Forecast from UT Austin, Jackson School of Geosciences with TACC resources using ongoing research models experimental HWRFx (with NOAA and India) and Graphcast Operational setup at UT')
# Display the first GIF
st.markdown("<H3 style='text-align: center;'>Hurricane Beryl forecast from Experimental HWRFx</H3>", unsafe_allow_html=True)
st.write('HWRFx is a physics or dynamics based model without ocean coupling or data assimilation.')
image_placeholder1 = st.empty()
imagePath1 = "IOLA1.gif"
displayLocalGIF(image_placeholder1, imagePath1,"Initialization: 2024-07-06 12:00:00 UTC")

image_placeholder8 = st.empty()
imagePath8 = "IOLA2.gif"
displayLocalGIF(image_placeholder8, imagePath8,"Initialization: 2024-07-06 12:00:00 UTC")

# Display the second GIF
st.markdown("<H3 style='text-align: center;'>Hurricane Beryl forecast from Graphcast Operational</H3>", unsafe_allow_html=True)
st.write('Graphcast is an AI/ML model developed by Google DeepMind. We are running this model on TACC Lonestar6 GPUs with initial conditions from GFS.')
image_placeholder2 = st.empty()
imagePath2 = "graphcast1.gif"
displayLocalGIF(image_placeholder2, imagePath2,"Initialization: 2024-07-07 00:00:00 UTC")

image_placeholder3 = st.empty()
imagePath3 = "graphcast2.png"
displayLocalGIF(image_placeholder3, imagePath3,"Initialization: 2024-07-07 00:00:00 UTC")
st.write('The forecast shows that the cumulative precipitation in and around Austin will be less than 1.5 inches.')

st.markdown("<H3 style='text-align: center;'>Previous Forecasts</H3>", unsafe_allow_html=True)
st.markdown("<H5 style='text-align: center;'>Graphcast Operational</H5>", unsafe_allow_html=True)

image_placeholder6 = st.empty()
imagePath6 = "graphcast1_old.gif"
displayLocalGIF(image_placeholder6, imagePath6,"Initialization: 2024-07-06 00:00:00 UTC")

image_placeholder4 = st.empty()
imagePath4 = "graphcast1_older.gif"
displayLocalGIF(image_placeholder4, imagePath4,"Initialization: 2024-07-05 00:00:00 UTC")

st.markdown("<H5 style='text-align: center;'>Experimental HWRFx</H5>", unsafe_allow_html=True)

image_placeholder7 = st.empty()
imagePath7 = "IOLA1_old.gif"
displayLocalGIF(image_placeholder7, imagePath7,"Initialization: 2024-07-06 00:00:00 UTC")

image_placeholder5 = st.empty()
imagePath5 = "IOLA1_older.gif"
displayLocalGIF(image_placeholder5, imagePath5,"Initialization: 2024-07-02 12:00:00 UTC")


st.markdown("<H3 style='text-align: center;'>National Hurricane Center advisory</H3>", unsafe_allow_html=True)
st.image('https://www.nhc.noaa.gov/storm_graphics/AT02/refresh/AL022024_5day_cone_no_line_and_wind+png/024651_5day_cone_no_line_and_wind.png')

st.write("PS: This is experimental and GFS is used to initialize the models")
st.write("Disclaimer: This experimental forecast is not for public advisory or use, or any decision making and is only updated here for the lab and project teams to test the models. No liability is assumed. The official forecasts are available from NOAA/NWS")
st.write("Last updated on 7th July 2024 at 12:15 AM CST")
