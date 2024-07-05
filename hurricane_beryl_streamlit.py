#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:18:42 2024

@author: geo-ns36752
"""

import streamlit as st
from PIL import Image
import base64

def displayLocalGIF1(placeholder, localImagePath, caption):
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
    
    # Display the GIF and caption with positioning relative to the placeholder
    placeholder.markdown(f"""<div style="{container_style}">
                    <img src="data:image/gif;base64,{imgData}" width='1000' height='600'>
                    <p style="{caption_style}">{caption}</p>
                    </div>""", unsafe_allow_html=True)


def displayLocalGIF2(placeholder, localImagePath, caption):
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
    
    # Display the GIF and caption with positioning relative to the placeholder
    placeholder.markdown(f"""<div style="{container_style}">
                    <img src="data:image/gif;base64,{imgData}" width='1000' height='500'>
                    <p style="{caption_style}">{caption}</p>
                    </div>""", unsafe_allow_html=True)



# Set the title of the app
st.title("Hurricane Beryl Forecast")
st.write('Experimental Forecast from UT Austin, Jackson School of Geosciences with TACC resources using ongoing research models IOLA (with NOAA and India) and Graphcast Operational setup at UT')
# Display the first GIF
st.header("Hurricane Beryl forecast from IOLA")
image_placeholder1 = st.empty()
imagePath1 = "IOLA.gif"
displayLocalGIF1(image_placeholder1, imagePath1,"Initialization: 2024-07-02 12:00:00 UTC")


# Display the second GIF
st.header("Hurricane Beryl forecast from Graphcast Operational")
image_placeholder2 = st.empty()
imagePath2 = "graphcast.gif"
displayLocalGIF2(image_placeholder2, imagePath2,"Initialization: 2024-07-04 00:00:00 UTC")

st.header('NHC advisory released on July 4, 2024 5PM EDT')
st.image('NHC_cone.png')
