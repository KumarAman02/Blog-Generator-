import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from LLAMA2 model

def get_llama_response(input_text, no_of_words, blog_style):

    # LLAMA2 Model
    llm = CTransformers(model="F:/Blog Generation App/models/llama-2-7b.ggmlv3.q8_0.bin", model_type="llama", config={"max_new_tokens":256,"temperature":0.05})

    # Prompt Template
    template = """Write a blog for {blog_style} job profile for a topic {input_text} within {no_of_words}"""

    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_of_words"], template=template)

    # Generate the response from LLAMA2 model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_of_words=no_of_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs", page_icon="", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text = st.text_input("Enter the blog topic")

# Creating two more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1:
    no_of_words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox("Writing the blog for",("Researchers","Data Scientist", "Common People"),index=0)

submit = st.button("Generate")

# Final Response
if submit:
    st.write(get_llama_response(input_text, no_of_words, blog_style))