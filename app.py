import streamlit as st
from pathlib import Path
import base64

# ------------------------------------------------------------------
# PAGE SETUP
# ------------------------------------------------------------------
st.set_page_config(page_title="Kaaviyaa I — Portfolio", page_icon="👩‍💻", layout="wide")

# Load files
PROFILE_IMG = Path("profile.jpg")
RESUME = Path("Kaaviyaa_Resume.pdf")

def file_to_b64(path: Path):
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode()
    return None

# ------------------------------------------------------------------
# SIMPLE CLEAN STYLE
# ------------------------------------------------------------------
st.markdown("""
<style>
body {
    font-family: 'Inter', sans-serif;
}
.section-title {
    font-size: 28px;
    font-weight: 900;
    color: #1E88E5;
    border-bottom: 3px solid #1E88E5;
    padding-bottom: 6px;
    margin-top: 30px;
}
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #dddddd;
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------
# HEADER SECTION
# ------------------------------------------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    if PROFILE_IMG.exists():
        st.image(str(PROFILE_IMG), width=260)
    else:
        st.image("https://via.placeholder.com/260x260.png?text=Kaaviyaa", width=260)

with col2:
    st.markdown("""
        # Hi, I'm **Kaaviyaa**  
        ### AI • Machine Learning • IoT • Computer Vision  
        **B.Tech — Computer Science & Business Systems (TCE)**  
    """)

    if RESUME.exists():
        b64 = file_to_b64(RESUME)
        st.download_button("📄 Download Resume", data=RESUME.read_bytes(),
                           file_name="Kaaviyaa_Resume.pdf", mime="application/pdf")
    else:
        st.error("Resume file not found. Add `Kaaviyaa_Resume.pdf` in folder.")


# ------------------------------------------------------------------
# ABOUT ME
# ------------------------------------------------------------------
st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
st.markdown("""
I am a passionate computer science and business systems student with keen intrest in using AI, Machine Learning, IoT, and Computer Vision  
to build solutions that create real-world impact. I enjoy research, prototyping, and developing full-stack AI-driven systems.
""")

st.markdown("""
### **Academics**
- **B.Tech CSBS** — TCE — *CGPA: 9.02 (2023–2027)*  
- **Class 12** — 93.8% (2023)  
- **Class 10** — 88.8% (2021)
""")


# ------------------------------------------------------------------
# SKILLS
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

st.markdown("""
### Programming:
- Python, C, C++, Java

### Design & Tools:
- Canva, FlutterFlow, Streamlit, Firebase

### Areas of Interest:
- Machine Learning  
- Computer Vision  
- Deep Learning  
- IoT  
- Data Structures & Algorithms  
""")

with st.expander("📜 Certifications"):
    st.markdown("""
- NPTEL — Introduction to Machine Learning  
- NPTEL — Python for Data Science  
- LinkedIn Learning — Professional Networking  
- CEC — Programming in Python  
- Infosys Springboard — Prompt Engineering  
    """)


# ------------------------------------------------------------------
# PROJECTS
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

with st.expander("🛰️ Aqua Sentinel — Satellite Water Body Segmentation"):
    st.write("""
- Built U-Net, Double U-Net, SegNet, ResUNet models  
- Achieved **96.02% accuracy**  
- Detects floods, shrinking reservoirs  
- Awarded **$25 by Xylem Innovation Challenge**  
""")

with st.expander("⚡ AI-Based Transformer Health Monitoring"):
    st.write("""
- IoT + ML system for real-time transformer monitoring  
- Random Forest classifier to compute health score  
- Full dashboard in Streamlit  
- **Winner — Energathon ’25 (₹3000)**  
""")

with st.expander("🌱 EcoAudit — AI Energy Audit App"):
    st.write("""
- FlutterFlow + Firebase mobile app  
- AI-powered consumption tracking  
- **2nd Runner-Up — Energathon ’24 (₹1000)**  
""")

with st.expander("🤟Sign X - Sign Language Translator"):
    st.write("""
- Computer Vision + NLP model  
- Converts hand gestures into text  
- **Winner — Ideaflow Hackathon (1st Place)**  
""")


# ------------------------------------------------------------------
# INDUSTRIAL EXPOSURE
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Industrial Experience</div>', unsafe_allow_html=True)

st.markdown("""
- **Web Development Intern** — Big Si Bucks Innovation Pvt. Ltd — 1 Month  
- **Deep Learning Intern** — Madras Institute of Technology — 1 Month  
""")


# ------------------------------------------------------------------
# ACHIEVEMENTS
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Achievements</div>', unsafe_allow_html=True)

st.markdown("""
- 🥇 1st Place — Energathon ’25 — Transformer Monitoring  
- 🥈 2nd Runner-Up — Energathon ’24 — EcoAudit  
- 🥇 1st Place — Ideaflow Sign Language Translator  
- 💰 $25 Award — Xylem Innovation  
- 🥉 3rd Place — Case Analytics, CIT  
- Winner — E-Cell Week ’25  
- 1st Place — Money Maze  
- 3rd Place — Stake ’25  
- 3rd Place — Tech Quest  
""")


# ------------------------------------------------------------------
# HACKATHONS & COMPETITIONS
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Hackathons & Competitions</div>', unsafe_allow_html=True)

with st.expander("View All"):
    st.markdown("""
- Finalist — K!Hacks (900+ teams)  
- Participant — IIT Madras Ethletics  
- Top 30 — Caterpillar Tech Challenge  
- Finalist — Hackxelerate ’25  
- Finalist — STEM Hackathon (SASTRA)  
- SAP HackFest — Regional Round  

""")


# ------------------------------------------------------------------
# WORKSHOPS
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Workshops & Seminars</div>', unsafe_allow_html=True)

with st.expander("View All"):
    st.markdown("""
- Workshop on Building and Experimenting with LLMs – Shaastra, IIT Madras
- Seminar on FinTech Fusion – CSBS Department
- Workshop on Humanitarian Design & Social Enterprise – IUCEE & Lehigh University
- IEEE MAS SIGHT HUB Summit – Participant & Volunteer
- Workshop on Data-Driven Decision Making with AI – CSBS Department
- Lecture Series on Mastering LLMs – IBM & PALS
- Workshop on Front-End Development (HTML, CSS, JavaScript) – Infosys Springboard 
""")


# ------------------------------------------------------------------
# CO-CURRICULAR
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Co-curricular & Sports</div>', unsafe_allow_html=True)

st.markdown("""
- Runner-Up, Zone 16 Basketball – Anna University
- Best Player, Handball & Basketball – Interdepartment Matches, TCE
- Team Member, TCE Women’s Basketball Team – CM Trophy Tournament
- Participant, TCE Mini Marathon - 7 Km Marathon
- Participant, Intra-College Chess Tournament – TCE Physical education department
- Volunteer, NSS – Community service events including blood donation camps
""")


# ------------------------------------------------------------------
# CONTACT
# ------------------------------------------------------------------
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)

st.markdown("""
**Email:** kaaviyaa.i@gmail.com  
**Phone:** 8608508638  
**Languages:** Tamil, English, Hindi   
""")
