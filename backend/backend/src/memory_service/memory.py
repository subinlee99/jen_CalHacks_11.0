import os

from mem0 import MemoryClient

import time

class MemoryService:
    def __init__(self, user_id =None, categories = None):
        print(f"API Key: {os.getenv('MEM0AI_API_KEY')}")
        self.client = MemoryClient(api_key=os.getenv("MEM0AI_API_KEY"))
        self.user_id = user_id
        self.categories = categories

    def add_messages(self, messages):
        self.client.add(messages, user_id=self.user_id, categories=self.categories)
    
    @staticmethod    
    def _get_all_memories_by_user_id(user_id):
        client = MemoryClient(api_key=os.getenv("MEM0AI_API_KEY"))
        return client.get_all(user_id=user_id)

    def search_memory(self, query):
        return self.client.search(query, user_id=self.user_id)

    # TODO: This is not working
    def update_memory(self, memory_id, updated_content):
        print(f"API Key: {os.getenv('MEM0AI_API_KEY')}")
        print(f"Updating memory with ID: {memory_id}")
        return self.client.update(memory_id, updated_content)

    def delete_memory(self, memory_id):
        return self.client.delete(memory_id)

    def get_all_memories(self):

        def has_categories(memory):
            if "categories" not in memory or memory["categories"] is None:
                print("Memory does not have categories")
                return False

            if len(memory["categories"]) > 0:
                return True
            return False
        
        memories = self.client.get_all(user_id=self.user_id)
        
        # If less than half of the memories have categories, get all memories, for some reason the memories are not categorized on first call
        max_iterations = 5
        iteration_count = 0
        while any(not has_categories(memory) for memory in memories):
            if iteration_count >= max_iterations:  # Check if the maximum number of iterations is reached
                raise TimeoutError("Operation exceeded maximum iterations of 5")
            print("Getting all memories because less than half of the memories have categories")
            memories = self.client.get_all(user_id=self.user_id)
            time.sleep(3)
            iteration_count += 1  # Increment the iteration counter 
                
        return memories



# EXAMPLE USAGE
# memory_service = MemoryService(user_id="alex")

# messages = [
#     {
#         "role": "user",
#         "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts.",
#     },
#     {
#         "role": "assistant",
#         "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions.",
#     },
# ]
# memory_service.add_messages(messages)

# query = "What can I cook for dinner tonight?"
# memory_service.search_memory(query)

# user_memories = memory_service.get_all_memories()
