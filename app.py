import streamlit as st


#necessary library
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def main():
    st.title("Google gemini app")
    input=st.text_input("Enter your question Here")
    
    if st.button("answer me:"):
        answer = "42"
    
    
if __name__=="__main__":
    main()