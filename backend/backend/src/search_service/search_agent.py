import os
from dotenv import load_dotenv
load_dotenv("backend/.env.local")
from src.search_service.perplexity_service import PerplexityService
from src.search_service.groq_service import GroqService
from pprint import pprint

PRINT_LOGS = False #int(os.getenv("PRINT_LOGS", default=False))


class SearchAgent:
    def __init__(self):
        self.groq_service = GroqService()
        self.perplexity_service = PerplexityService()


    def __search_query_formatter(self, user_query_string, user_context_dict):
        PRINT_LOGS and print(f"SearchAgent: __search_query_formatter inputs: user_query_string: {user_query_string} | user_context_dict: {user_context_dict}")

        """
        Uses an LLM to generate a Perplexity search query based on the user's query and context.
        
        :param user_query: The user's query string.
        :param user_context: Dictionary containing demographic, preferences, and context.
        :return: A string prompt ready to be sent to Perplexity.
        """
        prompt_template = f"""
        Here is the context of a particular user: {user_context_dict} 
        and what the user has asked from me: {user_query_string}. 
        Before I directly address the query, I want to do some research using Perplexity/web search to give the user options on what they want to do. 
        Make sure to phrase the query such that I get the most relevant results and to include as much relevant context as you can.
        Given this, can you help me prepare a search query for Perplexity?

        For examples on what kind of inputs and outputs are expected, see below:

        Example user_query_string: "find doctor."
        Example user_context_dict: {{
            "age": 45,
            "gender": "female",
            "medical_history": "diabetes",
            "location": "Richmond District, San Francisco",
            "travel_preferences": "walking distance",
            "timing_preferences": "this week"
        }}
        
        Example response: "Find nearby doctors (their names, address, phone number etc.) specializing in gastroenterology in Richmond District, San Francisco, that accept patients with diabetes, available this week, within walking distance from Richmond District, San Francisco, who can see patients with stomach pain and a medical history of diabetes, and can provide immediate appointments this week."

        NOTE: Your output should just be ONE query. Dont have "Based on the user's context and query, here's a search query that can be sent to Perplexity:" or anything like that. Just the query.
        """

        # Call to LLM (replace with your LLM model of choice)
        response = self.groq_service.get_groq_response(prompt_template)

        PRINT_LOGS and print(f"SearchAgent: __search_query_formatter: response: {response}")

        return response

    def search(self, user_query_string, user_context_dict):
        PRINT_LOGS and print(f"SearchAgent: search inputs: user_query_string: {user_query_string} | user_context_dict: {user_context_dict}")

        search_query = self.__search_query_formatter(user_query_string, user_context_dict)

        search_query += " Make sure to provide details such as names, addresses, phone numbers etc. If the person doesn't have a phone number but instead I have to contact the organization, explicitly state the organization's phone number as the person's phone number. Repeat information if needed."

        print(f"search_query: {search_query}")

        return self.perplexity_service.search_perplexity(search_query)


    def searchAboutTopic(self, topic):
        search_query = f"I am very interested in {topic}. Can you find any cool locations or events which I can attend? I live in Richmond District, San Francisco!"

        response = self.perplexity_service.search_perplexity_events(search_query)

        print(f"searchAboutTopic response: {response}")

        return response

# def main():
#     search_agent = SearchAgent()
#     user_query_string = "I have been experiencing back pain and need to see a doctor soon."
#     user_context_dict = {
#             "age": 69,
#             "gender": "female",
#             "medical_history": "diabetes",
#             "location": "Richmond District, San Francisco",
#             "travel_preferences": "walking distance",
#             "timing_preferences": "this week"
#         }
    
#     pprint(search_agent.search(user_query_string, user_context_dict))

    

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     from uagents import Agent, Context, Protocol, Model
#     from ai_engine import UAgentResponse, UAgentResponseType
#     import requests
#     from typing import Dict

#     from backend.src.search_service.search_agent import SearchAgent

#     SEED_PHRASE = "search_agent"
#     AGENT_MAILBOX_KEY = "48092180-959d-4487-ad82-68369b118143"

#     class SearcAgentResponse(Model):
#         search_string: str
#         user_dict: Dict = {}

#     searchAgent = Agent(
#         name="SearchAgent", #or any name
#         seed=SEED_PHRASE,
#         mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
#     )
#     content_protocol = Protocol("Search Agent Protocol")
#     print(searchAgent.address)

#     def get_doctor_list(search_string, user_dict):
#         search1agent = SearchAgent()
#         response = search1agent.search(search_string, user_dict)
#         return response

#     @content_protocol.on_message(model=SearcAgentResponse, replies={UAgentResponse})
#     async def sentiment(ctx: Context, sender: str, msg: SearcAgentResponse):
    
#         doctor_list = get_doctor_list(msg.search_string, msg.user_dict)
#         print(msg.search_string, msg.user_dict)
#         print(type(doctor_list))
#         await ctx.send(
#             sender, UAgentResponse(message=str(doctor_list), type=UAgentResponseType.FINAL)
#         )

#     searchAgent.include(content_protocol, publish_manifest=True)
#     searchAgent.run()
