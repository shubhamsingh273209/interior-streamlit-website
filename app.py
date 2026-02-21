import streamlit as st

st.set_page_config(page_title="3D DESIGN STUDIO", layout="wide")
# st.set_page_config(layout="wide")
st.set_page_config(page_title=" BY :- VIKASH KUMAR RANA")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://scontent-del2-3.cdninstagram.com/v/t51.2885-19/639668153_18071049152536885_8485514174942539167_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-del2-3.cdninstagram.com&_nc_cat=101&_nc_oc=Q6cZ2QHNQY7z_BcT1MfPVlwOX0erc582JOYSp0QRMu4TdWTHn_38Ysplam8Xpj4Edpk1Myc&_nc_ohc=gnyDjk1_Q9MQ7kNvwGTDfWi&_nc_gid=QmkEzHndhk8LULmxiYE6FQ&edm=AP4sbd4BAAAA&ccb=7-5&oh=00_AftM_aNJ2yj6vIDRGfWz1ckh-tdUsSVC4_TjCvsnrTM1Qg&oe=699F417F&_nc_sid=7a9f4b");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("3D DESIGN STUDIO")
st.subheader("Designing Beautiful Homes in Delhi NCR,GURGAON,NOIDA")
# st.subheader("✆ Contact us : +9198134723")
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
