
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
* **Deep Learning Internship** — **Madras Institute of Technology** (1 month)
* **Web Development Internship** — **Big Si Bucks Innovation pvt. Ltd.** (1 month)
""")


# Education

st.subheader("🎓 Academic Record")
st.markdown(f"""
* **B.Tech. Computer Science and Business Systems** | Thiagarajar College of Engineering, Madurai
    * Affiliated to Anna University
    * CGPA: $9.02^*$ (Up to VI semester)
    * Year of Passing: 2027
* **Class 12** | Bhaktavatsalam Vidyashram (CBSE)
    * % of Marks: 93.8%
    * Year of Passing: 2023
* **Class 10** | Bhaktavatsalam Vidyashram (CBSE)
    * % of Marks: 88.8%
    * Year of Passing: 2021
""")


# Skills & Areas of Interest

st.subheader("🛠 Computer Proficiency & Interests")
st.markdown("""
### **Programming Languages**
**Python, C++, C, Java**

### **Designing Software/Tools**
**Canva, Flutter Flow**

### **Areas of Interest**
* **Machine Learning**
* **Computer Vision**
* **Data Structures and Algorithms**
""")


# Certifications

st.subheader("📜 Certification Course(s)")
st.markdown("""
* Introduction to Machine Learning - **NPTEL**
* Python for data science - **NPTEL**
* Programming in Python - **Consortium for Educational Communication**
* Introduction to Prompt Engineering - **Infosys Springboard**
* Professional Networking - **Linkedin Learning**
""")


# Projects

st.subheader("🚀 Key Projects")

st.markdown("""
<h4 class="project-title">1. Aqua Sentinel - AI-Powered Water Body Monitoring using Satellite Image Segmentation</h4>
* **Objective**: Developed a deep learning system for satellite image segmentation to enhance water body monitoring and disaster response.
* **Key Achievement**: Achieved **96.02% accuracy (Double U-Net)**, improving prior benchmarks.
* **Recognition**: Recognized with a **\$25 incentive award at the Xylem Global Student Innovation Challenge 2025**.
* **Technology**: Used four models (U-Net, Double U-Net, SegNet, ResUNet) and a Streamlit dashboard.
""", unsafe_allow_html=True)

st.markdown("""
<h4 class="project-title">2. AI-Powered Transformer Health Monitoring System</h4>
* **Objective**: Developed an AI and IoT-based system for real-time transformer health monitoring, enabling predictive maintenance.
* **Key Achievement**: **Winner at Energathon '25, receiving a ₹3000 cash prize**.
* **Technology**: Designed an AI-Powered IoT device, integrated a **Random Forest ML model** for health scores, and built a **Streamlit dashboard**.
""", unsafe_allow_html=True)

st.markdown("""
<h4 class="project-title">3. EcoAudit - AI-Powered Energy Audit and Optimization App</h4>
* **Objective**: Developed a mobile application to automate household energy audits, helping users monitor consumption and adopt sustainable practices.
* **Key Achievement**: **Second Runner-Up at Energathon '24 hackathon, receiving a ₹1000 cash award**.
* **Technology**: Built using **FlutterFlow, Firebase, and LLaMA API** for AI-based insights and a user-friendly front-end.
""", unsafe_allow_html=True)


# Achievements & Awards

st.subheader("🏆 Achievements")
st.markdown("""
<div class="achievement-list">
* **1st Place**, Energathon '25 - Transformer Health Monitoring System (₹3000 cash prize)
* **1st Place**, Ideaflow Hackathon - Sign Language Translator for Deaf Communication
* **2nd Runner-up**, Energathon '24 - Energy Audit App (₹1000 cash prize)
* **Xylem Innovation Challenge '25** - Satellite Image Water Body Monitoring (\$25 Incentive)
* **3rd Place**, Case Analytics - Business Case Study (160+ teams, ₹1000 cash prize)
* **Overall Winner**, E-Cell Week '25 | **1st Place**, Money Maze - Startup Finance Proposal
* **Finalist**, K!Hacks - Anna University (Ranked in top 25 out of 900+ teams)
</div>
""", unsafe_allow_html=True)


# Leadership & Activities

st.subheader("🤝 Leadership and Extra-Curricular")
st.markdown("""
### **Leadership Qualities**
* **President**, Build Club, TCE - Guided juniors in project building, organized workshops and competitions.
* **Joint Treasurer**, Computer Science & Business Systems Association
* **Student Ambassador**, AI Consortium, TCE - Coordinated events and conducted AI awareness sessions.

### **Sports & Co-Curricular**
* Runner-Up, Zone 16 Basketball - Anna University
* **Best Player**, Handball & Basketball - Interdepartment Matches, TCE
* Team Member, TCE Women's Basketball Team - CM Trophy Tournament
* Participant in **3rd Place Tech Quest** (Technical Quiz), **Stake '25** (Startup Venture Pitching), and several **Hackathons** including **Caterpillar Tech Challenge (Top 30)** and **ISRO Hackathon**.
* Volunteer in NSS - Participated in community service events including blood donation camps.
""")

# Footer
st.markdown("""
<div class="footer">
    Connect with me: kaaviyaa.i@gmail.com | Thank you!
</div>
""", unsafe_allow_html=True)
