from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.utilities import SerpAPIWrapper
import streamlit as st

class ChatHandler:
    def __init__(self):
        self.DEFAULT_TEMPLATE = """You are a Career advisor and the following is a friendly conversation between a human and an You. The Advisor guides the user regarding skills,interests and other domain selection decisions. 
       you follow these steps to answer a user question -
        
        process the current user query, relate it to previous context history, you check for user query to find contexts for words like "this", "it", "that", "these", etc.  and respond accordingly.
       
        if query is not a career guidance query then you politely responds with no with some interactive message, and use previous context to suggest user for other questions.
        
    If the processed query is related to guidance or matches with previous history context, then you follow the previous conversation if applicable. You takes inspiration from career guidance books text which is provided to it and then you make the response in way it guides the user while giving important information, regarding user query.
     The responses should be detailed, explaine each points.
       
        Below is information for your response -

        Relevant pieces of previous conversation:
        {context},

        Useful information from career guidance books:
        {text}, 

        Useful information about career guidance from Web:
        {web_knowledge},

        Current user query:
        {input}
        """
        
        self.PROMPT = PromptTemplate(
            input_variables=['context','input','text','web_knowledge'], 
            template=self.DEFAULT_TEMPLATE
        )
        
    def get_response(self, history, user_message, temperature=1):
        docs = st.session_state["vectors"].similarity_search(user_message)
        
        params = {
            "engine": "bing",
            "gl": "us",
            "hl": "en",
        }
        
        search = SerpAPIWrapper(params=params)
        web_knowledge = search.run(user_message)
        # claude_model = ChatAnthropic(model_name='claude-3-5-sonnet-20240620')
        
        gemini_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=temperature)
        conversation_with_summary = LLMChain(
            llm=gemini_model,
            prompt=self.PROMPT,
            verbose=False
        )
        print("\n")
        print("history:" )
        print(history)
        print("\n")
        print("\n")
        print("user input: ")
        print(user_message)
        print("\n")
        print("\n")
        print("Web knowledge: ")
        print(web_knowledge)
        print("\n")
        print("\n")
        print("doc text: ")
        print(docs)
        print("\n")
        response = conversation_with_summary.predict(
            context=history,
            input=user_message,
            web_knowledge=web_knowledge,
            text=docs
        )
        print(response)
        return response
    
    @staticmethod
    def get_history(history_list):
        history = ''
        for message in history_list:
            if message['role'] == 'user':
                history = history + 'user:  ' + message['content'] + '\n'
            elif message['role'] == 'assistant':
                history = history + 'you:  ' + message['content'] + '\n'
        return history