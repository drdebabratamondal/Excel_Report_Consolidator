import streamlit as st
import pandas as pd
import numpy as np
from openpyxl.utils import column_index_from_string

st.title("Clinical Report Consolidator")

# 1. File Upload
uploaded_files = st.file_uploader("Upload your Excel reports", accept_multiple_files=True, type=['xlsx'])

if uploaded_files:
    # 2. Select Master
    master_file = st.selectbox("Select the master template file:", [f.name for f in uploaded_files])
    
    # 3. Grid Configuration
    col1, col2 = st.columns(2)
    row_start = col1.number_input("Starting row number", min_value=1, value=6)
    row_end = col2.number_input("Ending row number", min_value=1, value=194)
    
    col3, col4 = st.columns(2)
    col_start_letter = col3.text_input("Starting column letter", value="E")
    col_end_letter = col4.text_input("Ending column letter", value="S")

    if st.button("Consolidate Reports"):
        # Conversion
        row_idx_start = row_start - 1
        col_idx_start = column_index_from_string(col_start_letter) - 1
        col_idx_end = column_index_from_string(col_end_letter)

        # Logic to process files
        # (You would place the logic from run.py here, using file_uploader streams)
        st.success("Consolidation complete! Download your file below.")
        # st.download_button(...)