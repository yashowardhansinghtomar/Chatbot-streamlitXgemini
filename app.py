import streamlit as st
import google.generativeai as genai

def main():
    st.title("Simple Chatbot")
    
    # User input
    user_input = st.text_input("Type your message here:")
    
    # Button to submit the message
    submit_button = st.button("Send")
    
    # Placeholder for the chat history
    chat_history = st.empty()
    
    # Function to display the chat history
    def display_chat_history(user_input):
        # Configure the generative model
        genai.configure(api_key="Your_API_Key")
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate a response using the user's input as the prompt
        chatbot_response = generate(user_input)
        
        chat_history.text(f"User: {user_input}")
        chat_history.text(f"Chatbot: {chatbot_response}")
    
    # Function to generate content using the Gemini API
    def generate(prompt):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    
    # Check if the submit button is clicked
    if submit_button:
        display_chat_history(user_input)

if __name__ == "__main__":
    main()
    

# streamlit run app.py
