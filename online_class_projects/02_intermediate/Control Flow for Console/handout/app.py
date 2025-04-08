import random
import streamlit as st

NUM_ROUNDS = 5  
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #FF6347;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    .subheader {
        font-size: 2em;
        font-weight: bold;
        color: #3CB371;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
    }
    .score {
        font-size: 1.5em;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
    }
    .result {
        font-size: 1.7em;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }
    body {
        background-image: url('https://images.unsplash.com/photo-1590600895329-11e98c687ac0');
        background-size: cover;
        background-position: center;
    }
    .button {
        background-color: #FF6347;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.2em;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #FF4500;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="title">HIGH-LOW GAME</p>', unsafe_allow_html=True)
    st.write("WELCOME TO THE HIGH-LOW GAME! LET'S SEE IF YOU CAN GUESS CORRECTLY.")
    st.write("--------------------------------")

    score = 0  

 
    for round_num in range(1, NUM_ROUNDS + 1):
        st.markdown(f'<p class="subheader">ROUND {round_num}</p>', unsafe_allow_html=True)
        
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)

       
        st.write(f"YOUR NUMBER IS: **{player_number}**")

        
        guess = st.radio(
            f"DO YOU THINK YOUR NUMBER IS HIGHER OR LOWER THAN THE COMPUTER'S?",
            ('higher', 'lower'),
            key=f"guess_{round_num}"
        )

      
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            st.markdown(f'<p class="result">YOU WERE RIGHT! THE COMPUTER\'S NUMBER WAS **{computer_number}**.</p>', unsafe_allow_html=True)
            score += 1
        else:
            st.markdown(f'<p class="result">OOPS, YOU WERE WRONG. THE COMPUTER\'S NUMBER WAS **{computer_number}**.</p>', unsafe_allow_html=True)

        st.markdown(f'<p class="score">YOUR CURRENT SCORE IS: **{score}**</p>', unsafe_allow_html=True)

    
    st.write("\nTHANKS FOR PLAYING!")
    
   
    if score == NUM_ROUNDS:
        st.write("WOW! YOU PLAYED PERFECTLY!")
    elif score >= NUM_ROUNDS // 2:
        st.write("GOOD JOB, YOU PLAYED REALLY WELL!")
    else:
        st.write("BETTER LUCK NEXT TIME!")

if __name__ == "__main__":
    main()
