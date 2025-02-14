import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.title("❤️ Valentine's Day Ninja Scenario Game ❤️")
    st.write("Hello Nam-Nam (Hidden leaf village Shinobi)!\n Welcome to your special Valentine's Day game! Answer these fun scenarios and see what happens!")
    
    # Load animations
    lottie_heart = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_i4m5ctvd.json")
    # lottie_ninja1 = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_1pxqjqps.json")
    path1 = "./Animation - 1739549279665.json"
    with open(path1, "r") as file:
        lottie_ninja1 = json.load(file)
    # lottie_ninja1 = json.load("./Animation - 1739549279665.json")
    lottie_ninja2 = load_lottie_url("https://assets3.lottiefiles.com/private_files/lf30_2sc4cgsd.json")
    lottie_ninja3 = load_lottie_url("https://assets2.lottiefiles.com/private_files/lf30_lj6kjpv4.json")
    lottie_ninja4 = load_lottie_url("https://assets4.lottiefiles.com/private_files/lf30_wvyein4w.json")
    lottie_ninja5 = load_lottie_url("https://assets5.lottiefiles.com/private_files/lf30_xyz123.json")
    lottie_ninja6 = load_lottie_url("https://assets6.lottiefiles.com/private_files/lf30_abc456.json")
    
    if lottie_heart:
        st_lottie(lottie_heart, speed=1, width=200, height=200)
    
    # Define scenarios and options
    scenarios = [
        {"question": "You're on a secret ninja mission, but I forgot to pack the kunai. What do you do?",
         "options": ["Laugh it off and improvise with shurikens", "Get a little annoyed but use hand-to-hand combat", "Panic and start searching for replacements", "Say 'I told you so' but still fight alongside me"],
         "responses": ["You're always quick to adapt! 🌀", "True shinobi spirit! 🔥", "A bit chaotic, but I love your determination! 💪", "Haha, you know me too well! ❤️"],
         "animation": lottie_ninja1},
        {"question": "I made you a special ninja ramen, but it's slightly overcooked. Your reaction?",
         "options": ["Eat it with a big smile and say it's delicious!", "Laugh and suggest we order Ichiraku Ramen instead", "Tease me about my cooking skills but still eat it", "Pretend to enjoy it but secretly give it to Pakkun"],
         "responses": ["You're the best! 🍜❤️", "Great idea! Ichiraku Ramen it is! 🍜", "Hey, at least I tried! 😆", "Poor Pakkun! 😂"],
         "animation": lottie_ninja2},
        {"question": "We are training together, but I keep messing up my jutsu. How do you react?",
         "options": ["Encourage me and tell me I'll get it next time", "Laugh and say I should stick to taijutsu", "Challenge me to a friendly duel to improve", "Teach me step by step with patience"],
         "responses": ["Your support means everything! ❤️", "Haha! Maybe you're right! 🌀", "A duel? You’re on! 💥", "You're the best teacher! 😊"],
         "animation": lottie_ninja3},
        {"question": "A rival ninja challenges us to a fight! What do you do?",
         "options": ["Take them on together as a team", "Let me handle it while you watch", "Try to talk them down peacefully", "Set a trap and outsmart them"],
         "responses": ["Teamwork always wins! 💪", "I'll cheer for you! 😊", "Diplomacy is wise! 🧠", "Brilliant strategy! 🌀"],
         "animation": lottie_ninja4},
        {"question": "We find a mysterious scroll in the forest. What do you do?",
         "options": ["Open it immediately", "Take it to the village elders", "Bury it—it could be dangerous", "Use a sealing jutsu on it"],
         "responses": ["Curiosity is a ninja's strength! 🔍", "Smart move! Wisdom is key! 📜", "Better safe than sorry! 🛡️", "Clever thinking! 🌀"],
         "animation": lottie_ninja5},
        {"question": "A festival is happening in the village. What do you want to do first?",
         "options": ["Try all the food stands", "Watch the ninja performances", "Enter a friendly sparring match", "Enjoy a quiet moment under the fireworks"],
         "responses": ["Food lovers unite! 🍜", "Ninja skills on display! 🎭", "Show them your strength! 💪", "A perfect moment! 🎆"],
         "animation": lottie_ninja6}
    ]
    
    # Track score
    score = 0
    total_questions = len(scenarios)
    
    for idx, scenario in enumerate(scenarios):
        st.subheader(f"Scenario {idx + 1}")
        st.write(scenario["question"])
        
        if scenario["animation"]:
            st_lottie(scenario["animation"], speed=1, width=250, height=250)
        
        choice = st.radio(scenario["question"], scenario["options"], index=None, key=f"q{idx}")
        
        if choice:
            response_idx = scenario["options"].index(choice)
            st.success(scenario["responses"][response_idx])
            score += 1
    
    # Display final message
    if score == total_questions:
        st.balloons()
        st.success("Happy Valentine's Day, my ninja! ❤️ You're the strongest shinobi in my heart!")
    
if __name__ == "__main__":
    main()
