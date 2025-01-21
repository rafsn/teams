import streamlit as st
import pandas as pd
import webbrowser

if "data" not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    st.session_state["data"] = df_data

st.write("# Fifa Official DataSet")
st.sidebar.markdown("Desenvolvido por Rafa")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open("https://www.kaggle.com/")

st.markdown(
    """
    The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time.
    
    The Football Player Dataset from 2017 to 2023 is a comprehensive collection of information about professional football players. It includes details such as player demographics, physical characteristics, playing statistics, contract details, club affiliations, market values, wages, preferred positions, work rates, skill ratings, and player development. 
    
    """
)
