import streamlit as st
import Main

st.set_page_config(
    page_title="Word Guessing Game",
    page_icon="🎯",
    layout="centered",
)

DEEP_NAVY = "#0A1128"
DEEP_NAVY_LIGHT = "#132347"
ELECTRIC_BLUE = "#00A8FF"
ELECTRIC_BLUE_SOFT = "#3FC1FF"
TEXT_LIGHT = "#E8F1FF"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {DEEP_NAVY};
        color: {TEXT_LIGHT};
    }}
    h1, h2, h3, h4 {{
        color: {ELECTRIC_BLUE_SOFT} !important;
        font-family: 'Trebuchet MS', sans-serif;
    }}
    div[data-testid="stSidebar"] {{
        background-color: {DEEP_NAVY_LIGHT};
        border-right: 1px solid {ELECTRIC_BLUE};
    }}
    .stButton > button {{
        background-color: {ELECTRIC_BLUE};
        color: {DEEP_NAVY};
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        transition: all 0.15s ease-in-out;
    }}
    .stButton > button:hover {{
        background-color: {ELECTRIC_BLUE_SOFT};
        color: {DEEP_NAVY};
        transform: scale(1.03);
    }}
    div[data-baseweb="select"] > div, .stTextInput > div > div > input {{
        background-color: {DEEP_NAVY_LIGHT} !important;
        color: {TEXT_LIGHT} !important;
        border: 1px solid {ELECTRIC_BLUE} !important;
    }}
    .letter-box {{
        display: inline-block;
        width: 42px;
        height: 48px;
        line-height: 48px;
        margin: 3px;
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        border-radius: 6px;
        background-color: {DEEP_NAVY_LIGHT};
        border: 2px solid {ELECTRIC_BLUE};
        color: {ELECTRIC_BLUE_SOFT};
    }}
    .letter-box.filled {{
        background-color: {ELECTRIC_BLUE};
        color: {DEEP_NAVY};
        border-color: {ELECTRIC_BLUE_SOFT};
    }}
    .hint-card {{
        background-color: {DEEP_NAVY_LIGHT};
        border-left: 4px solid {ELECTRIC_BLUE};
        padding: 0.8em 1em;
        border-radius: 6px;
        margin-bottom: 1em;
    }}
    .stProgress > div > div > div > div {{
        background-color: {ELECTRIC_BLUE};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

def init_state():
    defaults = {
        "level": "easy",
        "secret": None,
        "attempts_used": 0,
        "max_attempts": Main.get_max_attempts("easy"),
        "guesses": [],
        "game_over": False,
        "won": False,
        "score": 0,
        "total_score": 0,
        "wins": 0,
        "losses": 0,
        "streak": 0,
        "best_streak": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def start_new_round(level: str):
    st.session_state.level = level
    st.session_state.secret = Main.pick_word(level)
    st.session_state.max_attempts = Main.get_max_attempts(level)
    st.session_state.attempts_used = 0
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.score = 0


init_state()

with st.sidebar:
    st.header("🎮 Game Stats")
    st.metric("Total score", st.session_state.total_score)
    col1, col2 = st.columns(2)
    col1.metric("Wins", st.session_state.wins)
    col2.metric("Losses", st.session_state.losses)
    st.metric("Current streak", st.session_state.streak)
    st.metric("Best streak", st.session_state.best_streak)

    st.divider()
    st.subheader("Difficulty")
    level_choice = st.selectbox(
        "Choose a level",
        options=["easy", "medium", "hard"],
        index=["easy", "medium", "hard"].index(st.session_state.level),
        format_func=lambda x: x.capitalize(),
    )
    if st.button("🔄 New word", use_container_width=True):
        start_new_round(level_choice)
        st.rerun()

st.title("🎯 Word Guessing Game")
st.caption("Deep Navy & Electric Blue edition — guess the word before you run out of attempts.")

if st.session_state.secret is None:
    start_new_round(level_choice)

secret = st.session_state.secret
attempts_left = st.session_state.max_attempts - st.session_state.attempts_used

st.markdown(
    f"""<div class="hint-card">💡 <b>Hint:</b> {Main.get_hint(secret)}</div>""",
    unsafe_allow_html=True,
)

progress_ratio = 1 - (attempts_left / st.session_state.max_attempts)
st.progress(min(max(progress_ratio, 0.0), 1.0))
st.write(f"**Attempts left:** {attempts_left} / {st.session_state.max_attempts}  |  **Word length:** {len(secret)} letters")

if st.session_state.guesses:
    last_guess = st.session_state.guesses[-1]
    pattern = Main.letter_pattern(last_guess, secret)
    boxes = "".join(
        f'<span class="letter-box filled">{ch}</span>' if ch != "_" else '<span class="letter-box">_</span>'
        for ch in pattern
    )
    st.markdown(boxes, unsafe_allow_html=True)

if not st.session_state.game_over:
    with st.form("guess_form", clear_on_submit=True):
        guess = st.text_input("Enter your guess", label_visibility="collapsed", placeholder="Type your guess here...")
        submitted = st.form_submit_button("Guess 🔵", use_container_width=True)

    if submitted and guess.strip():
        normalized = Main.normalize_guess(guess)
        st.session_state.attempts_used += 1
        st.session_state.guesses.append(normalized)

        if Main.is_correct(normalized, secret):
            st.session_state.game_over = True
            st.session_state.won = True
            score = Main.compute_score(st.session_state.level, st.session_state.attempts_used)
            st.session_state.score = score
            st.session_state.total_score += score
            st.session_state.wins += 1
            st.session_state.streak += 1
            st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
        elif st.session_state.attempts_used >= st.session_state.max_attempts:
            st.session_state.game_over = True
            st.session_state.won = False
            st.session_state.losses += 1
            st.session_state.streak = 0
        st.rerun()

if st.session_state.game_over:
    if st.session_state.won:
        st.success(
            f"🎉 Correct! The word was **{secret}**. "
            f"Solved in {st.session_state.attempts_used} attempt(s) → +{st.session_state.score} points."
        )
        st.balloons()
    else:
        st.error(f"💥 Out of attempts! The word was **{secret}**.")

    if st.button("▶️ Play again", use_container_width=True):
        start_new_round(st.session_state.level)
        st.rerun()

if st.session_state.guesses:
    with st.expander("📜 Guess history"):
        for i, g in enumerate(st.session_state.guesses, start=1):
            marker = "✅" if Main.is_correct(g, secret) else "❌"
            st.write(f"{i}. {marker} {g}")