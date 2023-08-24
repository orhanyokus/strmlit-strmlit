import streamlit as st
import pandas as pd

# Path to the Excel file
excel_file_path = 'STOK.xlsx'

# Load the Excel data
def load_excel_data():
    try:
        data = pd.read_excel(excel_file_path)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    st.title("Excel Data Viewer")

    # Load Excel data
    data = load_excel_data()

    if data is not None:
        st.sidebar.header("Search")

        # Search bar
        search_term = st.sidebar.text_input("Enter search term:")
        filtered_data = data[data.apply(lambda row: search_term.lower() in str(row).lower(), axis=1)]

        st.write("### Filtered Excel Data:")
        st.dataframe(filtered_data)

if __name__ == "__main__":
    main()
