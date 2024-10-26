
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI



load_dotenv()
PRINT_LOGS = False#os.getenv("PRINT_LOGS", default=False)

# MODEL = "llama-3-sonar-small-32k-online" 
MODEL = "llama-3.1-sonar-large-128k-online"
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", default=None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", default=None)

class DoctorInfo(BaseModel):
    name: str = Field(..., description="Name of the doctor")
    address: str = Field(..., description="Address of the doctor")
    phone_number: int = Field(..., description="Phone number of the doctor")
    associated_hospital: str | None = Field(None, description="Name of the hospital the doctor is associated with")

class DoctorInfoList(BaseModel):
    doctors: list[DoctorInfo] = Field(..., description="List of doctors")

class PerplexityService:
    def __init__(self):
        if not PERPLEXITY_API_KEY:
            raise ValueError("PERPLEXITY_API_KEY environment variable is not set")
        try:
            self.perplexity = ChatPerplexity(temperature=0, model=MODEL, api_key=PERPLEXITY_API_KEY)
        except Exception as e:
            raise ValueError(f"Error while initializing PerplexityWrapper: {e}")
        
    

    def search_perplexity(self, query):
        system = "You are a helpful web searching assistant. Make sure to give precise, accurate and structured responses which are real, not fake. For example if you have been asked for a list of doctors, provide the names, addresses, phone numbers, etc. of the doctors."
        human = "{input}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        chain = prompt | self.perplexity
        response = chain.invoke({"input": query})
        # return response.content

        # Extract the text content from the response
        response_text = response.content if hasattr(response, 'content') else str(response)

        print("Perplexity answer:", response_text)
    
        
        model = ChatOpenAI(temperature=0, api_key=OPENAI_API_KEY)
        # And a query intented to prompt a language model to populate the data structure.
        parser_query = f"Take the following list regarding doctors and provide the names, addresses, phone numbers, and associated hospitals of the doctors in a structured format. \n{response_text}"

        # Set up a parser + inject instructions into the prompt template.
        parser = JsonOutputParser(pydantic_object=DoctorInfoList)

        prompt = PromptTemplate(
            template="Answer the user query.\n{format_instructions}\n{query}\n",
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | model | parser
        
        parsed_response = chain.invoke({"query": parser_query})

        return parsed_response
    

    def search_perplexity_events(self, query):
        system = "You are a helpful web searching assistant. I need to search real events happening around me which I am interested in."
        human = "{input}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

        chain = prompt | self.perplexity
        response = chain.invoke({"input": query})
        # return response.content

        # Extract the text content from the response
        response_text = response.content if hasattr(response, 'content') else str(response)

        print("Perplexity answer:", response_text)

        return response_text

