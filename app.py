import streamlit as st
from PIL import Image
import base64

# Load custom CSS
# NOTE: style.css must be in the same directory as the script.
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    # Minimal fallback style if file is missing
    st.markdown("""
        <style>
        .header h1 {color: #4CAF50;}
        .header p {margin: 0;}
        .section-header {color: #1E88E5;}
        .project-title {color: #FF9800;}
        .achievement-item {margin-bottom: 5px;}
        .footer {text-align: center; margin-top: 50px; padding: 10px; background-color: #f0f0f0;}
        .btn {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 10px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #4CAF50;
            border: none;
            border-radius: 15px;
            box-shadow: 0 5px #999;
        }
        .btn:hover {background-color: #3e8e41}
        .btn:active {
            background-color: #3e8e41;
            box-shadow: 0 2px #666;
            transform: translateY(4px);
        }
        </style>
    """, unsafe_allow_html=True)


# Profile Image
# NOTE: The image file "profile.jpg" must be present.
try:
    image = Image.open("profile.jpg")
    st.image(image, width=240, caption="KAAVIYAA I")
except FileNotFoundError:
    st.image("https://via.placeholder.com/240x240?text=Profile+Image", width=240, caption="KAAVIYAA I")


# Header Section
st.markdown(f"""
    <div class="header">
        <h1>👩‍💻 KAAVIYAA I</h1>
        <p>B.Tech. Computer Science and Business Systems, Thiagarajar College of Engineering</p>
        <p><a href="mailto:kaaviyaa.i@gmail.com">kaaviyaa.i@gmail.com</a> | 📞 8608508638</p>
    </div>
""", unsafe_allow_html=True)

# Resume download button
def get_pdf_download_link(pdf_path):
    # NOTE: The PDF file "Kaaviyaa_Resume.pdf" must be present.
    try:
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        href = f'<a class="btn" href="data:application/octet-stream;base64,{base64_pdf}" download="Kaaviyaa_Resume.pdf">📄 Download Resume</a>'
    except FileNotFoundError:
        href = '<p style="color:red;">Resume PDF not found. Cannot provide download link.</p>'
    return href

st.markdown(get_pdf_download_link("Kaaviyaa_Resume.pdf"), unsafe_allow_html=True)

# Full Summary from Resume
st.subheader("🌟 Professional Objective")
st.success("To leverage my skills in computer science and innovative thinking to add value to company projects, while continuously learning and evolving as a professional.")



# Experience

st.subheader("💼 Industrial Exposure")
st.markdown("""
* [cite_start]**Deep Learning Internship** — **Madras Institute of Technology** (1 month) [cite: 40]
* **Web Development Internship** — **Big Si Bucks Innovation pvt. [cite_start]Ltd.** (1 month) [cite: 40]
""")


# Education

st.subheader("🎓 Academic Record")
st.markdown(f"""
* [cite_start]**B.Tech. Computer Science and Business Systems** | Thiagarajar College of Engineering, Madurai [cite: 13, 16]
    * [cite_start]Affiliated to Anna University [cite: 16]
    * [cite_start]CGPA: $9.02^*$ [cite: 16, 17]
    * [cite_start]Year of Passing: 2027 [cite: 16]
* **Class 12** | [cite_start]Bhaktavatsalam Vidyashram (CBSE) [cite: 16]
    * [cite_start]% of Marks: 93.8% [cite: 16]
    * [cite_start]Year of Passing: 2023 [cite: 16]
* **Class 10** | [cite_start]Bhaktavatsalam Vidyashram (CBSE) [cite: 16]
    * [cite_start]% of Marks: 88.8% [cite: 16]
    * [cite_start]Year of Passing: 2021 [cite: 16]
""")


# Skills & Areas of Interest

st.subheader("🛠 Computer Proficiency & Interests")
st.markdown("""
### **Programming Languages**
[cite_start]**Python, C++, C, Java** [cite: 23]

### **Designing Software/Tools**
[cite_start]**Canva, Flutter Flow** [cite: 23]

### **Areas of Interest**
* [cite_start]**Machine Learning** [cite: 19]
* [cite_start]**Computer Vision** [cite: 20]
* [cite_start]**Data Structures and Algorithms** [cite: 21]
""")


# Certifications

st.subheader("📜 Certification Course(s)")
st.markdown("""
* [cite_start]Introduction to Machine Learning - **NPTEL** [cite: 25, 26]
* [cite_start]Python for data science - **NPTEL** [cite: 27, 28]
* [cite_start]Programming in Python - **Consortium for Educational Communication** [cite: 31, 32]
* [cite_start]Introduction to Prompt Engineering - **Infosys Springboard** [cite: 33]
* [cite_start]Professional Networking - **Linkedin Learning** [cite: 29, 30]
""")


# Projects (Corrected)

st.subheader("🚀 Key Projects")

### [cite_start]**1. Aqua Sentinel - AI-Powered Water Body Monitoring** [cite: 35]
* [cite_start]Developed a deep learning system for satellite image segmentation (U-Net, Double U-Net, SegNet, ResUNet) to enhance water body monitoring and disaster response[cite: 35].
* [cite_start]Achieved **96.02% accuracy (Double U-Net)**[cite: 35].
* [cite_start]Provides insights such as early flood detection and tracking water loss via a Streamlit dashboard[cite: 35].
* [cite_start]Recognized with a **\$25 incentive award at the Xylem Global Student Innovation Challenge 2025**[cite: 35, 46].

### **2. [cite_start]AI-Powered Transformer Health Monitoring System** [cite: 36, 37]
* [cite_start]Designed and implemented an **AI-Powered IoT device** to monitor transformer parameters (voltage, current, temperature, vibration)[cite: 36].
* [cite_start]Integrated a **Random Forest ML model** to compute health scores and estimate remaining lifespan[cite: 37].
* [cite_start]Built a Streamlit dashboard for real-time visualization, maintenance advice, and cost-saving insights[cite: 37].
* [cite_start]**Winner at Energathon '25, receiving a ₹3000 cash prize**[cite: 37, 42].

### **3. [cite_start]EcoAudit - AI-Powered Energy Audit and Optimization App** [cite: 38]
* [cite_start]Developed a mobile application using **FlutterFlow, Firebase, and LLaMA API** to automate household energy audits[cite: 38].
* [cite_start]Implemented interactive dashboards for energy tracking and personalized energy-saving suggestions[cite: 38].
* [cite_start]Recognized as **Second Runner-Up at Energathon '24 hackathon, receiving a ₹1000 cash award**[cite: 38, 43].


# Achievements & Awards (Corrected)

st.subheader("🏆 Achievements")
st.markdown("""
* [cite_start]**1st Place**, Energathon '25 - Transformer Health Monitoring System (Received cash prize of ₹3000) [cite: 42]
* [cite_start]**1st Place**, Ideaflow Hackathon - Project on Sign Language Translator for Deaf Communication [cite: 44]
* [cite_start]**Overall Winner**, E-Cell Week '25 [cite: 48]
    * [cite_start]Included **1st Place** in Money Maze - Startup Finance Proposal [cite: 48]
    * [cite_start]Included **3rd Place** in Stake '25 - Startup Venture Pitching [cite: 49]
* [cite_start]**2nd Runner-up**, Energathon '24 - Energy Audit App (Received cash prize of ₹1000) [cite: 43]
* [cite_start]**3rd Place**, Case Analytics - Business Case Study (160+ teams, Received cash prize of ₹1000) [cite: 47]
* [cite_start]**Xylem Innovation Challenge '25** - Satellite Image Water Body Monitoring (Received \$25 Incentive) [cite: 46]
* [cite_start]**Finalist**, K!Hacks - Anna University, CEG Campus (Ranked in top 25 out of 900+ teams) [cite: 61]
* [cite_start]**3rd Place**, Tech Quest - Technical Quiz [cite: 50]
""")


# Leadership & Activities

st.subheader("🤝 Leadership and Extra-Curricular")
st.markdown("""
### **Leadership Qualities**
* [cite_start]**President**, Build Club, TCE - Guided juniors in project building, organized workshops and competitions[cite: 52].
* [cite_start]**Joint Treasurer**, Computer Science & Business Systems Association[cite: 53].
* [cite_start]**Student Ambassador**, AI Consortium, TCE - Coordinated events and conducted AI awareness sessions[cite: 55].

### **Sports & Co-Curricular**
* [cite_start]Runner-Up, Zone 16 Basketball - Anna University[cite: 75].
* [cite_start]**Best Player**, Handball & Basketball - Interdepartment Matches, TCE[cite: 76].
* [cite_start]Participant in multiple hackathons including **Caterpillar Tech Challenge (Top 30)** [cite: 63] [cite_start]and **ISRO Hackathon**[cite: 67].
* [cite_start]Volunteer in NSS - Participated in community service events including blood donation camps[cite: 57, 58, 78].
""")

# Footer
st.markdown("""
<div class="footer">
    Connect with me: kaaviyaa.i@gmail.com | Thank you!
</div>
""", unsafe_allow_html=True)

