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
                "How many days per week should a talent program run? What times work best?",
                "What kind of learning experiences excite you the most? (E.g., industry visits, mentorship, real-world projects)",
                "If you could design your dream talent development space, what would it include?"
            ],
            "Kiswahili": [
                "Programu ya vipaji inapaswa kufanyika mara ngapi kwa wiki? Wakati gani ni bora?",
                "Ni uzoefu gani wa kujifunza unakuvutia zaidi? (Mfano, ziara za viwanda, ulezi, miradi halisi)",
                "Ikiwa ungetengeneza nafasi yako bora ya kukuza vipaji, ungehusisha nini?"
            ]
        }
        
        responses = {}
        for q in questions[language]:
            response = st.text_area(q)
            responses[q] = response
            
            media_option = st.radio(f"How would you like to respond to: {q}", ["📸 Take a Photo", "📹 Record a Video", "📁 Upload Media", "✍️ Text Only"], key=q)
            if media_option == "📸 Take a Photo" or media_option == "📹 Record a Video":
                uploaded_file = st.camera_input(f"Capture a response for: {q}")
                if uploaded_file:
                    file_path = save_uploaded_file(uploaded_file)
                    responses[q + " (Media)"] = file_path
            elif media_option == "📁 Upload Media":
                uploaded_file = st.file_uploader(f"Upload a file for: {q}", type=["png", "jpg", "mp4"])
                if uploaded_file:
                    file_path = save_uploaded_file(uploaded_file)
                    responses[q + " (Media)"] = file_path
            
        st.markdown("### 🎨 Sketch Your Dream Talent Program")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=5,
            stroke_color="#000000",
            background_color="#ffffff",
            height=300,
            width=600,
            drawing_mode="freedraw",
            key="canvas_sketch"
        )
        
        if st.button("💾 Save My Co-Creation Responses"):
            user_data = {}
            user_data.update(responses)
            df = pd.DataFrame([user_data])
            df.to_csv("uwazi_cocreation_results.csv", mode='a', header=False, index=False)
            st.success("✅ Your Co-Creation responses have been saved successfully!")
    
    elif choice == "📂 View Responses (Admin)":
        admin_password = "UwaziAdmin2025"
        password_input = st.text_input("Enter Admin Password", type="password")
        if password_input == admin_password:
            df1 = pd.read_csv("uwazi_results.csv")
            st.subheader("📊 Pre-Assessment Results")
            st.dataframe(df1)
            
            df2 = pd.read_csv("uwazi_cocreation_results.csv")
            st.subheader("🛠 Co-Creation Responses")
            st.dataframe(df2)
        else:
            st.error("❌ Incorrect Password. Access Denied.")
    
    st.markdown("---")
    st.subheader("🔮 What Comes Next?")
    st.write("✅ Your **Siri MaP** will refine your career pathway based on your insights!")
    st.write("🚀 Stay tuned for deeper insights and personalized career mapping!")
    
if __name__ == "__main__":
    main()
