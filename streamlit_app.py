import streamlit as st
import random
import pandas as pd

def main():
    st.set_page_config(page_title="Uwazi Pre-Assessment", page_icon="ssapp_logo.png", layout="centered")
    
   
    st.title("🌟 Uwazi Pre-Assessment for Excandidates")
    st.subheader("Karibu Soma Siri Afrika! Get ready to Discover Your Strengths & Map Your Future with the Siri MaP")
    
    # Personal Information
    st.markdown("### 📝 Personal Information")
    name = st.text_input("What's your Full Name")
    age = st.number_input("Age", min_value=14, max_value=25, step=1)
    education = st.text_input("Where did you go to High School?")
    career_interests = st.text_area("Career Interests")
    
    st.markdown("---")
    
    # Section 1: Multiple Intelligences Self-Assessment
    st.markdown("### 🧠 Multiple Intelligences Self-Assessment")
    st.write("Rate yourself from 1 (Strongly Disagree) to 5 (Strongly Agree)")
    
    intelligences = {
        "Linguistic (Word Smart)": [
            "I enjoy reading books, articles, or stories.",
            "I like writing essays, poems, or journaling.",
            "I express myself well through spoken or written words.",
            "I enjoy word games like crosswords or Scrabble."
        ],
        "Logical-Mathematical (Number Smart)": [
            "I enjoy solving puzzles and brain teasers.",
            "I can easily work with numbers, formulas, and patterns.",
            "I like experimenting and testing theories.",
            "I prefer logical reasoning over emotions when making decisions."
        ],
        "Spatial (Picture Smart)": [
            "I enjoy drawing, painting, or designing.",
            "I can easily visualize objects, patterns, or spaces in my mind.",
            "I enjoy photography, video editing, or working with graphics.",
            "I understand and use maps, charts, and diagrams easily."
        ],
        "Bodily-Kinesthetic (Body Smart)": [
            "I enjoy physical activities such as sports, dance, or acting.",
            "I learn best when I can move around and use my hands.",
            "I have good hand-eye coordination and balance.",
            "I like building, crafting, or working with physical objects."
        ],
        "Musical (Music Smart)": [
            "I enjoy listening to music and can recognize rhythms easily.",
            "I can play a musical instrument or enjoy singing.",
            "I create beats, melodies, or lyrics in my mind.",
            "I learn well when information is presented in a rhythmic or musical form."
        ],
        "Interpersonal (People Smart)": [
            "I enjoy working in groups and collaborating with others.",
            "I easily understand people’s feelings and perspectives.",
            "I am good at resolving conflicts and helping others.",
            "I like networking and forming new relationships."
        ],
        "Intrapersonal (Self Smart)": [
            "I spend time reflecting on my thoughts and actions.",
            "I have a strong sense of self-awareness and personal goals.",
            "I enjoy journaling or meditating to understand myself better.",
            "I prefer working independently rather than in groups."
        ],
        "Naturalistic (Nature Smart)": [
            "I enjoy spending time in nature and observing animals or plants.",
            "I am passionate about environmental conservation and sustainability.",
            "I like gardening, hiking, or working with natural elements.",
            "I notice patterns and relationships in nature."
        ]
    }
    
    scores = {}
    for intelligence, statements in intelligences.items():
        st.subheader(f"{intelligence}")
        total_score = 0
        for statement in statements:
            score = st.slider(statement, 1, 5, 3)
            total_score += score
        scores[intelligence] = total_score
    
    st.markdown("---")
    
    # Section 2: Fun Aptitude Test
    st.markdown("### 🎭 Fun Aptitude Test")
    st.write("Try these quick challenges based on your strengths!")
    
    task_prompts = random.sample([
        "You’re designing a new school system. How would you make learning more fun?",
        "Imagine you're given unlimited resources to solve a global challenge. What would you focus on?",
        "You have 60 seconds to create a short story with the words: 'dream', 'journey', and 'unexpected'. Go!",
        "Create a simple math puzzle using numbers under 20.",
        "If you could design a new musical instrument, what would it sound like and look like?",
        "Sketch a futuristic city and describe how technology and nature coexist.",
        "Develop a 3-step plan to help a community reduce plastic waste.",
        "Come up with a game that teaches people about financial literacy.",
        "Write a motivational speech for students preparing for their final exams."
    ], 3)
    
    for i, task in enumerate(task_prompts, 1):
        st.write(f"🚀 Task {i}: {task}")
        response = st.text_area(f"Your response to Task {i}")
    
    st.markdown("---")
    
    # Display Results in the App
    st.subheader("📊 Your Assessment Summary")
    st.write(f"**👤 Name:** {name}")
    st.write(f"**🎓 Education:** {education}")
    st.write(f"**💡 Career Interests:** {career_interests}")
    
    st.subheader("🧠 Your Strengths Based on Multiple Intelligences")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for intelligence, score in sorted_scores:
        st.write(f"**{intelligence}:** {score}/20")
    
    # Save results to CSV
    if st.button("💾 Save My Results"):
        user_data = {"Name": name, "Age": age, "Education": education, "Career Interests": career_interests}
        for intelligence, score in scores.items():
            user_data[intelligence] = score
        df = pd.DataFrame([user_data])
        df.to_csv("uwazi_results.csv", mode='a', header=False, index=False)
        st.success("✅ Your results have been saved successfully!")
    
    # Admin View: View All Submitted Results
    if st.checkbox("📂 View All Submitted Results (Admin Only)"):
        df = pd.read_csv("uwazi_results.csv")
        st.dataframe(df)
    
    st.markdown("---")
    st.subheader("🔮 What Comes Next?")
    st.write("✅ After Uwazi and exposure to real-world problem-solving, we will refine your career pathway.")
    st.write("✅ Your **Siri MaP** will provide a more accurate, detailed guide based on your strengths and experiences.")
    st.write("🚀 Stay tuned for deeper insights and personalized career mapping!")

if __name__ == "__main__":
    main()
