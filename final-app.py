# imports
import streamlit as st
import google.generativeai as genai
import re
import time
from getpara import get_one_paragraph_wikipedia

# page configuration
st.set_page_config(page_title="Comprehension Quiz", page_icon="📝", layout="centered")

# api key configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

# try and except for error handling
try:
    # title
    st.title("Comprehension Quiz")

    # paragraph generation
    if "paragraph" not in st.session_state:
        st.session_state.paragraph = get_one_paragraph_wikipedia()
        st.session_state.questions = []
        st.session_state.answers = []
        st.session_state.user_answers = {}
        st.session_state.quiz_generated = False
        st.session_state.start_time = time.time()

    if not st.session_state.quiz_generated:
        if st.button("🔄 New Paragraph"):
            st.session_state.paragraph = get_one_paragraph_wikipedia()
            st.session_state.questions = []
            st.session_state.answers = []
            st.session_state.user_answers = {}
            st.session_state.quiz_generated = False
            st.session_state.start_time = time.time()

    if not st.session_state.quiz_generated:
        st.subheader("📖 Read the Paragraph")
        st.write(st.session_state.paragraph)

        # display word count
        word_count = len(st.session_state.paragraph.split())
        st.caption(f"Word Count: {word_count}")

        # quiz generation
        if st.button("✨ Generate Quiz"):
            #st.spinner("Generating quiz, please wait...")
            elapsed_time = round(time.time() - st.session_state.start_time, 2)
            st.session_state.reading_time = elapsed_time

            question_mcq = (
                f"Generate 5 MCQ questions with 4 options (A, B, C, D) "
                f"based on the following paragraph. "
                f"After each question, provide the correct answer in the format 'Answer: X'. "
                f"Do NOT include explanations.\n\nParagraph: {st.session_state.paragraph}"
            )
            response = chat.send_message(question_mcq)
            text = response.text

            # finding answers
            answers = re.findall(r'Answer:\s*([ABCD])', text, flags=re.IGNORECASE)
            answers = [a.upper() for a in answers]

            # finding questions
            questions_only = re.sub(r'Answer:\s*.*', '', text, flags=re.IGNORECASE).strip()
            questions_only = questions_only.replace("*", "")
            questions_split = re.split(r'\n\s*\d+\.', questions_only)
            questions = [q.strip() for q in questions_split if q.strip()]

            # defining questions and answers
            st.session_state.questions = questions
            st.session_state.answers = answers
            st.session_state.user_answers = {}
            st.session_state.quiz_generated = True
            st.rerun()
            #st.success("Quiz generated successfully!")

    # displaying quiz
    if st.session_state.quiz_generated and st.session_state.questions:
        st.subheader("📝 Quiz")

        for i, q in enumerate(st.session_state.questions):
            lines = q.split("\n")
            question_text = lines[0]
            options = [opt.strip() for opt in lines[1:] if opt.strip()]
            
            # option selection
            st.session_state.user_answers[i] = st.radio(
                f"Q{i+1}. {question_text}",
                options,
                key=f"q{i}"
            )

        # answer submission and evaluation
        if st.button("✅ Submit Answers"):
            correct = 0
            for i, chosen in st.session_state.user_answers.items():
                if i < len(st.session_state.answers):
                    correct_letter = st.session_state.answers[i]
                    if chosen.startswith(correct_letter):
                        correct += 1

            # statistics display
            st.success(f"You got {correct} out of {len(st.session_state.answers)} correct!")

            st.subheader("Correct Answers")
            for i, ans in enumerate(st.session_state.answers, start=1):
                if ans == st.session_state.user_answers[i-1][0]:
                    st.write(f"Q{i}: {ans} ✅")
                else:
                    st.write(f"Q{i}: {ans} ❌ (Your answer: {st.session_state.user_answers[i-1][0]})")

            st.write("Reading time (seconds):", st.session_state.reading_time)

            st.write(f"Reading speed (words per minute):", int(len(st.session_state.paragraph.split())/((int(st.session_state.reading_time))/60)))
            efficiency = int((len(st.session_state.paragraph.split())/((int(st.session_state.reading_time))/60)) * correct / len(st.session_state.answers))
            st.write(f"Reading efficiency (calculated by correct answers x wpm):", efficiency)
            if efficiency <= 49:
                st.write("Your reading efficiency is way below average. Keep practicing!")

            if efficiency >= 50 and efficiency <= 69:
                st.write("Your reading efficiency is below average. You can do better!")

            if efficiency >= 70 and efficiency <= 109:
                st.write("Your reading efficiency is average. Good job!")

            if efficiency >= 110 and efficiency <= 149:
                st.write("Your reading efficiency is above average. Great work!")

            if efficiency >= 150:
                st.write("Your reading efficiency is excellent. Outstanding performance!")
                st.balloons()

# catching exceptions
except Exception as e:
    st.error(f"An internal error occurred, refresh the page and try again. Error details: {e}")