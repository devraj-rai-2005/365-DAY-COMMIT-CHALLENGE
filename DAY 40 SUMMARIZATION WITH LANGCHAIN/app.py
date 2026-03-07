import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

chat_gemini_model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite-preview' , temperature =0)


# Making a Streamlit Application

st.header('RESEARCH TOOL')


paper_input = st.selectbox('Note :- Select the reserch paper name' , ["Attention All you Need" , "Bert: Pre-training of Deep Bidirectional Transformer" , "GPT-3 Language Model are few Shot Learners" , "diffusion Models Beat GAN's on Image Synthesis"])


style_input = st.selectbox('Note :- Select Explanation Style :' , ["Beginner-Frinedly" , "Technicall" ,"Code-Oriented" , "Mathematical"])


length_input = st.selectbox('Note :- Select the Explanation' , ["Short (1-2 paragrahs)" , "Medium (3-5 paragraph)" , "Long(detailed Explanation)"])


template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables= ['paper_input' , 'style_input' ,'length_input'  ]
)

prompt = template.invoke({
    'paper_input' :paper_input ,
    'style_input' : style_input ,
    'length_input' :length_input
})


if st.button('summarize'):

    response = chat_gemini_model.invoke(prompt)

    st.write(response.text)