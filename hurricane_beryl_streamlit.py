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
    
    # Define CSS styles for the container and caption
    container_style = (
        "position: relative;"       # Enable relative positioning
        "display: inline-block;"    # Display as inline-block to align with placeholder
    )
    
    caption_style = (
        "font-size: 14px;"      # Adjust the font size as needed
        "color: #888888;"       # Dimmer color
        "text-align: center;"   # Center the caption text
    )
    
    # Display the GIF and caption with positioning relative to the placeholder #<img src="data:image/gif;base64,{imgData}" width='1000' height='600'>
    placeholder.markdown(f"""<div style="{container_style}">
                    <img src="data:image/gif;base64,{imgData}"> 
                    <p style="{caption_style}">{caption}</p>
                    </div>""", unsafe_allow_html=True)





# Set the title of the app
st.markdown("<H1 style='text-align: center;'>Hurricane Beryl Forecast</H1>", unsafe_allow_html=True)
#st.title("")
st.write('Experimental Forecast from UT Austin, Jackson School of Geosciences with TACC resources using ongoing research models IOLA (with NOAA and India) and Graphcast Operational setup at UT')
# Display the first GIF
st.markdown("<H3 style='text-align: center;'>Hurricane Beryl forecast from IOLA</H3>", unsafe_allow_html=True)
image_placeholder1 = st.empty()
imagePath1 = "IOLA.gif"
displayLocalGIF(image_placeholder1, imagePath1,"Initialization: 2024-07-02 12:00:00 UTC")

# Display the second GIF
st.markdown("<H3 style='text-align: center;'>Hurricane Beryl forecast from Graphcast Operational</H3>", unsafe_allow_html=True)
image_placeholder2 = st.empty()
imagePath2 = "graphcast1.gif"
displayLocalGIF(image_placeholder2, imagePath2,"Initialization: 2024-07-04 00:00:00 UTC")

image_placeholder3 = st.empty()
imagePath3 = "graphcast2.gif"
displayLocalGIF(image_placeholder3, imagePath3,"Initialization: 2024-07-05 00:00:00 UTC")

st.markdown("<H3 style='text-align: center;'>National Hurricane Center advisory</H3>", unsafe_allow_html=True)
st.image('https://www.nhc.noaa.gov/storm_graphics/AT02/refresh/AL022024_5day_cone_no_line_and_wind+png/024651_5day_cone_no_line_and_wind.png')

st.write("PS: This is experimental")
st.write("Last updated on 4 July 2024 at 11:30 PM CST")
