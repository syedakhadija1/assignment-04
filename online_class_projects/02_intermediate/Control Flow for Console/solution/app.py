import random
import streamlit as st
import time

NUM_ROUNDS = 5


def display_header():
    st.title("🎲 High-Low Game 🎲")
    st.markdown("""
        Welcome to the **High-Low Game**!  
        In this game, you’ll try to guess if your number is higher or lower than the computer’s number.
        You have **5 rounds** to test your luck. Let's see how well you can play!
    """)
    st.write('--------------------------------')


def display_end_message():
    if st.session_state.score == NUM_ROUNDS:
        st.markdown("### 🎉 Congratulations! 🎉")
        st.write("You played perfectly! You guessed all rounds correctly.")
    elif st.session_state.score >= NUM_ROUNDS // 2:
        st.markdown("### 👍 Great Job! 👍")
        st.write("You did really well! Keep up the good work!")
    else:
        st.markdown("### 😢 Better Luck Next Time! 😢")
        st.write("Don't worry, you'll get better with more practice!")


def play_game():

    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'round' not in st.session_state:
        st.session_state.round = 1

  
    if st.session_state.round <= NUM_ROUNDS:
        round_num = st.session_state.round
        st.subheader(f"Round {round_num}")
        
       
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)

        st.markdown(f"**Your number**: {your_num}")
        
        
        prompt = random.choice(["higher", "lower"])
        choice = st.radio(
            f"Do you think your number is **{prompt}** than the computer's number?",
            ('higher', 'lower'),
            key=f"choice_{round_num}"
        )

        
        if st.button("Submit Guess"):
            st.spinner("Evaluating your guess... Please wait.")
            time.sleep(1)

            
            higher_and_correct = choice == "higher" and your_num > computer_num
            lower_and_correct = choice == "lower" and your_num < computer_num

            if higher_and_correct or lower_and_correct:
                st.success(f"✅ You were right! The computer's number was **{computer_num}**")
                st.session_state.score += 1
            else:
                st.error(f"❌ Oops! That's incorrect. The computer's number was **{computer_num}**")

       
            st.session_state.round += 1
            st.markdown(f"### Your score is now: **{st.session_state.score}**")

    else:
        
        display_end_message()

       
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.round = 1
            st.experimental_rerun()


def main():
    display_header()
    play_game()

if __name__ == "__main__":
    main()
