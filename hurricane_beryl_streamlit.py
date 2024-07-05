#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:18:42 2024

@author: geo-ns36752
"""

import streamlit as st

def displayLocalGIF(placeholder, imagePath, caption):
    placeholder.image(
        imagePath,
        use_column_width=False,  # Disable container width
        width=100,               # Set the width
        caption=caption       # Optional caption
    )

# Set the title of the app
st.title("Hurricane Beryl Forecast")
st.write('Experimental Forecast from UT Jackson School of Geosciences with TACC resources using ongoing research models IOLA (with NOAA and India) and Graphcast Operational setup at UT')
# Display the first GIF
st.header("Hurricane Beryl forecast from IOLA (Initialization: 2024-07-02 12:00:00 UTC)")
image_placeholder1 = st.empty()
imagePath1 = "https://github.com/nvnsudharsan/hurricane_beryl_forecast/blob/main/IOLA.gif"
displayLocalGIF(image_placeholder1, imagePath1,"Local Image")

# Display the second GIF
st.header("Hurricane Beryl forecast from Graphcast Operational (Initialization: 2024-07-04 00:00:00 UTC)")
st.image("graphcast.gif")

st.header('NHC advisory released on July 4, 2024 5PM EDT')
st.image('NHC_cone.png')
