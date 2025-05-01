# Title
st.title("⚗️ Games Kimia")

# Description
st.write("""
Aplikasi ini berguna untuk mempelajari tabel periodic unsur""")

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

def ask_question():
    element = random.choice(periodic_table)
    question_type = random.choice(["symbol", "number", "group", "period"])
    
    if question_type == "symbol":
        answer = input(f"\nApa simbol dari unsur '{element['name'].capitalize()}'? ").strip()
        return answer.lower() == element['symbol'].lower()
    
    elif question_type == "number":
        answer = input(f"\nBerapa nomor atom dari '{element['name'].capitalize()}'? ").strip()
        return answer == str(element['number'])
    
    elif question_type == "group":
        answer = input(f"\nGolongan berapa unsur '{element['name'].capitalize()}'? ").strip()
        return answer == str(element['group'])
    
    elif question_type == "period":
        answer = input(f"\nPeriode berapa unsur '{element['name'].capitalize()}'? ").strip()
        return answer == str(element['period'])

def play_quiz():
    print("=== Kuis Tabel Periodik ===")
    score = 0

    for i in range(5):
        if ask_question():
            print("✅ Benar!")
            score += 1
        else:
            print("❌ Salah.")
    
    print(f"\nSkor akhir kamu: {score}/5")

if __name__ == "__main__":
    play_quiz()
