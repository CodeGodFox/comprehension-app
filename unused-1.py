import wikipedia
import google.generativeai as genai
import time
import os
import re
from getpara import get_one_paragraph_wikipedia


API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat(history=[])

paragraph = get_one_paragraph_wikipedia(n_sentences=10)

# Generate MCQ Questions
question_mcq = (f"Generate 5 MCQ question with 4 options based on the following paragraph with answers after every question. Do not include any explanation of each answer: {paragraph}")

response = chat.send_message(question_mcq)

questions_completion_mcq_final = response.text



print(paragraph)
#time.sleep(180)
print("")
done = input("Press Enter when done reading the paragraph...")
os.system('cls' if os.name == 'nt' else 'clear')
print("⏳ Time's up! Paragraph hidden.")

import re

# Find all answers
answers = re.findall(r'Answer:\s*(.*)', questions_completion_mcq_final, flags=re.IGNORECASE)
#print(answers)

# Remove all 'Answer: ...' occurrences from the text
questions_completion_mcq_final = re.sub(r'Answer:\s*.*', '', questions_completion_mcq_final, flags=re.IGNORECASE).strip()

print(questions_completion_mcq_final)
print("\n")
user_answers = [ans.strip() for ans in input("Enter your answers letters (A/B/C/D, comma-separated): ").split(',')]
i = 0
correct_answers = 0
for answer in answers:
    match = re.search(r'[ABCD]', answer)

    if match:
        first_char = match.group(0)
        if first_char.lower() == user_answers[i].lower().strip():
            correct_answers += 1

    i += 1

print(f"\nYou got {correct_answers} out of {len(answers)} correct!")
print("\nAnswers were:")
for ans in answers:
    print(ans.strip())

done = input("Press Enter to exit...")