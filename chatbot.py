from openai import OpenAI

client = OpenAI()

# accepts a preferred model (in this case "gpt-3.5-turbo") and a list of messages
# makes chat completions API call
# returns the response message content

def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
    model = model,
    messages = messages
    )
    
    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content


# prompt the user to ask a question
user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {
        "role": "system",            
        "content": "You are an assistant that always answers in the form of a poem."
    },
    {
        "role": "user",
        "content": user_input
    }
]

response_for_user = get_api_chat_response_message(model, messages)

print("\n" + response_for_user + "\n")

# test to see if github will commit this with no problem