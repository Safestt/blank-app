import streamlit as st
import pandas as pd

# Set page config to match the theme
st.set_page_config(
    page_title="Student Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match the theme
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #009688;
        color: white;
        border: none;
    }
    .stSelectbox {
        color: #333;
    }
    div[data-testid="stHeader"] {
        background-color: #009688;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("NKST SEC SCH")
    st.sidebar.markdown("---")
    
    menu_options = [
        "Dashboard",
        "Portal Request",
        "Profile",
        "Administrative Manager",
        "Student Management",
        "Class Attendance",
        "View Attendance Records",
        "Behavioral Analysis",
        "Class Management",
        "Subject Management",
        "Result Management"
    ]
    
    selected_menu = st.sidebar.selectbox("Menu", menu_options)

# Main content
st.title("Student Management")
st.subheader("View Students in Class")

# Class selector
col1, col2 = st.columns([3, 1])
with col1:
    selected_class = st.selectbox("CLASS", ["Select Class", "JSS1B", "JSS2A", "JSS3B", "SS1A", "SS2B", "SS3A"])
with col2:
    st.button("VIEW MEMBERS", type="primary")

# Sample data
data = {
    'S/N': range(1, 5),
    'Student Name': ['Abdulmumini Adamu Musa', 'Alhamdu Peter', 'Anthony Esther', 'Daniel Julius'],
    'Sex': ['Male', 'Male', 'Female', 'Male'],
    'Class': ['JSS1B'] * 4,
    'Phone': ['09023123319', '00', '00', '00'],
    'Reg Number': ['201815FSTCMICH205', '201815FSTCMICH215', '201815FSTCMICH222', '201815FSTCMICH212'],
    'Password': ['fstc'] * 4
}

df = pd.DataFrame(data)

# Display table with action buttons
st.dataframe(df, hide_index=True)

# Action buttons for each row (in practice, you'd want to add these to the table)
col1, col2, col3 = st.columns(3)
with col1:
    st.button("EDIT", key="edit_btn", type="primary")
with col2:
    st.button("DELETE", key="delete_btn", type="secondary")
with col3:
    st.button("SLIP", key="slip_btn", type="primary")

# Note: In a real application, you would need to:
# 1. Connect to a database
# 2. Implement proper authentication
# 3. Add functionality to the action buttons
# 4. Handle file uploads for passport photos
# 5. Implement proper error handling
