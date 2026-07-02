import streamlit as st

# Clear data caches (e.g., dataframes, queries)
st.cache_data.clear()

# Clear resource caches (e.g., database connections, ML models)
st.cache_resource.clear()
