from openai import OpenAI

client = OpenAI()

# accepts a preferred model (in this case "gpt-3.5-turbo") and a list of messages
# makes chat completions API call
# returns the response message content

def set_user_input_category(user_input):
    question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
    return "statement"

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
        "content": "You are an assistant that talks in the style of Shel Silverstein poems."
    },
    {
        "role": "user",
        "content": user_input
    }
]

response_for_user = get_api_chat_response_message(model, messages)

if set_user_input_category(user_input) == "question":
    response_for_user = "Good question! " + response_for_user

print("\n" + response_for_user + "\n")

# test to see if github will commit this with no problem