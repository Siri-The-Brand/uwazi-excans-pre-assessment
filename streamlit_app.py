import streamlit as st
import random
import pandas as pd
import os

def main():
    st.set_page_config(page_title="Uwazi Pre-Assessment", page_icon="ssapp_logo.png", layout="centered")
    
    st.title("🌟 Uwazi Pre-Assessment for Excandidates")
    st.subheader("Karibu Soma Siri Afrika! Discover Your Strengths & Map Your Future with the Siri MaP")
    
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
        "Linguistic (Word Smart)": ["I enjoy reading books, articles, or stories.",
                                     "I like writing essays, poems, or journaling.",
                                     "I express myself well through spoken or written words.",
                                     "I enjoy word games like crosswords or Scrabble."],
        "Logical-Mathematical (Number Smart)": ["I enjoy solving puzzles and brain teasers.",
                                                "I can easily work with numbers, formulas, and patterns.",
                                                "I like experimenting and testing theories.",
                                                "I prefer logical reasoning over emotions when making decisions."],
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
    
    # PART 2: CO-CREATING UWAZI
    st.markdown("## 🛠 CO-CREATING UWAZI for Excandidates")
    st.subheader("Step 1: Dream")
    dream_questions = [
        "What kind of interactive space excites you the most?",
        "If you could design an interactive space, what would it look like?",
    ]
    
    dream_responses = {}
    for q in dream_questions:
        response = st.text_area(q)
        dream_responses[q] = response
    
    st.subheader("Step 2: Design")
    design_questions = [
        "What should be included in a program that helps young people develop their talents?",
    ]
    
    design_responses = {}
    for q in design_questions:
        response = st.text_area(q)
        design_responses[q] = response
    
    st.subheader("Step 3: Do")
    do_questions = [
        "What feedback do you have on the ideas presented?",
    ]
    
    do_responses = {}
    for q in do_questions:
        response = st.text_area(q)
        do_responses[q] = response
    
    st.markdown("---")
    
    # Save results to CSV
    if st.button("💾 Save My Results"):
        user_data = {"Name": name, "Age": age, "Education": education, "Career Interests": career_interests}
        for intelligence, score in scores.items():
            user_data[intelligence] = score
        user_data.update(dream_responses)
        user_data.update(design_responses)
        user_data.update(do_responses)
        df = pd.DataFrame([user_data])
        df.to_csv("uwazi_results.csv", mode='a', header=False, index=False)
        st.success("✅ Your results have been saved successfully!")
    
    # Admin View: View All Submitted Results with Password
    admin_password = "UwaziAdmin2025"
    if st.checkbox("📂 View All Submitted Results (Admin Only)"):
        password_input = st.text_input("Enter Admin Password", type="password")
        if password_input == admin_password:
            df = pd.read_csv("uwazi_results.csv")
            st.dataframe(df)
        else:
            st.error("❌ Incorrect Password. Access Denied.")
    
    st.markdown("---")
    st.subheader("🔮 What Comes Next?")
    st.write("✅ Your **Siri MaP** will refine your career pathway based on your insights!")
    st.write("🚀 Stay tuned for deeper insights and personalized career mapping!")
    
if __name__ == "__main__":
    main()
