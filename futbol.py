# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 13:45:08 2023

@author: jperezr
"""

import pandas as pd
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

# Create a dataframe with pandas (you can pass any pandas dataframe)

st.title("Creado por: Javier Horacio Pérez ricárdez"

#dataframe = pd.DataFrame({'A': [1, 2, 3]})

dataframe = pd.read_csv("Libro1.csv")

# Display the dataframe in a Mito spreadsheet
final_dfs, code = spreadsheet(dataframe)

# Display the final dataframes created by editing the Mito component
# This is a dictionary from dataframe name -> dataframe
#st.write(final_dfs)   PARA QUE SE VEA EL CÓDIGO EN LA PÁGINA WEB

# Display the code that corresponds to the script
#st.code(code)   PARA QUE SE VEA EL CÓDIGO EN LA PÁGINA WEB
