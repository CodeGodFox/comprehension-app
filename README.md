# 📝 Comprehension Quiz

A simple AI-powered reading comprehension app built with **Streamlit**. The app fetches a random paragraph from Wikipedia, gives the user time to read it, and then generates a short multiple-choice quiz to test how well they understood and remembered the content.

## ✨ Features

* 📖 **Random Wikipedia Paragraphs** — Fetches a random paragraph from Wikipedia for each session.
* ⏱️ **Reading Time Tracking** — Measures how long the user takes to read the paragraph.
* 🤖 **AI-Generated Questions** — Uses Google's Gemini model to generate comprehension questions based on the paragraph.
* ❓ **Multiple-Choice Quiz** — Generates 5 questions with 4 options each.
* ✅ **Automatic Evaluation** — Checks the user's answers and calculates their score.
* 📊 **Reading Statistics** — Displays:

  * Reading time
  * Reading speed (words per minute)
  * Quiz score
  * Reading efficiency
* 🎈 **Performance Feedback** — Provides feedback based on the user's reading efficiency.

## 🧠 How It Works

The app follows a simple process:

```text
Random Wikipedia Paragraph
          ↓
      User Reads
          ↓
   Reading Time Recorded
          ↓
    Gemini Generates Quiz
          ↓
      User Answers
          ↓
     Answers Evaluated
          ↓
 Reading Speed + Efficiency
```

### 1. Get a paragraph

The app uses the `get_one_paragraph_wikipedia()` function to retrieve a random paragraph from Wikipedia.

### 2. Read the paragraph

The paragraph is displayed along with its word count. A timer starts when the paragraph is loaded so the app can measure the user's reading time.

### 3. Generate the quiz

After finishing the paragraph, the user clicks **Generate Quiz**.

Gemini receives the paragraph and is asked to generate **5 multiple-choice questions**, each with four options.

### 4. Take the quiz

The generated questions and options are displayed using Streamlit radio buttons.

### 5. Calculate the results

After submitting the answers, the app calculates the user's score and displays their reading statistics.

The reading speed is calculated as:

```text
Reading Speed = Words Read / Reading Time (minutes)
```

The app also calculates a reading efficiency score based on both reading speed and comprehension:

```text
Reading Efficiency = WPM × Comprehension Accuracy
```

## 🛠️ Technologies Used

* **Python**
* **Streamlit** — Web app interface
* **Google Gemini** — AI-generated comprehension questions
* **Wikipedia** — Source of reading material
* **Regular Expressions** — Parsing AI-generated questions and answers

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/comprehension-quiz.git
cd comprehension-quiz
```

### 2. Install dependencies

```bash
pip install streamlit google-genai wikipedia
```

Install any additional dependencies required by `getpara.py`.

### 3. Add your Gemini API key

Open `final-app.py` and find the API key section:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

Replace `YOUR_API_KEY_HERE` with your own Gemini API key.

You can obtain a Gemini API key from **Google AI Studio**.

> ⚠️ **Important:** If you upload this project to a public GitHub repository, **do not commit your API key**. Anyone who can see the code could potentially use your key. Replace it with a placeholder before uploading the project publicly.

## ▶️ Running the App

Start the Streamlit application with:

```bash
streamlit run final-app.py
```

The app will open in your browser.

## 📁 Project Structure

```text
comprehension-quiz/
│
├── final-app.py
├── getpara.py
└── README.md
```

## 📊 Example

A typical session looks like:

**Paragraph**

> The user receives a randomly selected paragraph from Wikipedia.

**Reading**

The user reads the paragraph while the app tracks their reading time.

**Quiz**

The AI generates questions such as:

```text
Q1. What was the main reason for...?

A. ...
B. ...
C. ...
D. ...
```

**Results**

```text
You got 4 out of 5 correct!

Reading time: 42 seconds
Reading speed: 142 WPM
Reading efficiency: 113
```

## 🎯 Purpose

The goal of this project is to combine **reading speed** and **reading comprehension** into a simple interactive exercise.

Reading quickly isn't necessarily useful if the reader doesn't understand what they read. By testing comprehension immediately after reading, the app provides a simple way to track both aspects of reading performance.

## 🚀 Future Improvements

Some possible improvements include:

* 📈 Track performance across multiple sessions
* 📊 Add graphs for reading speed and comprehension over time
* 🎚️ Add difficulty levels
* ⏳ Add configurable reading-time limits
* 🧠 Generate different types of questions
* 🏆 Add personal bests and high scores
* 👤 Add user accounts and progress tracking
* 📚 Allow users to choose topics
* 🎯 Improve AI question parsing and validation
* 📱 Improve the mobile experience

## 📜 Disclaimer

The reading material is sourced from Wikipedia. This project is intended for educational and personal use as a reading-comprehension exercise.

## 👨‍💻 Author

Created as a Python/AI project using **Streamlit** and **Google Gemini**.

