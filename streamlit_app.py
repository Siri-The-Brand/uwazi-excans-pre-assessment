import streamlit as st
import random
import pandas as pd
import os
from streamlit_drawable_canvas import st_canvas
from datetime import datetime

data_folder = "uploads"
os.makedirs(data_folder, exist_ok=True)

def save_uploaded_file(uploaded_file, folder=data_folder):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(folder, f"{timestamp}_{uploaded_file.name}")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def main():
    st.set_page_config(page_title="Uwazi Co-Creation Hub", page_icon="🌍", layout="wide")
    
    st.title("🌟 Uwazi Co-Creation Hub")
    st.subheader("Karibu Soma Siri Afrika! Let's Design the Future of Talent Discovery")
    
    menu = ["📊 Pre-Assessment", "🎨 Co-Creation Lab", "📂 View Responses (Admin)"]
    choice = st.sidebar.radio("Navigate", menu)
    
    if choice == "📊 Pre-Assessment":
        st.markdown("### 📝 Personal Information")
        name = st.text_input("What's your Full Name")
        age = st.number_input("Age", min_value=14, max_value=25, step=1)
        education = st.text_input("Where did you go to High School?")
        career_interests = st.text_area("Career Interests")
        
        st.markdown("### 🧠 Multiple Intelligences Self-Assessment")
        st.write("Rate yourself from 1 (Strongly Disagree) to 5 (Strongly Agree)")
        
        intelligences = {
            "Linguistic (Word Smart)": ["I enjoy reading books, articles, or stories.",
                                         "I like writing essays, poems, or journaling."],
            "Logical-Mathematical (Number Smart)": ["I enjoy solving puzzles and brain teasers.",
                                                    "I can easily work with numbers, formulas, and patterns."],
        }
        
        scores = {}
        for intelligence, statements in intelligences.items():
            st.subheader(f"{intelligence}")
            total_score = 0
            for statement in statements:
                score = st.slider(statement, 1, 5, 3)
                total_score += score
            scores[intelligence] = total_score
        
        if st.button("💾 Save My Pre-Assessment Results"):
            user_data = {"Name": name, "Age": age, "Education": education, "Career Interests": career_interests}
            for intelligence, score in scores.items():
                user_data[intelligence] = score
            df = pd.DataFrame([user_data])
            df.to_csv("uwazi_results.csv", mode='a', header=False, index=False)
            st.success("✅ Your pre-assessment results have been saved successfully!")
    
    elif choice == "🎨 Co-Creation Lab":
        st.markdown("## 🛠 Designing the Best Talent Discovery Program")
        
        st.write("Choose your preferred language: ")
        language = st.radio("Language", ["English", "Kiswahili"])
        
        questions = {
            "English": [
                "What kind of space would make talent discovery fun and exciting for you?",
                "If you could design your dream talent discovery program, what would it look like?",
                "What are creative ways we could explore different talents together?",
                "What excites you the most about discovering and using your talents?",
                "How many days a week should the program run? What time would be best?",
                "What kind of learning experiences would you like? (E.g., company visits, job shadowing, hands-on projects)",
                "What should a talent program include to help you develop your skills and career goals?",
                "Would you benefit from guest speakers, internships, or real-world projects?",
                "What support do you need to take action on your ideas?",
                "What activities make you feel most alive and energized?",
                "What is something you've done that made you feel proud?",
                "Have you ever used your talent to help someone or solve a problem? What happened?",
                "Which careers or industries excite you the most?",
                "What careers have you thought about but need more exposure to?",
                "If you had unlimited resources, what problem would you want to solve first?",
                "What support would help you turn your ideas into reality?",
                "What is one action you can take today to develop your talent or career interest?",
                "How will you hold yourself accountable for your growth?",
                "How would you like to stay engaged with Uwazi moving forward?"
            ],
            "Kiswahili": [
                "Ni aina gani ya nafasi ingefanya kugundua vipaji kuwa jambo la kufurahisha kwako?",
                "Ikiwa ungeweza kubuni programu bora ya kugundua vipaji, ingekuwaje?",
                "Ni njia zipi za ubunifu ambazo tunaweza kutumia kuchunguza vipaji kwa pamoja?",
                "Ni nini kinakuvutia zaidi kuhusu kugundua na kutumia vipaji vyako?",
                "Ungependa programu ifanyike mara ngapi kwa wiki? Wakati gani ungependa?",
                "Ungependa uzoefu gani wa kujifunza? (Mfano, ziara za makampuni, kujifunza kwa vitendo, miradi ya mikono)",
                "Programu ya vipaji inapaswa kujumuisha nini ili kusaidia kukuza ujuzi na malengo yako ya kazi?",
                "Ungepata faida kutoka kwa wazungumzaji wa wageni, mafunzo ya kazi, au miradi halisi?",
                "Ungehitaji msaada gani ili kuchukua hatua kuhusu mawazo yako?",
                "Ni shughuli zipi zinakufanya ujisikie hai na mwenye shauku?",
                "Ni kitu gani umewahi kufanya kilichokufanya ujisikie fahari?",
                "Umewahi kutumia kipaji chako kusaidia mtu au kutatua tatizo? Ilikuwaje?",
                "Ni taaluma au viwanda vipi vinakuvutia zaidi?",
                "Ni taaluma gani umewahi kufikiria lakini unahitaji maelezo zaidi kuyahusu?",
                "Ikiwa ungekuwa na rasilimali zote unazohitaji, ni tatizo gani ungetaka kulitatua kwanza?",
                "Msaada gani ungehitaji ili kufanya mawazo yako kuwa halisi?",
                "Ni hatua gani moja unaweza kuchukua leo kukuza kipaji chako au maslahi yako ya kazi?",
                "Utawezaje kujibebesha jukumu la ukuaji wako?",
                "Ungependa kushiriki vipi na Uwazi siku zijazo?"
            ]
        }
        
        responses = {}
        for q in questions[language]:
            response = st.text_area(q)
            responses[q] = response
            
            media_option = st.radio(f"How would you like to respond to: {q}", ["📸 Take a Photo", "📹 Record a Video", "📁 Upload Media", "✍️ Text Only"], key=q)
            if media_option in ["📸 Take a Photo", "📹 Record a Video"]:
                uploaded_file = st.camera_input(f"Capture a response for: {q}")
                if uploaded_file:
                    file_path = save_uploaded_file(uploaded_file)
                    responses[q + " (Media)"] = file_path
            elif media_option == "📁 Upload Media":
                uploaded_file = st.file_uploader(f"Upload a file for: {q}", type=["png", "jpg", "mp4"])
                if uploaded_file:
                    file_path = save_uploaded_file(uploaded_file)
                    responses[q + " (Media)"] = file_path
        
        if st.button("💾 Save My Co-Creation Responses"):
            user_data = {}
            user_data.update(responses)
            df = pd.DataFrame([user_data])
            df.to_csv("uwazi_cocreation_results.csv", mode='a', header=False, index=False)
            st.success("✅ Your Co-Creation responses have been saved successfully!")

if __name__ == "__main__":
    main()
