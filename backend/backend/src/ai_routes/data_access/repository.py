from fastapi import APIRouter, Request

from ...app import server
from openai import OpenAI

router = APIRouter(prefix="/ai", tags=["ai"])

client = OpenAI()

def extract_filters_from_text(user_input: str):
    functions = [
        {
            "name": "extract_filters",
            "description": "Extracts price filters from user input",
            "parameters": {
                "type": "object",
                "properties": {
                    "price_max": {"type": "number", "description": "Maximum price"},
                    "price_min": {"type": "number", "description": "Minimum price"},
                },
                "required": ["price_max"]
            },
        }
    ]
    
    response = client.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "user", "content": user_input}
        ],
        functions=functions,
        function_call="auto",
    )
    
    function_args = response['choices'][0]['message']['function_call']['arguments']
    return eval(function_args)  # Convert string to dict

def generate_embedding(text):

    model = "text-embedding-ada-002"

    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding
@router.post("/")
async def get_ai_data(request: Request):
    user_input = await request.json()
    print(user_input)
    supabase = server.get_supabase_client()

    query = supabase.table("vendors").select("name, about_vendor, price")
    
    # filters = extract_filters_from_text(user_input)
    
    embedding = generate_embedding(user_input)

    query = query.filter("embeddings", "similarity", embedding).limit(3)
    
    response = query.execute()
    print(response)
    # response = (
        # supabase.table("vendors")
        # .select("name, about_vendor")
        #.eq("name", "One in a Million Films")
        # .execute()
    # )

    return {"message": "Hello World"}
