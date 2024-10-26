import asyncio
import uuid
import requests
import json

async def check_hospital_availability(data):

    person_info = json.loads(data)

    name = person_info['name']
    insurance_info = person_info['insurance_info']
    availability = person_info['availability'] 
    reason_for_visit = person_info['reason_for_visit'] 
    #hospital_contact

    phoneNumberId = "b3418c1b-5b69-4ca4-829c-c86a8fdbb22b"
    cust = {"number": "+13417669783"}
    authorization = "Bearer 89e8bedd-1abd-46f4-bae3-90753ae0581e"

    message_content = f"""
        You are a virtual assistant helping {name}. You are going to call the hospital for {name} to check the availability for an appointment.

        Your task is to:  
        1. Call the hospital and ask the hospital whether if they accept patient's insurance type which is {insurance_info}. 
        2. If the insurance is **not** supported, politely hang up. 
        3. If the insurance **is** supported, inform the hospital about the patient’s symptoms .
        4. Ask for available appointment times that match the patient’s availability, but **do not** make a reservation. Just say I will double confirm and get back to you.  
        5. After you get the appointment information. Say thank you and hang up. 
        
        **Patient Information:**
        - **Patient Name:** {name}
        - **Insurance Provider:** {insurance_info}
        - **Reason for Visit:** {reason_for_visit}
        - **Preferred Availability:** {availability}

        During the call: 
        1. Use casual responses and maintain proper flow of the conversation and no gaps. 
        2. Remember to **only** check availability without making a reservation, and confirm all details with the hospital at the end.  
        Keep the conversation short and avoid over-explaining.
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
                "toolIds": [
                    "f4425b21-86f8-4820-a20c-c0797a1db985",
                    "8c1086c3-3323-4029-af84-bce1daed7d67"
                ],
                "maxTokens": 250
            },
            "voice": {
                "fillerInjectionEnabled": True,
                "provider": "deepgram",
                "voiceId": "luna"
            }
        },
        "customer": cust,
        "phoneNumberId": phoneNumberId
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

    #TODO: throw this into an LLM, get something regarding did we successfully get a time or not
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
        },
        "reason_for_visit":"headache"
    }'''

    asyncio.run(check_hospital_availability(input_data))
    


if __name__ == "__main__":
    main()