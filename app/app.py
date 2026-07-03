import streamlit as st
import pandas as pd
import numpy as np
import io
from openpyxl.utils import column_index_from_string

st.set_page_config(page_title="Clinical Report Consolidator", layout="wide")
st.title("📊 Clinical Report Consolidator")
st.write("Upload your monthly RARI clinical reports to consolidate them automatically.")

# 1. File Upload
uploaded_files = st.file_uploader("Upload Excel reports", accept_multiple_files=True, type=['xlsx'])

if uploaded_files:
    # 2. Select Master Template
    file_names = [f.name for f in uploaded_files]
    master_file_name = st.selectbox("Select the master template file:", file_names)
    
    # Locate the master file object
    master_file = next(f for f in uploaded_files if f.name == master_file_name)
    
    # 3. Grid Configuration
    st.subheader("Grid Configuration")
    col1, col2 = st.columns(2)
    row_start = col1.number_input("Starting row number", min_value=1, value=6)
    row_end = col2.number_input("Ending row number", min_value=1, value=194)
    
    col3, col4 = st.columns(2)
    col_start_letter = col3.text_input("Starting column letter", value="E").upper()
    col_end_letter = col4.text_input("Ending column letter", value="S").upper()

    # 4. Process Data
    if st.button("Consolidate Reports"):
        try:
            row_idx_start = row_start - 1
            col_idx_start = column_index_from_string(col_start_letter) - 1
            col_idx_end = column_index_from_string(col_end_letter)
            
            df_summed = pd.read_excel(master_file, sheet_name='Sheet1', header=None)
            
            for f in uploaded_files:
                if f.name == master_file_name:
                    continue
                    
                df_temp = pd.read_excel(f, sheet_name='Sheet1', header=None)
                
                for r in range(row_idx_start, row_end):
                    for c in range(col_idx_start, col_idx_end):
                        val_curr = pd.to_numeric(df_summed.iloc[r, c], errors='coerce')
                        val_new = pd.to_numeric(df_temp.iloc[r, c], errors='coerce')
                        df_summed.iloc[r, c] = np.nansum([val_curr, val_new])
            
            # Save to buffer using explicit ExcelWriter
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_summed.to_excel(writer, index=False, header=False)
            
            # Save the file to session state
            st.session_state['download_data'] = buffer.getvalue()
            st.session_state['success'] = True
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # 5. Display Download Button
    if st.session_state.get('success', False):
        st.success("Consolidation complete! Download your file below.")
        st.download_button(
            label="Download Consolidated Report",
            data=st.session_state['download_data'],
            file_name="Consolidated_Master_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )