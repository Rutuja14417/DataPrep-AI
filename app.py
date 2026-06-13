import streamlit as st
import time

# Page setup for a clean user interface
st.set_page_config(page_title="DataPrep AI", page_icon="🤖", layout="centered")

st.title("🤖 DataPrep AI: Data Science Interview Bot")
st.write("Welcome! Let's test and sharpen your AI, Machine Learning, and Data Science knowledge.")

# Sidebar for configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password", value="AIzaSyFakeKey_ForDemoPurposes Only")

# Initialize session memory for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your technical recruiter today. Let's begin your practice session. First question: Can you explain the difference between supervised and unsupervised learning?"}
    ]
    st.session_state.step = 1

# Render previous conversation blocks nicely
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle incoming user responses
if user_reply := st.chat_input("Type your answer here..."):
    # Append user message to display
    st.session_state.messages.append({"role": "user", "content": user_reply})
    with st.chat_message("user"):
        st.write(user_reply)
        
    # Simulate realistic AI analysis spinner
    with st.spinner("Analyzing your response..."):
        time.sleep(2)  # Simulates network lag for the video
        
        # Smart dynamic response matching based on what step of the interview we are on
        if st.session_state.step == 1:
            ai_response = (
                "**Evaluation Score: 9.5/10**\n\n"
                "Excellent answer! You correctly identified that supervised learning relies on labeled data and clear outcomes "
                "(like regression and classification), while unsupervised learning discovers underlying structures or groupings "
                "in unlabeled data (like clustering).\n\n"
                "Let's move to the next question: **Can you explain what overfitting is in a machine learning model, and name one way to prevent it?**"
            )
            st.session_state.step = 2
        else:
            ai_response = (
                "**Evaluation Score: 9.0/10**\n\n"
                "Spot on! Overfitting happens when a model learns the training data noise too well, failing to generalize to new data. "
                "Using techniques like regularization or cross-validation is a perfect way to mitigate it.\n\n"
                "Great job completing this evaluation round! Your technical conceptual foundations are incredibly strong."
            )
            
    # Append and render assistant feedback
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.rerun()