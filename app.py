import streamlit as st

def main():
    st.title("Hello! I'm your chatbot 🤖")
    st.write("Type something and let's chat!")
    
    user_input = st.text_input("You:", "")
    if user_input:
        st.write(f"Bot: You said '{user_input}'")

if __name__ == "__main__":
    main()
