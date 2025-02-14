import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.title("❤️ Valentine's Day Scenario Game ❤️")
    st.write("Welcome to your special Valentine's Day game! Answer these fun scenarios and see what happens!")
    
    # Load animations
    lottie_heart = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_i4m5ctvd.json")
    lottie_character1 = load_lottie_url("https://assets9.lottiefiles.com/private_files/lf30_touohxvc.json")
    lottie_character2 = load_lottie_url("https://assets9.lottiefiles.com/private_files/lf30_jcikwtux.json")
    
    if lottie_heart:
        st_lottie(lottie_heart, speed=1, width=200, height=200)
    
    # Define scenarios and options
    scenarios = [
        {
            "question": "You're on a dream vacation, but I forgot to book the hotel. What do you do?",
            "options": [
                "Laugh it off and find an adventure",
                "Get a little annoyed but help figure it out",
                "Panic and start searching for the nearest hotel",
                "Say 'I told you so' but still love me anyway"
            ],
            "responses": [
                "You're always up for an adventure! Love that about you! 😍",
                "Teamwork makes the dream work! We got this! 💕",
                "Crisis mode activated! But I appreciate your quick thinking! 🤓",
                "You know me too well! 😂 Love you anyway! ❤️"
            ],
            "animation": lottie_character1
        },
        {
            "question": "I surprise you with a home-cooked meal, but it's slightly burnt. Your reaction?",
            "options": [
                "Eat it with a big smile and say it's delicious!",
                "Laugh and suggest we order takeout instead",
                "Tease me about my cooking skills but still eat it",
                "Pretend to enjoy it but secretly feed it to the dog"
            ],
            "responses": [
                "You're the sweetest! My cooking may be questionable, but your love isn't! ❤️",
                "Good call! Pizza, anyone? 🍕",
                "Hey, at least I tried! Points for effort? 😆",
                "Poor dog! Guess I better work on my cooking skills! 😂"
            ],
            "animation": lottie_character2
        }
    ]
    
    # Track score
    score = 0
    total_questions = len(scenarios)
    
    for idx, scenario in enumerate(scenarios):
        st.subheader(f"Scenario {idx + 1}")
        st.markdown(
            """
            <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .fade-in {
                animation: fadeIn 2s ease-in;
            }
            </style>
            <div class="fade-in">""" + scenario["question"] + """</div>
            """,
            unsafe_allow_html=True
        )
        
        # Display character animation
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
        st.success("Happy Valentine's Day, my love! ❤️ You're the best!")
    
if __name__ == "__main__":
    main()
