import openai
import os
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate

# Access the API key from the environment
#api_key = os.getenv('OPENAI_API_KEY')

# Set the API key for the openai library (using the environment variable)
#openai.api_key = api_key

#langchain_key = os.getenv("LANCHAIN_API_KEY_NKP")


class AIEmergencyCare:
    def __init__(self):
        model = ChatOpenAI()
    def get_response(self,usr_input):
        prompt = ChatPromptTemplate(
            messages= [SystemMessagePromptTemplate.from_template("4V Medical Emergency Care."),HumanMessagePromptTemplate.from_template(usr_input),]
        )
        response = self.model.generate_response(prompt)
        return response.content
    def aiChat(self):
        print("4V AI Emergency Care: How can I help you?")
        while True:
            usr_input = input("You:")
            if usr_input.lower() in ["exit","quit","bye"]:
                break
            response = self.get_response(usr_input)
            print(f'4V Medical Emergency Care:{response}')

if __name__  ==  "__main__":
    aichatbot = AIEmergencyCare()
    aichatbot.aiChat()