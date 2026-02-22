import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="3D DESIGN STUDIO", layout="wide")

# ---------------- BACKGROUND IMAGE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://scontent-del2-3.cdninstagram.com/v/t51.2885-19/639668153_18071049152536885_8485514174942539167_n.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Overlay for readability */
    .overlay {
        background: rgba(0,0,0,0.55);
        padding: 30px;
        border-radius: 20px;
        margin-top: 20px;
    }

    /* -------- IMAGE SLIDER -------- */
    .slider {
        overflow: hidden;
        white-space: nowrap;
        width: 100%;
        margin-top: 40px;
    }

    .slide-track {
        display: inline-block;
        animation: scroll 40s linear infinite;
    }

    .slide-track img {
        height: 260px;
        margin-right: 20px;
        border-radius: 15px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
    }

    @keyframes scroll {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    h1, h2, h3, p, label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HERO SECTION ----------------
st.markdown(
    """
    <div class="overlay">
        <h1>3D DESIGN STUDIO</h1>
        <h3>Designing Beautiful Homes in Delhi NCR, Gurgaon, Noida</h3>
        <p><b>Our Best Designer:</b> Vikas Rana | 📞 +91 6207634535</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- MAIN IMAGE ----------------
st.image(
    "WhatsApp Image 2026-02-19 at 16.42.10.jpeg",
    use_column_width=True
)

# ---------------- IMAGE SLIDER ----------------
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

images = [
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.19.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.13.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.10.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.23.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.19.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.13.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.10.jpeg"),
    img_to_base64("WhatsApp Image 2026-02-19 at 16.42.23.jpeg"),
]

slider_html = """
<div class="slider">
    <div class="slide-track">
"""

for img in images:
    slider_html += f'<img src="data:image/jpg;base64,{img}"/>'

slider_html += """
    </div>
</div>
"""

st.markdown(slider_html, unsafe_allow_html=True)

# ---------------- SERVICES ----------------
st.markdown(
    """
    <div class="overlay">
        <h2>Our Services</h2>
        <ul>
            <li>Modular Kitchen</li>
            <li>Wardrobe Design</li>
            <li>Living Room Interiors</li>
            <li>Full Home Renovation</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CONTACT FORM ----------------
st.markdown(
    """
    <div class="overlay">
        <h2>📞 Get Free Consultation</h2>
    </div>
    """,
    unsafe_allow_html=True
)

name = st.text_input("Your Name")
phone = st.text_input("Phone Number")
city = st.selectbox("City", ["Delhi", "Gurugram", "Noida"])

if st.button("Submit"):
    st.success("Thank you! We will contact you soon.")
