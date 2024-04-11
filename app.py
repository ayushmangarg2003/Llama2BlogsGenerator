import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers

# Generation Function Defined
def getLlamaResponse(input_text,no_words,blog_style):
   llm = CTransformers(model='model\llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',config={
     'max_new_tokens':256,
     'temperature':0.01
    })
   template = "Write a Blog for {blog_style} job profile for a topic {input_text} within {no_words} words."
   prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)
   st.write(prompt)
   st.write(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words ))
   response = llm("Hello")
   # response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words ))
   st.write(response)
   return response

# getLlamaResponse("WEB3.0",100,"Student")

# Website
st.set_page_config(page_title='Ayushman Blogs',
                   page_icon='@',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Ayushman Blogs @")

input_text = st.text_input("Enter The Blog Title")

col1,col2 = st.columns([5,5])

with col1:
   no_words = st.text_input('No of Words')
with col2:
   blog_style = st.selectbox('Writing a blog for',('Researcher','Data Scientist','Common People'), index=0)

submit = st.button('Generate')

if submit:
   st.write("Started")
   st.write(getLlamaResponse(input_text,no_words,blog_style))
   st.write("Ended")
