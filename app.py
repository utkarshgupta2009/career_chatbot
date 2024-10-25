from config import setup_streamlit
from database import DocumentDatabase
from chat_handler import ChatHandler
from itertools import zip_longest
import streamlit as st
import time

def display_sample_questions():
    st.markdown("### Sample Questions to Get Started:")
    questions = [
        "What career paths are suitable for someone with a Computer Science degree?",
        "What skills should I develop for a career in Data Science?",
        "How can I prepare for a job interview in Software Engineering?",
        "What are the growing career fields in Technology?",
        "How do I write an effective resume for tech jobs?"
    ]
    
    for question in questions:
        if st.button(question, key=f"sample_{question}"):
            return question
    return None

def display_chat_history():
    for i in range(len(st.session_state["generated"])):
        user_message = st.chat_message("user")
        assistant_message = st.chat_message("assistant")
        user_message.write(st.session_state['past'][i])
        assistant_message.write(st.session_state['generated'][i])

def main():
    # Initialize Streamlit
    setup_streamlit()
    
    # Initialize database
    pdf_dir = 'D:/New Work/career-advisor-chatbot/pdf'
    db = DocumentDatabase(pdf_dir)
    db.initialize_database()
    
    # Initialize chat handler
    chat_handler = ChatHandler()
    
    # Initialize session state
    if "past" not in st.session_state:
        st.session_state["past"] = []
    if "generated" not in st.session_state:
        st.session_state["generated"] = []
    if "first_visit" not in st.session_state:
        st.session_state["first_visit"] = True
    if "thinking" not in st.session_state:
        st.session_state["thinking"] = False

    # Display existing chat history
    display_chat_history()
    def submit():
        st.session_state["first_visit"] = False

    # If thinking, show the last user message and thinking indicator
    if st.session_state.thinking:
        user_message = st.chat_message("user")
        user_message.write(st.session_state.past[-1])
        
        assistant_message = st.chat_message("assistant")
        with assistant_message:
            with st.empty():
                st.write("Thinking...")
    
    # Welcome message and sample questions on first visit
    if st.session_state["first_visit"] and not st.session_state["generated"]:
        st.markdown("""
        I'm here to help you with career guidance and professional development.
        Feel free to ask me anything or try one of the sample questions below.
        """)
        selected_question = display_sample_questions()
        if selected_question:
            st.session_state["first_visit"] = False
            user_input = selected_question
        else:
            user_input = st.chat_input(placeholder="Enter your question here", key="input",on_submit=submit)
    else:
        user_input = st.chat_input(placeholder="Enter your question here", key="input")

    if user_input:
        # Add user input to history
        st.session_state.past.append(user_input)
        # Set thinking state to True
        st.session_state.thinking = True
        # Rerun to show thinking state
        st.rerun()

    # If we're in thinking state, generate response
    if st.session_state.thinking:
        user_history = list(st.session_state["past"])
        bot_history = list(st.session_state["generated"])
        
        combined_history = []
        for user_msg, bot_msg in zip_longest(user_history[:-1], bot_history):
            if user_msg is not None:
                combined_history.append({'role': 'user', 'content': user_msg})
            if bot_msg is not None:
                combined_history.append({'role': 'assistant', 'content': bot_msg})
        
        # Add the latest user message
        combined_history.append({'role': 'user', 'content': user_history[-1]})
        
        formatted_history = chat_handler.get_history(combined_history)
        output = chat_handler.get_response(formatted_history, user_history[-1])
        
        # Add response to generated history
        st.session_state.generated.append(output)
        # Reset thinking state
        st.session_state.thinking = False
        # Rerun to show final state
        st.rerun()

if __name__ == "__main__":
    main()