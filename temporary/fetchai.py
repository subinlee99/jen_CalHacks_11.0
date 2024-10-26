import asyncio
import logging
import os
import sys
from time import sleep
import json
from ai_engine_sdk import (
    AiEngine,
    is_agent_message,
    is_ai_engine_message,
    is_confirmation_message,
    is_stop_message,
    is_task_selection_message, TaskSelectionMessage
)
from ai_engine_sdk import ApiBaseMessage, FunctionGroup
 
logger = logging.getLogger(__name__)
final_response = ""

#ADD DOTENV
api_key = ""
interaction_user_prompt_header = f"\n\n🤖 Interaction time"
 
 
async def main(objective: str = None):
    # logger.debug("🚀 Starting example execution")
    ai_engine = AiEngine(api_key)
 
    function_groups: list[FunctionGroup] = await ai_engine.get_function_groups()
    # print(function_groups)
    public_group = next((g for g in function_groups if g.name == "Public"), None)
    if public_group is None:
        raise Exception('Could not find "Public" function group.')
 
    session = await ai_engine.create_session(function_group=public_group.uuid)
 
    # logger.info(interaction_user_prompt_header)
    if objective == None:
        objective = """
        user_query_string = I have been experiencing back pain and need to see a doctor soon.
        user_context_dict = {
                age: 69,
                gender: female,
                medical_history: diabetes,
                location: Richmond District, San Francisco,
                travel_preferences: walking distance,
                timing_preferences: this week
            }
        """
    await session.start(objective)
 
    try:
        empty_count = 0
        session_ended = False
 
        while empty_count < 100:
            messages: list[ApiBaseMessage] = await session.get_messages()
            if len(messages) == 0:
                empty_count += 1
            else:
                empty_count = 0
 
            message: ApiBaseMessage
            for message in messages:
                if is_task_selection_message(message_type=message.type):
                    task_selection_message: TaskSelectionMessage = message
 
                    # logger.info(interaction_user_prompt_header)
                    SKIP_PARAM = False
                    print("Please select a key from the list below:\n")
                    for _, option in task_selection_message.options.items():
                        print(f"➡ 🔑 {option.key}  ->  🧰 {option.title}")
                        if option.title == "Hospital Search Agent":
                            option_key='0'
                            SKIP_PARAM=True
                            continue
                    if SKIP_PARAM == False:
                        option_key = str(input("\nEnter task key: "))
 
                    # check the index
                    if option_key not in task_selection_message.options.keys():
                        raise Exception(f"🔴 Invalid task number.\n You selected: {option_key}")
                    # logger.debug(option_key)
                    await session.submit_task_selection(
                        message, 
                        [task_selection_message.options[option_key]]
                        )
                    del task_selection_message
                elif is_agent_message(message):
                    # LAST TIME IT IS CALLED
                    # final_response = message.text.capitalize()
                    try:
                        final_response = json.loads(json.loads(message.json())["text"].replace('"', '"""').replace("'", '"'))
                    except:
                        pass
                    response = ""
                elif is_ai_engine_message(message):
                    # logger.info(f"\n 🤖 ℹ Informative message \n\n ---> ✨{message.text}")
                    sleep(3.5)
                elif is_confirmation_message(message_type=message.type):
                    # logger.info(interaction_user_prompt_header)
                    print("Confirm:", message.payload)
                    if "user_dict" in message.payload.keys():
                        response = ""
                    else:
                        response = input("\nPress enter to confirm, otherwise explain issue:\n")
 
                    if response == "":
                        await session.submit_confirmation(message)
                    else:
                        await session.reject_confirmation(message, response)
                elif is_stop_message(message):
 
                    logger.info("\n 👋 Session has ended, thanks! ")
                    session_ended = True
                    break
 
            # if the session has concluded then break
            if session_ended:
                return final_response
 
            # logger.info(f"\n🤖 Processing\n")
            sleep(1.5)
            # logger.debug(f"No messages: {empty_count} times in a row")
 
    except Exception as e:
        # logger.debug(f"Unhandled exception: {e}")
        print("Error", e)
        raise e
    finally:
        # clean up the session
        await session.delete()
 
 
if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        # level=logging.INFO,
        format='%(asctime)s %(levelname)s %(module)s: %(message)s',
        datefmt="%H:%M:%S"
    )
    print(asyncio.run(main()))