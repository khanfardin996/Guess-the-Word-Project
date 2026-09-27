### The actual and no AI used Cose is in the The code With Actual Logic.py

Word Guessing Game

A word-guessing game built with Python and Streamlit, styled in a Deep Navy + Electric Blue theme.

Files
main.py — Core game logic (word lists, hints, guess-checking, scoring). No UI code — pure functions only.
app.py — Streamlit front-end. Handles session state, rendering, and styling. Imports everything it needs from main.py.
Requirements
Python 3.8+
streamlit

Install streamlit if you don't already have it:

pip install streamlit
How to Run

From the folder containing both files:

python -m streamlit run app.py

This opens the game in your browser (usually at http://localhost:8501).

How to Play
Pick a difficulty in the sidebar: Easy, Medium, or Hard.
A hint is shown for the secret word.
Type a guess and submit. Correctly placed letters light up in their position; the rest show as blanks.
Keep guessing until you get the word or run out of attempts (8 for Easy, 7 for Medium, 6 for Hard).
Click "New word" or "Play again" to start another round.
Features
Difficulty-based word lists and hints (30 words each for Easy/Medium/Hard)
Limited attempts ("lives") per round, scaled by difficulty
Scoring system — fewer attempts and higher difficulty earn more points
Session stats: total score, wins, losses, current streak, best streak
Letter-by-letter visual feedback boxes
Progress bar showing attempts used
Guess history log
Deep Navy (
#0A1128) + Electric Blue (
#00A8FF) custom theme
Project Structure
.
├── app.py # Streamlit UI
├── main.py # Game logic
└── README.md
