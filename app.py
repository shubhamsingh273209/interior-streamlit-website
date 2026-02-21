import streamlit as st

st.set_page_config(page_title="Interior Design Studio", layout="wide")

st.title("🏠 Interior Design Studio")
st.subheader("Designing Beautiful Homes in Delhi NCR")

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
