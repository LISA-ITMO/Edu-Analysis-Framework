from helpers.DocumentSplitter import DocumentSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
from langchain.prompts import load_prompt
from dotenv import load_dotenv
from os import getenv

# load enviroment variables
load_dotenv('config/giga.env')

class GigaModel:    
    def __init__(self, role=""):
        # configuration for the chatbot model
        self.credentials = getenv('AUTH_TOKEN')
        self.verify_ssl_certs = getenv('VERITY_SSL_CERTS')
        self.model = getenv('MODEL')
        self.role = role
        
        # define a role
        self.messages = [
            SystemMessage(content=role)
        ]
        
        # create an instance of our model
        self.chat = GigaChat(
            credentials=self.credentials, 
            verify_ssl_certs=self.verify_ssl_certs,
            model=self.model
        )
    
    
    # def summarize_file(self, file):
    #     documents = DocumentSplitter.split(file)
        
    #     map_prompt = load_prompt('lc://prompts/summarize/map_reduce/map.yaml')
    #     combine_prompt = load_prompt('lc://prompts/summarize/map_reduce/combine.yaml')
        
    #     chain = load_summarize_chain(
    #         self.chat,
    #         chain_type="map_reduce",
    #         map_prompt=map_prompt,
    #         combine_prompt=combine_prompt,
    #         verbose=False  
    #     )
        
    #     result = chain.invoke({ "input_documents": documents })
        
    #     return result['output_text'].replace('. ', '.\n')
    
    
    def send_message(self, content):
        """ Send message to model and display result """
        self.messages.append(HumanMessage(content))
        response = self.chat(self.messages)
        self.messages.append(response)
        return response.content

