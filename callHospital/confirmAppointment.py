import asyncio
import uuid
import requests
import json

async def confirm_appointment(data, mode):
 
    person_info = json.loads(data)

    name = person_info['name']
    selectedTime = person_info['availability'] 
    #hospital_contact

    phoneNumberId = "b3418c1b-5b69-4ca4-829c-c86a8fdbb22b"
    cust = {"number": "+13417669783"}
    authorization = "Bearer 89e8bedd-1abd-46f4-bae3-90753ae0581e"

    # Creating the message dynamically
    message_content = f"""
        You are a virtual assistant helping {name}. You are going to call the hospital for {name} to check the availability for an appointment.

        1. Call the hospital that matches the elderly patient's chosen availability.
        2. Confirm the booking for the {selectedTime}selected time and date, ensuring the appointment is scheduled.

        If no details are provided, assume the following:

        **Default Information:**
        - **Selected Appointment Time:** October 20, 2024, between 3 PM - 5 PM

        During the call:
        - Use friendly and casual language.
        - Be concise and to the point, keeping the conversation short.
        - do not ask the same question again

        Make sure to **clearly confirm the booking at the end of the conversation and thank the hospital staff.
    """

    payload = {
        "name": "check_hospital_availability",
        "assistant": {
            "transcriber": {
                "provider": "deepgram",
                "model": "nova-2",
                "language": "en",
                "smartFormat": True
            },
            "model": {
                "provider": "openai",
                "model": "gpt-4o-mini",
                "temperature": 0,
                "messages": [
                    {
                        "role": "assistant",
                        "content": message_content
                    }
                ],
                "maxTokens": 250,
                "toolIds":[
                    "8c1086c3-3323-4029-af84-bce1daed7d67"
                ],
            },
            "voice": {
                "fillerInjectionEnabled": True,
                "provider": "deepgram",
                "voiceId": "luna"
            }
        },
        "phoneNumberId":phoneNumberId,
        "customer": cust 
    }
   
    url = "https://api.vapi.ai/call"
    headers = {

        "Authorization": authorization,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    id = (response.json().get("id"))

    while response.json().get("status") != "ended":
        url = f"https://api.vapi.ai/call/{id}"
        response = requests.request("GET", url, headers=headers)
        await asyncio.sleep(2)

    print(response.text)
    return response.text

        


def main():
    # Example input data
    input_data = '''{
        "name": "John Doe",
        "age": 72,
        "birthday": "1952-07-29",
        "insurance_info": "MediHealth",
        "availability": {
            "time_hour": 14,
            "date": 20,
            "month": 10,
            "year": 2024
        },
        "hospital": {
            "name": "City Hospital",
            "number": "+1234567890",
            "operation_hour": "9 AM - 5 PM"
        }
    }'''

    input_data2 = '''{
        "name": "John Doe",
        "age": 72,
        "birthday": "1952-07-29",
        "insurance_info": "MediHealth",
        "availability": {
            "time_hour": 14,
            "date": 20,
            "month": 10,
            "year": 2024
        },
        "hospital": {
            "name": "City Hospital",
            "number": "+1234567890",
            "operation_hour": "9 AM - 5 PM"
        }
    }'''

    asyncio.run(confirm_appointment(input_data, 1))
    


if __name__ == "__main__":
    main()