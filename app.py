import streamlit as st

st.set_page_config(page_title="TERRAWOOD.IN", layout="wide")
# st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F5F5F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🏠 TERRAWOOD.IN")
st.subheader("Designing Beautiful Homes in Delhi NCR,GURGAON,NOIDA")
st.subheader("✆ Contact us : +9198134723")
st.subheader("Our Best Designer :Vikas Rana contact: +916207634535")

st.image(
    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
    use_column_width=True
)

st.markdown("""
### Our Services
- Modular Kitchen
- Wardrobe Design
- Living Room Interiors
- Full Home Renovation
""")

st.markdown("### 📞 Get Free Consultation")

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
city = st.selectbox("City", ["Delhi", "Gurugram", "Noida"])

if st.button("Submit"):
    st.success("Thank you! We will contact you soon.")
