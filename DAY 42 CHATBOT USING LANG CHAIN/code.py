from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

load_dotenv()

model  = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite-preview')


chat_history = [
    SystemMessage(content='I am Your AI Assistant')
]

while True:
    user_input = input('You :  ')

    chat_history.append(HumanMessage(content=user_input))

    if user_input == 'exit':
        break

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content= result.text))

    print("AI : "  , result.text)


print(chat_history)