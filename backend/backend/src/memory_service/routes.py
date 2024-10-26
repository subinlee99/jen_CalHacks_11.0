from fastapi import APIRouter

from .memory import MemoryService
from fastapi import Request
router = APIRouter()

memory_router = APIRouter(prefix="/memory")


@memory_router.get("/all_memories")
async def get_all_memories(user_id: str):

    memory_service = MemoryService(user_id=user_id)

    memories = memory_service.get_all_memories()

    return {"memories": memories}


@memory_router.put("/{memory_id}")
async def update_memory(memory_id: str, updated_content: dict):
    memory_service = MemoryService()
    success = memory_service.update_memory(memory_id, updated_content)
    if success:
        return {"message": "Memory updated successfully"}
    else:
        return {"message": "Memory update failed"}, 400
        

@memory_router.post("/add_messages")
async def add_messages(request: Request):
    data = await request.json()
    messages = data["messages"]
    
    print("messages are ")
    print(messages)
    
    concatenated_messages = " ".join(messages)
    
    object = [
        {
            "role": "user",
            "content": concatenated_messages
        }
    ]
    
    user_id = "jenny"
    memory_service = MemoryService(user_id=user_id)
    memory_service.add_messages(object)
    return {"message": "Messages added successfully"}


@memory_router.delete("/{memory_id}")
async def delete_memory(memory_id: str):
    memory_service = MemoryService()
    success = memory_service.delete_memory(memory_id)
    if success:
        return {"message": "Memory deleted successfully"}
    else:
        return {"message": "Memory deletion failed"}, 400


@memory_router.get("/load-jenny")
async def test_run():

    memory_service = MemoryService(user_id="jenny")
    messages = [
        {
            "role": "user",
            "content": "Hi, I'm Jennyy. I'm a vegetarian and I'm allergic to nuts and I'm 79 years old. I love singing, Im a retired. My health nsurance provider is Blue Shield, and I have a Medicare Supplement Plan. i stay at 426 27th avenue, i have diabetes and i prefer to go to the doctor that is walking distance from me.",
        }
    ]

    memory_service.add_messages(messages)

    memories = memory_service.get_all_memories()

    return {"memories": memories}

@memory_router.get("/test-all")
async def test_all():

    memories = MemoryService._get_all_memories_by_user_id("jenny")

    return {"memories": memories}


@memory_router.get("/search_memories")
async def search_memories(id):
    return {"message": "Memory search successful"}


@memory_router.post("/add")
async def add_memory():
    return {"message": "Memory added successfully"}
