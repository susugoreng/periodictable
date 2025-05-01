import streamlit as st
import random

# Daftar contoh unsur (bisa diperluas)
periodic_table = [
    {"name": "hidrogen", "symbol": "H", "number": 1, "group": 1, "period": 1},
    {"name": "helium", "symbol": "He", "number": 2, "group": 18, "period": 1},
    {"name": "litium", "symbol": "Li", "number": 3, "group": 1, "period": 2},
    {"name": "berilium", "symbol": "Be", "number": 4, "group": 2, "period": 2},
    {"name": "boron", "symbol": "B", "number": 5, "group": 13, "period": 2},
    {"name": "karbon", "symbol": "C", "number": 6, "group": 14, "period": 2},
    {"name": "nitrogen", "symbol": "N", "number": 7, "group": 15, "period": 2},
    {"name": "oksigen", "symbol": "O", "number": 8, "group": 16, "period": 2},
    {"name": "fluorin", "symbol": "F", "number": 9, "group": 17, "period": 2},
    {"name": "neon", "symbol": "Ne", "number": 10, "group": 18, "period": 2}
]

# Inisialisasi state
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.question_num = 0
    st.session_state.current_question = None
    st.session_state.feedback = ""

def generate_question():
    element = random.choice(periodic_table)
    question_type = random.choice(["symbol", "number", "group", "period"])
    return {"element": element, "type": question_type}

st.title("🔬 Kuis Tabel Periodik")

if st.session_state.question_num < 5:
    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question()

    q = st.session_state.current_question
    e = q["element"]
    q_text = ""
    correct_answer = ""

    if q["type"] == "symbol":
        q_text = f"Apa simbol dari unsur '{e['name'].capitalize()}'?"
        correct_answer = e["symbol"]
    elif q["type"] == "number":
        q_text = f"Berapa nomor atom dari '{e['name'].capitalize()}'?"
        correct_answer = str(e["number"])
    elif q["type"] == "group":
        q_text = f"Golongan berapa unsur '{e['name'].capitalize()}'?"
        correct_answer = str(e["group"])
    elif q["type"] == "period":
        q_text = f"Periode berapa unsur '{e['name'].capitalize()}'?"
        correct_answer = str(e["period"])

    user_input = st.text_input(q_text, key=st.session_state.question_num)

    if st.button("Kirim Jawaban"):
        if user_input.strip().lower() == correct_answer.lower():
            st.session_state.score += 1
            st.session_state.feedback = "✅ Benar!"
        else:
            st.session_state.feedback = f"❌ Salah. Jawaban yang benar: {correct_answer}"

        st.session_state.question_num += 1
        st.session_state.current_question = None

st.markdown(f"### Skor: {st.session_state.score}/5")
st.write(st.session_state.feedback)

if st.session_state.question_num >= 5:
    st.success(f"🎉 Kuis selesai! Skor akhir kamu: {st.session_state.score}/5")
    if st.button("Main Lagi"):
        for key in ["score", "question_num", "current_question", "feedback"]:
            st.session_state[key] = 0 if key == "score" or key == "question_num" else None
