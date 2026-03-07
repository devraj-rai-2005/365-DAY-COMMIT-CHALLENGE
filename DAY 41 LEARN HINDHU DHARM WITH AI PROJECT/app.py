# Making a Streamlit FrontEnd 

import streamlit as st
from langchain_core.prompts import load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

st.title("🕉 Learn Hindu Dharma with AI")

st.write("Explore the wisdom of Hindu scriptures through stories and teachings.")

# 1 Deity Selection
deity_name = st.selectbox(
    "Select a Deity or Character",
    [
        "Lord Krishna",
        "Lord Rama",
        "Lord Shiva",
        "Goddess Durga",
        "Goddess Lakshmi",
        "Goddess Saraswati",
        "Lord Hanuman",
        "Lord Ganesha",
        "Arjuna",
        "Bhishma",
        "Karna",
        "Prahlada"
    ]
)

# 2 Scripture Source
scripture_source = st.selectbox(
    "Select the Scripture Source",
    [
        "Bhagavad Gita",
        "Ramayana",
        "Mahabharata",
        "Shiva Purana",
        "Vishnu Purana",
        "Bhagavata Purana",
        "Vedas",
        "Upanishads"
    ]
)

# 3 Topic
topic = st.selectbox(
    "Select the Topic",
    [
        "Dharma (Righteous Duty)",
        "Karma Yoga",
        "Bhakti (Devotion)",
        "Courage and Bravery",
        "Devotion to God",
        "Importance of Truth",
        "Good vs Evil",
        "Power of Faith",
        "Detachment from Results",
        "Leadership and Responsibility"
    ]
)

# 4 Audience
audience_type = st.selectbox(
    "Select Target Audience",
    [
        "Kids",
        "Beginners",
        "Students",
        "Teenagers",
        "Spiritual Seekers",
        "General Audience"
    ]
)

# 5 Style
language_style = st.selectbox(
    "Select Explanation Style",
    [
        "Simple Explanation",
        "Storytelling Style",
        "Motivational Style",
        "Spiritual Teaching",
        "Teacher Style"
    ]
)

# 6 Dharma Lesson
moral_focus = st.selectbox(
    "Select Dharma Lesson to Emphasize",
    [
        "Importance of Duty",
        "Power of Devotion",
        "Courage in Difficult Times",
        "Self Discipline",
        "Truth and Honesty",
        "Faith in God",
        "Importance of Righteous Action",
        "Overcoming Ego"
    ]
)


# Importing A Model 

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite-preview')

prompt = load_prompt('TEMPLATE/tempalate.json')

chain = prompt  | model


# Button
if st.button("Generate Teaching"):

    response = chain.invoke({
        'deity_name' : deity_name, 
        'scripture_source' :  scripture_source , 
        'topic' :  topic  , 
        'audience_type' :  audience_type , 
        'language_style' : language_style , 
        'moral_focus' : moral_focus
    })

    st.write(response.text)