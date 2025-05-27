import streamlit as st
from PIL import Image
import base64

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Profile Image
image = Image.open("profile.jpg")
st.image(image, width=240 ,caption="Kaaviyaa Ilangovan")

# Header Section
st.markdown("""
    <div class="header">
        <h1>👩‍💻 Kaaviyaa Ilangovan</h1>
        <p>Second Year CSBS | TCE | AI & Computer Vision Enthusiast</p>
        <p><a href="mailto:kaaviyaa.I@gmail.com">kaaviyaa.i@gmail.com</a> | 📞 8608508638</p>
    </div>
""", unsafe_allow_html=True)

# Resume download button
def get_pdf_download_link(pdf_path):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    href = f'<a class="btn" href="data:application/octet-stream;base64,{base64_pdf}" download="Kaaviyaa_Resume.pdf">📄 Download Resume</a>'
    return href

st.markdown(get_pdf_download_link("Kaaviyaa_Resume.pdf"), unsafe_allow_html=True)

# Full Summary from Resume
st.subheader("🌟 Summary")
st.success("""
I am a Second Year Computer Science and Business Systems Student at Thiagarajar College of Engineering with a Keen Interest in Computer Vision and Machine Learning. I am Eager to Apply my Skills in Real-World Scenarios through Internships or Apprenticeships. I have a strong inclination towards Research and Development. I am committed to contributing to innovative projects, seeking Professional connections to collaborate with like-minded individuals.
""")

# Experience
st.subheader("💼 Experience")
st.markdown("""
**Web Development Intern** — Big Bucks Innovation (07/2024 - 08/2024)  
• Developed front-end interfaces using HTML, CSS, and JavaScript.
""")

# Education
st.subheader("🎓 Education")
st.markdown("""
- **B.Tech - CSBS**, Thiagarajar College of Engineering — *CGPA: 9.10*
- **12th Grade**, Bhaktavatsalam Vidyashram — *93.8%*
- **10th Grade**, Bhaktavatsalam Vidyashram — *88.8%*
""")

# Skills
st.subheader("🛠 Skills")
st.markdown("""
- **Languages**: Python, Java (Advanced), C, C++ (Intermediate)
- **Web Dev**: HTML, CSS, JavaScript
- **Libraries/Frameworks**: NumPy, Pandas, Scikit-learn, OpenCV, TensorFlow, Keras, MediaPipe, Matplotlib, Seaborn
- **Tools**: Git, GitHub
""")

# Certifications
st.subheader("📜 Certifications")
st.markdown("""
- Machine Learning - NPTEL  
- Python for Data Science - NPTEL  
- Programming in Python - CEC  
- Prompt Engineering & ChatGPT Courses - Infosys, Great Learning  
- Generative AI - Guvi Geek Networks
""")

# Projects
st.subheader("🚀 Projects")
st.markdown("""
- **AI-Powered Waste Segregation System
Used DenseNet, ResNet-50, and InceptionV3 for multi-class waste classification using computer vision.

- **Building Crack Detection & Severity Classification
Built a vision-based model to detect cracks and classify severity using deep learning.

- **Deepfake Detection using LSTM
Developed an LSTM-based system to identify deepfakes from facial video data.

- **Number Recognition (OCR)
Implemented OCR using OpenCV and Tesseract for handwritten and printed number recognition.

""")


# Research
st.subheader("📖 Research")
st.markdown("""
- Titled **“IoT and ML-Integrated Forest Fire Detection”**  
Presented at International Conference on Green AI (April 2025). Will be published in Springer Artificial Intelligence Integrated Enhanced  
Software and Systems Engineering.
""")

# Achievements
st.subheader("🏆 Achievements")
st.markdown("""
- 🏆 Winner – Ideaflow Intra College Hackathon 
- 🥈 Energython 24 – sencond runner ₹1000 prize  
- 🥈 Hackerz National level case Analytics Event sencond runner up  
- 🧠 Conducted image processing workshop for 100+ juniors
- 🥈 Tech Quest sencond runner up 
- 🎯 Finalist – K! Hacks (Top 900+ teams)
""")

# Co/Extra Curricular
st.subheader("🤝 Activities")
st.markdown("""
- **Technical Lead** – Build Club  
- **Student Ambassador** – AI Consortium, TCE  
- **Joint Treasurer** – IUCEE EWB TCE student chapter
- **Entrepreneurship Cell Member**  
- 🏀 Basketball & Handball Player  
- 🏅 “Best Player” in inter Department Matches  
""")

# Footer
st.markdown("""
<div class="footer">
    Connect with me on kaaviyaa.i@gmail.com 
</div>
""", unsafe_allow_html=True)
