import streamlit as st

def main():
    st.title("Google gemini app")
    input=st.text_input("Enter your question Here")
    
    if st.button("answer me:"):
        answer = "42"
    
    
if __name__=="__main__":
    main()