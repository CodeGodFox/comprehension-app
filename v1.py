import wikipedia
from groq import Groq
import time
import os
import re

client = Groq(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key

def get_random_wiki_paragraphs():
    try:
        title = wikipedia.random()
        para = wikipedia.summary(title, sentences=10)
        if para.count('.') < 10:
            return get_random_wiki_paragraphs()

        question = f"Reduce this to 300 words, 1 paragraph: {para}"
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}]
        )
        return completion.choices[0].message.content.strip()
    
    except (wikipedia.exceptions.PageError, Exception):
        return get_random_wiki_paragraphs()

paragraph = get_random_wiki_paragraphs()

# Generate MCQ Questions
question_mcq = (f"Generate 5 MCQ question with 4 options based on the following paragraph with answers: {paragraph}")

questions_completion_mcq = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": question_mcq}]
)
questions_completion_mcq_final = questions_completion_mcq.choices[0].message.content.strip()

print(paragraph)
#time.sleep(180)
done = input("Enter anything when done: ")
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